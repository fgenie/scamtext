fun isSpam(text: String): Boolean {

    val spamPatterns = arrayOf(
            // URL shorteners and patterns associated with scam websites
            "(http|https)://(bit\\.ly|me2\\.kr|buly\\.kr)[^\\s]*".toRegex(),

            // Numbers and special characters repeated in sequence
            "\\d{2,}%?[↑↓]".toRegex(),

            // Unusual amount of special characters (e.g. parentheses & brackets)
            "[(){}<>]{3,}".toRegex(),

            // Unusual phrases commonly found in spam messages
            "(슈퍼개미|선물|수익|감사합니다|카카오톡|모집|축하|교육|영업점|오픈초대|폭등|다음주도 이어서|상승)".toRegex(),

            // Repeated exclamation marks or question marks
            "[!?]{2,}".toRegex(),

            // Words with an excessive amount of capital letters
            "[A-Z\\s]{4,}".toRegex(),

            // Pattern of time or percentage followed by an unusual word or character
            "(\\d[해선]%|\\d+[시\\s]*간?|\\d+[\\s-]*월)[^가-힣]+".toRegex(),

            // Repeated phrases or words
            "(\\b\\w+\\b)\\W+\\1".toRegex())

    for (pattern in spamPatterns) {
        if (pattern.containsMatchIn(text)) {
            return true
        }
    }

    return false
}
