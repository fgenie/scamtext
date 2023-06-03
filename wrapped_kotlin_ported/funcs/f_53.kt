import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // check for spam keywords
    val spamKeywords = listOf("(광고)", "수익", "무료", "VIP", "안전", "건", "신입", "정보", "트레이딩", "대표님", "추천", "공개", "체험반", "보유종목", "프로", "실력", "초보", "개인정보", "비밀번호", "복구", "님", "혜택")

    // check for URL patterns
    val urlPattern: Pattern = Pattern.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

    // check for phone numbers
    val phonePattern: Pattern = Pattern.compile("(\\d{2,4}-\\d{3,4}-\\d{3,4})|(\\(\\d{2,4}\\)\\d{3,4}-\\d{3,4})")

    // check if message contains any spam keywords
    if (spamKeywords.any { message.contains(it) }) {
        return true
    }

    // check if message contains URLs
    if (urlPattern.matcher(message).find()) {
        return true
    }

    // check if message contains phone numbers
    if (phonePattern.matcher(message).find()) {
        return true
    }

    // if message passed all the checks, it is not spam
    return false
}
