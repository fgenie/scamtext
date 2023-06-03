fun isSpam(message: String): Boolean {
    // Check for excessive use of special characters
    val specialChars = Regex("""[\*\.\(\)\\\-/@\[\]<>]""").findAll(message)
    if (specialChars.count() > 20) {
        return true
    }

    // Check for excessive use of numbers
    val numbers = Regex("""\d+""").findAll(message)
    if (numbers.count() > 15) {
        return true
    }

    // Check for pattern of shortened urls
    val urls = Regex("""(https?://[a-zA-Z0-9./]+)""").findAll(message)
    if (urls.count() > 5) {
        return true
    }

    // Check for presence of keywords in the message
    val keywords = arrayOf("상한가", "추천", "입장", "무료")
    keywords.forEach { keyword ->
        if (message.contains(keyword)) {
            return true
        }
    }
    return false
}
