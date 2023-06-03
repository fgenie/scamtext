import com.google.gson.Gson
import java.nio.file.Files
import java.nio.file.Paths

data class Response(
    val input_txts: List<String>,
    val voted_spam_fraction: List<Double>,
    val decisions: List<Boolean>,
    val num_functions: Int
)

typealias CheckerFunction = (String) -> Boolean

fun evalDirs(conf: Conf): List<Path> {
    val evaluateDirs = Files.walk(Paths.get(conf.root, conf.expname))
        .filter { it.fileName.toString().startsWith(conf.globpattern) && it.fileName.toString().contains(conf.data) }
        .toList()
    return evaluateDirs
}

fun tandemExecution(functions: List<CheckerFunction>, txt: String): Double {
    val results = functions.map { func -> if (func(txt)) 1.0 else 0.0 }
    return results.average()
}

fun preproc(txts: List<String>): List<String> {
    val headers = listOf("[Web발신]", "[국외발신]", "[국제발신]")
    val headersPattern = headers.joinToString(separator = "|") { Regex.escape(it) }
    val urlPattern = "https?://(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%_+.~#?&//=]*)"

    val processedTxts = txts.map { txt ->
        txt.replace(headersPattern.toRegex(), "").replace(urlPattern.toRegex(), "")
    }
    val newtxt = txts[0].replace(urlPattern.toRegex(), "").replace(headersPattern.toRegex(), "")

    return processedTxts
}

fun main(
    inputmsgsCsv: String = "3_inputmsgs.csv",
    decisionOnly: Boolean = false,
    thld: Double = 0.35 // affects performance. do not configure this.
): Any {
    // load checkers
    val indivCheckers = mutableListOf<CheckerFunction>()
    Files.newDirectoryStream(Paths.get("funcs"), "f_*.kt").use { stream ->
        stream.forEach { path ->
            val className = path.toFile().nameWithoutExtension
            val checkerFunction = Class.forName(className)
                .getDeclaredMethod("isSpam", String::class.java)
                .let { method ->
                    { txt: String -> method.invoke(null, txt) as Boolean }
                }
            indivCheckers.add(checkerFunction)
        }
    }

    // load input_txt msgs
    val inputTxts_ = Files.readAllLines(Paths.get(inputmsgsCsv))
    val inputTxts = preproc(inputTxts_)
    val votedSpamRatio = inputTxts.map { txt -> tandemExecution(indivCheckers, txt) }
    val decisions = votedSpamRatio.map { r -> r >= thld }
    val numFunctions = indivCheckers.size

    return if (decisionOnly) {
        decisions
    } else {
        val response = Response(
            input_txts = inputTxts_,
            voted_spam_fraction = votedSpamRatio,
            decisions = decisions,
            num_functions = numFunctions
        )
        Gson().toJson(response)
    }
}

fun main(args: Array<String>) {
    val conf = Conf(root = "", expname = "", globpattern = "", data = "")
    main()
}

data class Conf(
    val root: String,
    val expname: String,
    val globpattern: String,
    val data: String
)
