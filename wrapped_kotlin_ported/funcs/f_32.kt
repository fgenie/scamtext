fun isSpam(message: String): Boolean {

    val spamWords = listOf(
        "광고", "랜선", "셀프무료점검", "무료거부", "무료패키지", "탈퇴", "증선", "추천", "지난",
        "성공적", "파랑", "특별", "할인", "행사", "회원", "혜택", "추가", "종목", "나가요",
        "확정", "입장", "체크", "사업", "목표", "참여",
        "숙박", "이벤트"
    )

    val urlPattern = Regex("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.＆+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    val emailPattern = Regex("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._+-]+\\.[a-zA-Z]{2,}")
    val phonePattern = Regex("\\d{2,4}-\\d{2,4}-\\d{4}")

    val hasUrl = urlPattern.containsMatchIn(message)
    val hasEmail = emailPattern.containsMatchIn(message)
    val hasPhone = phonePattern.containsMatchIn(message)

    val possibleSpam = if (hasUrl || hasEmail || hasPhone) true else false

    val spamWordCount = spamWords.sumOf { message.count(it) }

    val multipleSpamWords = spamWordCount > 2

    val isSpamResult = multipleSpamWords || possibleSpam

    return isSpamResult
}
