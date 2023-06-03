fun isSpam(text: String): Boolean {
    // Check for common spam phrases
    val spamPhrases = listOf<String>(
        "광고", "지원금", "신청", "추천주", "수익률", "무료거부", "지급", 
        "누적수익률", "코드", "원", "비용", "%", "더", "합병", "지금", 
        "개미", "이벤트", "영업일"
    )

    val numSpamPhrases = spamPhrases.filter { phrase -> phrase in text }.count()

    // Check for URLs
    val urlPattern = Regex("(http(s?)://|www.)\S+")
    val urls = urlPattern.findAll(text).toList()
    val textWithoutUrls = urlPattern.replace(text, "")

    // Count digits in the text
    val numDigits = textWithoutUrls.count { it.isDigit() }

    // Check for unusual structure of the text
    val numWordsInTextWithoutUrls = textWithoutUrls.trim().split(' ').count()
    val numWordsInText = text.trim().split(' ').count()
    val propWordsRemovedWithoutUrls = (numWordsInText - numWordsInTextWithoutUrls) / numWordsInText.toDouble()

    return numSpamPhrases >= 3 || numDigits >= 5 && urls.isNotEmpty() || propWordsRemovedWithoutUrls >= 0.5
}
