fun isSpam(message: String): Boolean {
    val spamWords = listOf(
        "축하",
        "상한가",
        "확정",
        "치료제",
        "공개",
        "다음타자",
        "C제약",
        "긴급입수정보",
        "관련주",
        "프로젝트",
        "참여",
        "입장",
        "상담",
        "문의",
        "빠르게",
        "지급",
        "체험반",
        "독보적인",
        "수익 실탁",
        "한농화성",
        "무료",
        "체험",
        "비밀번호",
        "VIP",
        "전환"
    )

    // Check for URL
    val urlRegex = """http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"""
    val urlCheck = Regex(urlRegex).containsMatchIn(message)

    // Check for spam words
    val spamWordCheck = spamWords.any { word -> message.contains(word) }

    return spamWordCheck || urlCheck
}
