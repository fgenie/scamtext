fun isSpam(message: String): Boolean {
    val unwantedPhrases = listOf(
        Regex("^\\*"),
        Regex("연속 [^ ]*(?:상승장|수익률검증|체험반)"),
        Regex("(?:추천|분석|참여)(?:[^\n]*\\?= http)"),
        Regex("미래에셋증권"),
        Regex("(수익|입장|펀\\d+|안전)종목"),
        Regex("한정수량|타점|입수|상단|급등강")
    )
    val pattern = unwantedPhrases.joinToString(separator = "|") { it.pattern }
    return Regex(pattern).find(message) != null
}
