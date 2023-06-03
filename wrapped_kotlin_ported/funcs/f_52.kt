import java.util.regex.Pattern

fun isSpam(text: String): Boolean {
    // Check for common spam features
    val spamFeatures = arrayOf(
        "https?:\\/\\/",  // URLs
        "\\d+\\.\\d+%",  // percentages
        "\\d+원",  // KRW amounts
        "^축하합니다",  // Congratulations
        "VIP",  // VIP
        "수익률",  // Profit rate
        "상한가",  // Price ceiling
        "적중",  // Hit rate
        "배터리",  // Battery
        "사업",  // Business
        "계열사",  // Subsidiary
        "혹여라도",  // In any case
        "오픈합니다",  // Open
        "프로젝트",  // Project
        "최소인원",  // Minimum number of members
        "추천",  // Recommendation
        "종목",  // Stock item
        "투자",  // Investing
        "시장",  // Market
        "공시",  // Disclosure
        "기관",  // Institutions or Organizations
        "세력"  // Power, usually referring to influential groups
    )

    for (feature in spamFeatures) {
        val regex = Pattern.compile(feature)
        if (regex.matcher(text).find()) {
            return true
        }
    }

    return false
}
