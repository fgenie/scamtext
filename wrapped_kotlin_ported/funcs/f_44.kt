fun isSpam(message: String): Boolean {
    val spamPatterns = listOf(
            "입장번호",
            "투자",
            "상한가",
            "수익",
            "추천",
            "광고",
            "계좌",
            "축하",
            "공개",
            "선물",
            "쿠폰",
            "오픈",
            "무료거부",
            "https?:\\/\\/",
            "주식",
            "투자반",
            "%"
    )

    for (pattern in spamPatterns) {
        if (Regex(pattern).containsMatchIn(message)) {
            return true
        }
    }

    return false
}
