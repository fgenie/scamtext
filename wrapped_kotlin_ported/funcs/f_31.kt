fun isSpam(message: String): Boolean {
    val spamKeywords = listOf(
        "무료거부",
        "프로젝트",
        "지원금",
        "특별",
        "혜택",
        "상승",
        "수익",
        "웹그룹",
        "광고",
        "초대",
        "폭등"
    )

    val normalKeywords = listOf(
        "안녕하세요",
        "하루",
        "이제",
        "문의",
        "수고",
        "회의",
        "친구"
    )

    var msg = message.toLowerCase().trim()

    var spamCount = 0
    var normalCount = 0

    // Count spam keywords in the message
    for (keyword in spamKeywords) {
        if (msg.contains(keyword)) {
            spamCount++
        }
    }

    // Count normal keywords in the message
    for (keyword in normalKeywords) {
        if (msg.contains(keyword)) {
            normalCount++
        }
    }

    return spamCount > normalCount
}
