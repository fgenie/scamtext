fun isSpam(message: String): Boolean {

    val spamPhrases = listOf("(광고)", "입니다", "상한가확정", "무료거부", "추천주", "결과값은", "지원받고", "적중", "최소 150%", "수익금",
                    "십만원 만들기", "소액투자", "체험반", "종목도 이어서", "상세주소", "기회를 놓치지", "만원한장 시작",
                    "수익률", "바로 입장", "신한 렌탈")

    val spamRegexPatterns = listOf("\\bhttps?:\\/\\/\\S+".toRegex(), "\\bme2\\.kr\\/\\S+".toRegex(), "\\bopenkakao\\.\\S+".toRegex(), "\\bvvd\\.bz\\/\\S+".toRegex(),
                           "[0-9]+[\\u4e00-\\u9fff]+".toRegex())

    // Check for spam phrases
    for (phrase in spamPhrases) {
        if (phrase in message) {
            return true
        }
    }

    // Check for spam regex patterns
    for (pattern in spamRegexPatterns) {
        if (pattern.containsMatchIn(message)) {
            return true
        }
    }

    return false
}
