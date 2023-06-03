fun isSpam(message: String): Boolean {
    val spamPhrases = listOf(
        "당첨 되셨습니다",
        "공시발표",
        "급등예정",
        "증권사 매집주 공개",
        "정회원방 입장"
    )

    for (phrase in spamPhrases) {
        if (phrase in message) {
            return true
        }
    }

    val symbolsPattern = "[!@#\$%^&*\\(\\)\\-_=+\\[\\]\\{\\};:\\"\\|,.<>/?~`§※✭]"
    val symbolsRegex = symbolsPattern.toRegex()
    val symbolMatches = symbolsRegex.findAll(message)
    if (symbolMatches.count() > 5) {
        return true
    }

    val urlPattern =
        Regex("(?:http|https)://|bit\\.ly|han\\.gl|me2\\.kr|gg\\.gg|buly\\.kr|openkakao\\.at|abit\\.ly")
    if (urlPattern.containsMatchIn(message)) {
        return true
    }

    val numbersPattern = "\\d{4,}|[0-9]+원|[0-9]+,\\d{3,}|[0-9]+%\\s*\\+"
    if (numbersPattern.toRegex().containsMatchIn(message)) {
        return true
    }

    return false
}
