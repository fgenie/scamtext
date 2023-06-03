fun isSpam(message: String): Boolean {
    // Check for typical spam patterns related to money and URLs
    val moneyKeywords = arrayOf("만원", "백만원", "신속", "지원금", "할인", "혜택", "마감")
    val spamUrlPattern = Regex("(https?:\\/\\/\\S*[정보투자]|\\S*(bit\\.ly|me2\\.kr|asq\\.kr|openkakao)\\S*)")
    if (moneyKeywords.any { it in message } || spamUrlPattern.containsMatchIn(message)) {
        return true
    }
    // Check for advertisement tag in the message
    if ("(광고)" in message) {
        return true
    }
    return false
}
