import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Check for typical spam keywords/phrases
    val keywords = listOf("추천", "입장", "알려드린", "참여", "상승", "적중", "상한가", "투자", "만들기", "마지막안내", "오픈합니다", "다음주", "계약", "이벤트", "광고")
    
    for (keyword in keywords) {
        if (message.contains(keyword)) {
            return true
        }
    }
    
    // Check for multiple consecutive special characters (excluding Korean)
    if (Pattern.compile("[^\\w\\sㄱ-ㅣ가-힣]+[^\\w\\sㄱ-ㅣ가-힣]+").matcher(message).find()) {
        return true
    }
    
    // Check for excessive capitalization
    val uppercaseCount = message.count { it.isUpperCase() }
    if (uppercaseCount > message.length / 2) {
        return true
    }
    
    // Check for links with suspicious domains
    val spamDomains = listOf("me2.kr", "han.gl", "ko.gl", "vvd.bz")
    for (domain in spamDomains) {
        if (message.contains(domain)) {
            return true
        }
    }

    return false
}
