fun isSpam(message: String): Boolean {
    val spamPatterns = listOf(
        "(광고)",
        "\\d{2,}%",
        "[ㄱ-ㅎㅏ-ㅣ가-힣]*[주식|추천|상승|하락|투자]",
        "(상한가|하한가)",
        "\\d{1,2}월\\s?체험",
        "\\d{2,3}만원",
        "\\+[가-힣]+주",
        "\\b\\d{1,2}타\\b",
        "(https?:\\/\\/[\w\\.-]+\\.[\w\\.-]+\\/\\S*)",
        "-코인",
        "[가-힣]+계약",
        "(시작하세요|수익|적중|투자)+" +
                "(https?:\\/\\/(bit\\.ly|dokdo\\.in|me2\\.kr|me2\\.do)\\S*)"
    ).map { it.toRegex() }

    for (pattern in spamPatterns) {
        if (pattern.containsMatchIn(message)) {
            return true
        }
    }

    return false
}
