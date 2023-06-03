import java.util.regex.Pattern

fun isSpam(text: String): Boolean {
    val spamKeywords = listOf("랜드마크파워", "증 권", "무료체험", "민수 님", "마감", "회원 가", "알 에프 세미",
                              "주식 매매 성과", "증센터 고객 센터", "자동 진행", "추가 종목", ",확정", "백화점 상품권", "경품혜택", "방송하는 이 선생")
    
    for (keyword in spamKeywords) {
        if (keyword in text) {
            return true
        }
    }

    // URLs that are not for scam
    val safeUrls = listOf("https://i.kiwoom.com", "https://me2.kr")
    for (url in safeUrls) {
        if (url in text) {
            return false
        }
    }

    // Checking for suspicious URLs
    val urlPattern = Pattern.compile("(https?|ftp)://(-\\.)?([^\\s/?\\.#-]+\\.?)+(/[^\\s]*)?$")
    if (urlPattern.matcher(text).find()) {
        return true
    }

    // Checking for excess numeric patterns
    val numericPattern = Pattern.compile("\\d{4,}")
    if (numericPattern.matcher(text).find()) {
        return true
    }

    // Check for excess special characters
    val specialCharsPattern = Pattern.compile("[※\\<>@#$%^&*\\(\\)]{3,}")
    if (specialCharsPattern.matcher(text).find()) {
        return true
    }

    return false
}
