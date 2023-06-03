import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    val spamKeywords = listOf(
        "추천주", "수익", "상한가", "환장", "VVIP", "유료", "증권", "혜택", "지원금", "관망", "매수", "매도", "투자", "거래", "성과",
        "매매", "추천", "종목", "체험반", "광고", "상승", "상향", "하락", "단기", "장기", "카카오톡 제재", "안전한 업", "생활비 수익", "%",
        " 백분율", "계약", "월 수익", "주식", "분석", "프로 성과", "다음 일정"
    )

    val messageLower = message.toLowerCase()
    var numKeywords = 0

    for (keyword in spamKeywords) {
        if (keyword.toLowerCase() in messageLower) {
            numKeywords++
        }
    }
    val urlPattern: Pattern = Pattern.compile("https?://(?:[-\\w.]|(?:%[\\da-fA-F]{2}))+")
    val numUrls = urlPattern.matcher(message).results().count()
    val phoneNumberPattern: Pattern = Pattern.compile("\\d{2,4}-?\\d{2,4}-?\\d{4}")
    val numPhoneNumbers = phoneNumberPattern.matcher(message).results().count()

    return numKeywords > 1 || numUrls > 0 || numPhoneNumbers > 1
}
