
import java.util.regex.Pattern

fun isSpam(message: String): Boolean {

    // Checking for spam URL patterns
    val spamUrlPatterns = arrayOf(
        "(?i)https?:\\/\\/(?:me2.kr|buly.kr|opcn\\-kakao.com|han.gl|abit.ly)\\/\\S*",
        "(?i)ⓢlⓩ102.com",
        "(?i)orl.kr\\/\$\\S*",
        "(?i)https?:\\/\\/openkakao.io/\\S*"
    )

    for (pattern in spamUrlPatterns) {
        if (Pattern.compile(pattern).matcher(message).find()) {
            return true
        }
    }

    // Checking for other spam patterns
    val spamPatterns = arrayOf(
        "(?i)(vip|vvip)투자반",
        "(?i)차별화 된",
        "(?i)시작하루만에",
        "(?i)추천주 현황",
        "(?i)slot\uD83C\uDFAFzone",
        "(?i)지니틱스",
        "(?i)카카오톡제재",
        "(?i)[5일평균].*[8,930.000원]",
        "(?i)문의▼",
    )

    for (pattern in spamPatterns) {
        if (Pattern.compile(pattern).matcher(message).find()) {
            return true
        }
    }

    // If none of the spam patterns are present
    return false

}
