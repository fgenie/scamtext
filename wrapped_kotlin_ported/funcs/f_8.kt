
import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Check for ad-related keywords
    val adKeywords = listOf("(광고)", "무료거부", "주식", "http", "추천")
    if (adKeywords.any { keyword -> message.contains(keyword) }) {
        return true
    }

    // Check for excessive use of special characters
    val specialChars = listOf('!', '?', '@', '#', '*', '=', '+')
    val count = specialChars.sumBy { char -> message.count { it == char } }
    if (count >= 5) {
        return true
    }

    // Check for consecutive capital letters
    val pattern = Pattern.compile("[A-Z|가-힣]{3,}")
    val matcher = pattern.matcher(message)
    if (matcher.find() && matcher.find()) {
        return true
    }

    // Check for numeric sequences
    val numericPattern = Pattern.compile("\\d{3,}")
    val numericMatcher = numericPattern.matcher(message)
    if (numericMatcher.find()) {
        return true
    }

    // If none of the above conditions are met, consider the message as normal
    return false
}

