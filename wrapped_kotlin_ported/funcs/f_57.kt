fun isSpam(message: String): Boolean {
    val patterns = listOf(
        Regex("""(?i)\b(추천|상승|단기간|익절|무료교육|달성|거래량|폭등)\b"""), // 유형 1,2,4에서 발견됩니다.
        Regex("""(?i)\b(http|bit\.ly|t\.ly|me2\.kr|dokdo\.in|buly\.kr)\b"""), // 유형 1,2,3,4,5에서 발견됩니다.
        Regex("""(?i)\b(입금|출금)\b"""), // 일부 스팸 메시지에서 발견됩니다.
        Regex("""(%|상한가|모션|목표)\b"""), // 일부 스팸 메시지에서 발견됩니다.
        Regex("""(?i)\b(광고)\b""") // 스팸 메시지에서 때때로 발견됩니다.
    )

    patterns.forEach { pattern ->
        if (pattern.containsMatchIn(message)) {
            return true
        }
    }

    return false
}
