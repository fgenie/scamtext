fun isSpam(message: String): Boolean {
    // Check for common spam words and phrases
    val spamWords = listOf("추천주", "체험", "공시발표", "목표달성", "수익", "투자", "증권", "정보방", "국내식약처", "안정적인 수익", "클릭", "금전요구", "상한가", "연매출", "매출", "무료거부", "총 수익", "위험", "특집", "국내", "상품안내", "알려드린", "출신")

    for (word in spamWords) {
        val pattern = Pattern.compile(word)
        if (pattern.matcher(message).find()) {
            return true
        }
    }

    // Check for shortened URLs and suspicious links
    val urlRegex = "(?P<url>https?://\\S*.[\\w]*(?=\\s|\\b))".toRegex()
    val urls = urlRegex.findAll(message).map { it.value }.toList()
    val spamUrls = listOf("me2.kr", "bit.ly", "dokdo.in")
    urls.forEach { url ->
        spamUrls.forEach { spamUrl ->
            if (url.contains(spamUrl)) {
                return true
            }
        }
    }

    // Check for unusual numbers by looking for consecutive digits or percentage signs
    val numbersRegex = "\\d{2,}|%".toRegex()
    val numbers = numbersRegex.findAll(message).map { it.value }.toList()
    if (numbers.isNotEmpty()) {
        return true
    }

    return false
}
