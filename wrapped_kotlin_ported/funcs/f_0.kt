import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Patterns that can indicate a message is spam
    val spamWords = arrayOf("축하합니다", "공개합니다", "\\d{1,2}일추천", "알려드린", "무료체험", "돌파", "상한가", "최소.*연상")
    val urlShorteners = arrayOf("bit.ly", "me2.kr", "han.gl")
    val consecutiveNumbers = "\\d+\\.?\\d*" // e.g., 30%, 19일
    val suspiciousReferral = "\\d{1,2}[일월수목금토일]"

    // Flags for checking whether a message is spam
    val containsSpamWord = spamWords.any { Pattern.compile(it).matcher(message).find() }
    val containsShortUrl = urlShorteners.any { message.contains(it) }
    val containsConsecutiveNumbers = Pattern.compile(consecutiveNumbers).matcher(message).find()
    val containsSuspiciousReferral = Pattern.compile(suspiciousReferral).matcher(message).find()

    // Evaluate if message is a spam based on the flags
    if (containsSpamWord && containsShortUrl) {
        return true
    }
    if (containsConsecutiveNumbers && containsSuspiciousReferral) {
        return true
    }
    if (containsSpamWord && containsConsecutiveNumbers) {
        return true
    }
    if (containsSpamWord && containsSuspiciousReferral) {
        return true
    }
    if (containsShortUrl && (containsConsecutiveNumbers || containsSuspiciousReferral)) {
        return true
    }
    // If none of the conditions are met, return false, indicating the message is not spam
    return false
}
