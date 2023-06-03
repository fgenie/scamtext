import java.util.regex.Pattern

fun isSpam(text: String): Boolean {
    // Check for spam keywords
    val spamKeywords = listOf("광고", "핫딜", "편지함으로", "지금 바로", "무료거부", "지원금", "안전거래", "입장코드", "추천주",
            "수익", "주식", "특별한 혜택")

    for (keyword in spamKeywords) {
        if (text.contains(keyword)) {
            return true
        }
    }

    // Check for url patterns
    val urlPattern1 = Pattern.compile("https?://\\S+")
    val urlPattern2 = Pattern.compile("www\\.\\S+")
    val urlMatch1 = urlPattern1.matcher(text).find()
    val urlMatch2 = urlPattern2.matcher(text).find()

    if (urlMatch1 || urlMatch2) {
        if ("원" in text || "계약" in text || "시작" in text || "특별" in text) {
            return true
        }
    }

    // Check for money and percentage patterns
    val moneyPattern = Pattern.compile("\\d{1,3}(,\\d{3})*(\\.\\d{2})?원")
    val moneyMatch = moneyPattern.matcher(text).find()
    val percentagePattern = Pattern.compile("\\d{1,3}(\\.\\d{1,2})?%")
    val percentageMatch = percentagePattern.matcher(text).find()

    return moneyMatch && percentageMatch
}
