fun isSpam(message: String): Boolean {
    
    val suspiciousDomains = arrayOf("han.gl", "me2.kr", "bit.ly", "ko.gl", "vo.la", "asq.kr", "buly.kr")
    val urlPattern = Regex("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\\\(\\\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    val urls = urlPattern.findAll(message).map { it.value }.toList()
    for (url in urls) {
        for (domain in suspiciousDomains) {
            if (domain in url) {
                return true
            }
        }
    }
    
    val specialCharPattern = Regex("[!@#\$%^&*_+=|;:?<>,.(){}\\[\\]]")
    val specialChars = specialCharPattern.findAll(message).map { it.value }.toList()
    if (specialChars.size.toDouble() / message.length.toDouble() > 0.3) {
        return true
    }
    
    val numericalCharPattern = Regex("[0-9]")
    val numericalChars = numericalCharPattern.findAll(message).map { it.value }.toList()
    if (numericalChars.size.toDouble() / message.length.toDouble() > 0.4) {
        return true
    }
    
    val consecutiveNewlinePattern = Regex("\\s?(\\n){2,}")
    val consecutiveNewlines = consecutiveNewlinePattern.findAll(message).map { it.value }.toList()
    if (consecutiveNewlines.isNotEmpty()) {
        return true
    }
    
    val capitalLetters = Regex("[A-Z]").findAll(message).map { it.value }.toList()
    if (capitalLetters.size.toDouble() / message.length.toDouble() > 0.2) {
        return true
    }
    
    return false
}
