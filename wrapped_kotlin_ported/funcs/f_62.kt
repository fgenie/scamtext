
fun isSpam(message: String): Boolean {
    val spamKeywords = listOf("광고", "무료", "배달", "상한가", "수익", "프로모션", "추천", "적중", "할인", "선착순", "차익", "소득", "개설", "열립니다", "안내입", "공유", "입장", "연락", "투자", "공개론")
    val messageClean = message.replace(Regex("[^가-힣0-9\\s]"),"")
    val messageLower = messageClean.toLowerCase()
    val messageWords = messageLower.split("\\s+".toRegex())
    for (keyword in spamKeywords) {
        if (messageWords.contains(keyword)) {
            return true
        }
    }
    val links = Regex("(https?://\\S+)").findAll(message)
    val linkCount = links.count()
    if (linkCount > 1) {
        return true
    }
    if (Regex("(\\d)\\1{2,}").containsMatchIn(message)) {
        return true
    }
    return false
}

