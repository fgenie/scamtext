fun isSpam(message: String): Boolean {
    // Words/phrases commonly found in spam messages
    val spamWords = listOf("↑", "무료거부", "멤버십", "무료체험", "https://me2.kr", "비밀번호", "수익", "상승", "룰렛", "무료강의", "예약")

    // Check if any of the spam words/phrases are in the input message
    for (word in spamWords) {
        if (message.contains(word)) {
            return true
        }
    }

    // Check if the message contains "광고" at the beginning
    if (message.startsWith("(광고)") || message.startsWith("* (광고)")) {
        return true
    }

    // Check if the message contains excessive line breaks
    if (message.count { it == '\n' } >= 3) {
        return true
    }

    return false
}
