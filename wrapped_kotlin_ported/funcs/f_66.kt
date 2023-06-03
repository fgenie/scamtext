fun isSpam(message: String): Boolean {
    val spamPhrases = listOf("상한가", "특별 할인", "무료수신거부", "%", "MOU", "특가", "소문난 주식")

    spamPhrases.forEach {
        if (it in message) return true
    }

    val specialChars = Regex("[!@#$%^&*()\\-_=+\\[\\]{};:\'\"|,<.>/?]+").findAll(message).toList()
    if (specialChars.size > 5) return true

    val urls = Regex("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\\\(\\\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+").findAll(message).toList()
    if (urls.size > 1) return true

    val numbers = Regex("[0-9]+").findAll(message).toList()
    if (numbers.size > 3) return true

    val nonKorean = Regex("[^ㄱ-하-ㅣ가-힣\\s]+").findAll(message).toList()
    if (nonKorean.size > 5) return true

    return false
}
