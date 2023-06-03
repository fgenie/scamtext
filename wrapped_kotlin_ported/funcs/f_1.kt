fun isSpam(message: String): Boolean {
    var lowerCaseMessage = message.lowercase()

    val spamKeywords = arrayOf(
        "추천주", "적중", "지급", "퍼센트", "확인", "축하", "상한가",
        "월 체", "추친", "click", "오시는길", "텔레그램", "텔레그램 친추",
        "건설알미늄", "벳썸", "무제한 충전", "소니드", "더메티팜", "메이저 계열",
        "VIP 담당 에이전시", "다음주"
    )

    val normalKeywords = arrayOf(
        "친구", "오랜만", "여기로", "여기와라", "하이", "내일", "자료", "오키",
        "안녕", "나는 잘지내", "가정의 달 그린피", "손이아파"
    )

    val urlPattern = Regex("""http\S+|www\..+\..+|bit\.ly\S+|https:\/\/me2\.kr\S+""")

    // Check if message contains any URLs
    if (urlPattern.containsMatchIn(lowerCaseMessage)) {
        return true
    }

    // Check if message contains any spam keywords
    if (spamKeywords.any { spamWord -> spamWord in lowerCaseMessage }) {
        return true
    }

    // Check if message contains any normal words
    if (normalKeywords.any { normalWord -> normalWord in lowerCaseMessage }) {
        return false
    }

    return false
}
