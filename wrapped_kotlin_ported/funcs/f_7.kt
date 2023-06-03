fun isSpam(message: String): Boolean {
    val shorteners = listOf("bit.ly", "goo.gl", "tinyurl.com", "ow.ly", "me2.kr", "t.co", "t2m.io", "han.gl", "opcn-kakao.com")
    shorteners.forEach { shortener ->
        if (shortener.toLowerCase() in message.toLowerCase()) {
            return true
        }
    }

    val specialCharacters = listOf('+', '*', '_', '.')
    val specialCharCount = specialCharacters.sumBy { message.count { it == char } }
    if (specialCharCount.toDouble() / message.length > 0.1) {
        return true
    }

    val phoneNumbers = Regex("\\d{10,15}").findAll(message).toList()
    if (phoneNumbers.isNotEmpty()) {
        return true
    }

    val upperCaseCount = message.count { it.isUpperCase() }
    if (upperCaseCount.toDouble() / message.length > 0.3) {
        return true
    }

    val nonKoreanCount = message.count { (it.toInt() < 0xAC00 || it.toInt() > 0xD7AF) && (it.toInt() < 0x3130 || it.toInt() > 0x318F) }
    if (nonKoreanCount.toDouble() / message.length > 0.7) {
        return true
    }

    return false
}
