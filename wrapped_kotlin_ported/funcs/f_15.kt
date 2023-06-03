fun isSpam(message: String): Boolean {
    val spamKeywords = listOf("신규", "입금", "출금", "증권", "추천주",
                              "혜택", "악성광고", "무료추천", "전달",
                              "종목", "상승", "최소", "특허")
    for (keyword in spamKeywords) {
        if (keyword in message) {
            return true
        }
    }

    val linkPattern = Regex("""(http|https:\/\/|www\.|bit\.ly|me2\.kr|kakao[^ ]*|talk[^ ]*|naver\.me|ko\.gl)[^ ]+""")
    if (linkPattern.containsMatchIn(message)) {
        return true
    }

    val percentPattern = Regex("""\d{1,3}%""")
    if (percentPattern.containsMatchIn(message)) {
        return true
    }

    return false
}
