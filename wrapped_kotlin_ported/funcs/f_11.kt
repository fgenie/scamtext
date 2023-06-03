fun isSpam(message: String): Boolean {
    val spamPhrases = arrayOf(
        Regex("카카오톡제재"), Regex("테|_|\u0028|\u0029|£|€|\\.| |그램으로 이동"), Regex("\\d월.험반"), Regex("잔여 [\\d]+/"),
        Regex("신년맞이 모집"), Regex("무료거부"), Regex("\\d+일 알려드린"), Regex("신 청 하 신"), Regex("인증\\w+"), Regex("클릭"),
        Regex("openkakao.at|me2.kr|vvvkauy.com|ocx.kr|a.to"), Regex("\\d%.상승"),
        Regex("사만 원"), Regex("지니틱스"), Regex("지금 날짜"), Regex("폐.배터리")
    )

    val specialChars = arrayOf(
        Regex("\\.{2,}"), Regex("!{2,}"), Regex("\\?{2,}"), Regex("\u2665")
    )

    val specialCharThreshold = 0.25
    val spamRegex = Regex(spamPhrases.joinToString(separator = "|") + "|" + specialChars.joinToString(separator = "|"))

    val matches = spamRegex.findAll(message)
    val specialCharCount = matches.map { regexMatch ->
        specialChars.count { specialCharRegex ->
            specialCharRegex.matches(regexMatch.value)
        }
    }.sum()

    return matches.isNotEmpty() && (specialCharCount.toDouble() / maxOf(1, message.length)) <= specialCharThreshold
}
