fun isSpam(message: String): Boolean {
    val spamKeywords = arrayOf("광고", "축하드립니다", "선물", "무료", "입장", "수익", "하루에", "체험반", "카톡", "수익률",
            "추천", "대출", "거래", "상승장", "만족", "프로젝트", "최고급", "종목", "증가", "VIP", "만원",
            "방", "공개", "적중", "익절", "기회", "적발", "공시", "현금", "적립", "수수료", "신용")

    val messageWords = message.split(" ")

    for (word in messageWords) {
        if (word in spamKeywords) {
            return true
        }
    }
    return false
}
