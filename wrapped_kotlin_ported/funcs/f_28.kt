fun isSpam(text: String): Boolean {
    // Basic spam indicators
    val spamWords = listOf("상한가", "추천", "vip", "관심종목", "명가", "수익률", "비번", "비밀번호", "차트", "투자")
    val textLower = text.toLowerCase()
  
    for (word in spamWords) {
        if (word in textLower) {
            return true
        }
    }
  
    // Check for URLs
    val urlRegex = """http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+""".toRegex()
    val urls = urlRegex.findAll(text).toList()
    if (urls.isNotEmpty()) {
        return true
    }
  
    // Check for unusual patterns
    val unusualPatterns = listOf("[0-9]+%[\\+\\-↑]".toRegex(), "key:[0-9]+".toRegex(), "코드번호 [0-9]+".toRegex())
    for (pattern in unusualPatterns) {
        if (pattern.find(text) != null) {
            return true
        }
    }
  
    // Check for sequences of numbers and characters combined
    val sequences = "([0-9]+[a-zA-Z]+|[a-zA-Z]+[0-9]+)".toRegex().findAll(text).toList()
    if (sequences.size > 1) {
        return true
    }
  
    return false
}
