import java.util.regex.Pattern

fun isSpam(text: String): Boolean {
    // Check for spam keywords and patterns
    val spamKeywords = arrayOf("광고", "거부", "클릭", "해지", "이벤트", "공짜", "하세요", "무료", "최고", "상위", "증권사", "특별", "혜택", "무료거부", "입장코드", "특별정보방", "여의도", "입장", "금전")

    // Check for URL patterns
    val urlPattern = Pattern.compile("(http|https)://\\S+")

    // Check for phone number patterns
    val phonePattern = Pattern.compile("\\d{2,4}-\\d{3,4}-\\d{4}")

    // Check for non-normal characters
    val nonNormalChars = Pattern.compile("[^가-힣a-zA-Z0-9.,?!:;\\-\\s]+")

    // Count the number of spam indicators
    var spamCount = 0

    // Check for spam keywords
    for (keyword in spamKeywords) {
        if (text.contains(keyword)) {
            spamCount++
        }
    }

    // Check for URL patterns
    if (urlPattern.matcher(text).find()) {
        spamCount++
    }

    // Check for phone number patterns
    if (phonePattern.matcher(text).find()) {
        spamCount++
    }

    // Check for non-normal characters
    if (nonNormalChars.matcher(text).find()) {
        spamCount++
    }

    // If more than 1 spam indicators are detected, classify the message as spam
    return spamCount >= 2
}
