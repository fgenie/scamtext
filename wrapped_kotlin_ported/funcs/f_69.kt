import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Spam indicators
    val spamIndicators = arrayOf(
        "[\\d,]*원",
        "\\d{1,2}% ?~",
        "\\d{1,2}대",
        "http[s]?://",
        "주식",
        "종목",
        "익 절 가",
        "펀드매니저",
        "수익률",
        "매매승률",
        "목표가",
        "최소",
        "매일",
        "최대",
        "최고"
    )

    // Iterate through spam indicators and check if any are present in the message
    for (indicator in spamIndicators) {
        val pattern = Pattern.compile(indicator, Pattern.CASE_INSENSITIVE)
        val matcher = pattern.matcher(message)
        if (matcher.find()) {
            return true
        }
    }

    // If none of the spam indicators are present, consider it a normal message
    return false
}
