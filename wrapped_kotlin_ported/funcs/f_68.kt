import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Check for presence of numbers or special characters
    if (Pattern.compile("\\d").matcher(message).find() || Pattern.compile("[^\\w\\s]").matcher(message).find()) {
        // Check for presence of URL
        if (Pattern.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\\\(\\\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+").matcher(message).find()) {
            return true
        }

        // Check for presence of short URL
        if (Pattern.compile("bit\\.ly|goo\\.gl|me2\\.kr|tinyurl\\.com|ocx\\.kr|buly\\.kr").matcher(message).find()) {
            return true
        }

        // Check for promotional keywords
        val promotional_keywords = arrayOf(
            "광고", "프로모션", "이벤트", "쿠폰", "할인", "구인", "회원가입", "신규", "주식", "공시", "정보", "단독", "상한가", "경품"
        )
        for (keyword in promotional_keywords) {
            if (message.contains(keyword)) {
                return true
            }
        }
    }
    return false
}
