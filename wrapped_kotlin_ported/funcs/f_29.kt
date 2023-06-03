import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Keywords and phrases often found in spam messages
    val spamKeywords = arrayOf(
        "무료", "출금", "적중", "상품목록", "기대 성과", "지급중", 
        "상한가", "성공현황", "성과 보여드리고", "공지", "추천"
    )

    // Patterns often found in scam URLs
    val scamUrlPatterns = arrayOf(
        "(?i)bit\\.ly",
        "(?i)me2\\.kr"
    )

    // Checking if any spam keyword is found in the message
    for (keyword in spamKeywords) {
        if (message.contains(keyword)) {
            return true
        }
    }

    // Checking if any scam URL pattern is found in the message
    for (pattern in scamUrlPatterns) {
        val regex = Pattern.compile(pattern)
        val matcher = regex.matcher(message)

        if (matcher.find()) {
            return true
        }
    }

    // If none of the spam indicators are found, the message is considered normal
    return false
}
