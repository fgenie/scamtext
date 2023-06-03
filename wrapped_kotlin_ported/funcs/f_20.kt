import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Check for common spam indicators
    val spamIndicators = arrayOf(
        "(광고)",  // 광고 keyword
        "(추천종목)",  // 추천종목 keyword
        "\\bh.t.t.p.s?:\\/\\/\\S*",  // shortened urls
        "([A-Za-z0-9]{3,}(\\.[A-Za-z0-9]{2,})+)\\/?[A-Za-z0-9]*\\b",  // urls with no http(s)
        "▒+",  // multiple consecutive square characters
        "♥+",  // multiple consecutive heart characters
        "▲+",  // multiple consecutive triangle characters
        "※",  // reference mark character
        "(.{2,40}\\s?\\|)",  // '|' character within 40 characters from start of the line
        "[0-9]{2,}[,.\s]*[0-9]{4,}",  // numbers separated by comma or space
        "월공개",
        "무료.+거부"  // 무료 followed later by 거부
    )

    // Check the presence of each of the above spam-related patterns
    for (indicator in spamIndicators) {
        if (Pattern.compile(indicator).matcher(message).find()) {
            return true
        }
    }

    // If none of the above patterns are found, the message is not spam
    return false
}
