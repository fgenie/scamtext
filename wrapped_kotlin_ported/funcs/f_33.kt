import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Look for spam-specific keywords and patterns in the message
    val keywords = listOf("추천주", "지금 가입", "VIP", "돌파", "참여", "상한가확정", "청개구리VIP", "출신", "수익", "루멘스")
    val urlPattern = Pattern.compile("(https?://\\S+|me2\\.\\S+|vo\\.la/\\S+|dokdo\\.\\S+)")
    var spamScore = 0

    for (keyword in keywords) {
        if (message.contains(keyword)) {
            spamScore++
        }
    }

    if (urlPattern.matcher(message).find()) {
        spamScore++
    }

    return spamScore > 1 // If the spamScore is greater than 1, classify the message as spam
}
