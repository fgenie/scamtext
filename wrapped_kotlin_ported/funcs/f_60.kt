fun isSpam(message: String): Boolean {
    val moneyKeywords = arrayOf("원", "수익", "이익", "상승", "월공개", "현황", "롤", "지원금", "현황", "추천주", "대박", "지갑", "출금", "추천", "경제", "경제야", "하락", "주식", "주가", "수익률", "분기", "최근", "금전요구", "매매", "최고의", "장점", "event", "code", "일물천금", "%", "회원가입", "광고", "연이은", "숫자를", "총 수익", "▼", "▲", "(광고)", "오키")
    val urlPattern = Pattern.compile("https?://\\S+|www\\.\\S+")
    val repeatedPattern = Pattern.compile("(\\b\\w+\\b)(.*\\1){3,}.*")

    if (message.length > 100) {
        return true
    }

    if (repeatedPattern.matcher(message).matches()) {
        return true
    }

    if (moneyKeywords.any { message.contains(it) }) {
        return true
    }

    if (urlPattern.matcher(message).find()) {
        return true
    }

    return false
}
