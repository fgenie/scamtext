import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    val spamKeywords = listOf(
        "무료", "수익", "광고", "증.권", "안내", "금일부터", "최고급",
        "강의", "교육", "완료", "적립금", "확률", "세계", "비밀번호",
        "추천", "단체방", "오픈", "수익률", "매매", "마이크로", "내일부터", "리뉴얼"
    )

    val regularTerms = listOf(
        "안녕하세요", "넵", "감사합니다", "수고하세요", "좋은 하루 보내",
        "끝나고 뭐하냐?", "야야", "오늘", "안녕", "게임한판",
        "상황", "인터넷", "뱅킹", "계좌"
    )

    var message = message.toLowerCase()

    var spamCount = 0
    spamKeywords.forEach { keyword ->
        if (message.contains(keyword)) {
            spamCount++
        }
    }

    var regularCount = 0
    regularTerms.forEach { term ->
        if (message.contains(term)) {
            regularCount++
        }
    }

    val linkPattern = Pattern.compile("https?://\\S+")
    val percentPattern = Pattern.compile("\\d{2}\\.\\d{2}%?")

    if (linkPattern.matcher(message).find() || percentPattern.matcher(message).find()) {
        spamCount++
    }

    return spamCount > regularCount
}
