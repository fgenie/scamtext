import java.util.regex.Pattern

fun isSpam(text: String): Boolean {
    // Check for common spam characteristics
    val spamIndicators = arrayOf(
        "(광고)",  // 'Advertisement'
        "\\d{1,2}월",  // 'Month'
        "\\d{1,2}%".toRegex(), // 'Percentage'
        "www\\.\\w+\\.com".toRegex(), // 'URLs'
        "https?://(?:[-\\w.]|(?:%[\\da-fA-F]{2}))+".toRegex(),
        "무료수신거부",  // 'Free message rejection'
        "적중",  // 'Hit'
        "상한가",  // 'Upper limit(potentially stock market spam)'
        "\\d{1,2}만원".toRegex(),  // Large amounts of money
        "금일" // 'Today'
    )

    // Compile the regular expressions
    val spamPatterns = spamIndicators.map { Pattern.compile(it) }

    // Check each pattern for a match
    for (pattern in spamPatterns) {
        if (pattern.matcher(text).find()) {
            return true
        }
    }

    // If none of the spam indicators were found, consider the message as not spam
    return false  
}
