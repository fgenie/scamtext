fun isSpam(text: String): Boolean {
    val spamKeywords = listOf("상한가", "추친중", "무료체험", "수익보장", "정보입수", "출발", "마감", "무료거부", "코드", "체험반", "초대", "실력입증", "알려드린", "카카오톡제재")
    val suspiciousUrlPattern = Regex("(https?://\\S+)")
    val suspiciousUrlPattern2 = Regex("han.gl/\\S+")

    val foundKeyword = spamKeywords.any { it in text }
    val foundSuspiciousUrl = suspiciousUrlPattern.containsMatchIn(text) || suspiciousUrlPattern2.containsMatchIn(text)

    return foundKeyword || foundSuspiciousUrl
}
