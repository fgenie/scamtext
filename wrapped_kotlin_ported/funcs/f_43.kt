import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Rule 1: Check for the presence of special characters or spaces between characters (common in spam messages)
    if (Pattern.compile("\\W").matcher(message).find()) {
        return true
    }

    // Rule 2: Check for non-standard domain names
    val domainRegex: String = "(http|https)://[^\\s/]+"
    val domainMatches: Matcher = Pattern.compile(domainRegex).matcher(message)
    while (domainMatches.find()) {
        val match: String = domainMatches.group()
        if (!match.contains(".") || match.length <= 5) // exclude standard ones
            return true
    }

    // Rule 3: Check for unusual percentage signs
    if (Pattern.compile("[%][^ ][^\\d]").matcher(message).find()) {
        return true
    }

    // Rule 4: Check for the presence of unusual substrings (광고, 보장, 무료, 무료거부, 등록, SMS, 입장, 1000명, 무조건, 매수)
    val spamKeywords = listOf("광고", "보장", "무료", "무료거부", "등록", "SMS", "입장", "1000명", "무조건", "매수")
    for (word in spamKeywords) {
        if (word in message) {
            return true
        }
    }

    return false
}
