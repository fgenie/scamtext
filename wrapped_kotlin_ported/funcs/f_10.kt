import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Find patterns commonly found in spam messages
    val patterns = arrayOf(
        "(광고)", // Advertising in Korean
        "https?://\\S+", // URLs
        "\\b[백만천만만억]+원?\\b", // Large amount of money in Korean
        "[%][0-9]+", // Percentage
        "\\b지원\\b", // Support in Korean
        "\\b수익\\b", // Profit in Korean
        "\\b주식\\b", // Stock in Korean
        "\\b어디서 만나\\??\\b", // Where to meet in Korean
        "\\b청개구리\\b", // Frog in Korean
        "\\b투자\\b", // Investment in Korean
        "\\b정보\\b", // Information in Korean
        "\\b초대\\b", // Invitation in Korean
    )

    var spamScore = 0

    for (pattern in patterns) {
        val regex = Pattern.compile(pattern)
        if (regex.matcher(message).find()) {
            spamScore += 1
        }
    }

    // If spam_score is greater or equal to 1, it is considered spam
    return spamScore >= 1
}
