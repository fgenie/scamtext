import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Check for common spam phrases, words and symbols
    val spamPhrases = arrayOf(
        "\\b(무료|체험|vip|상승|성공|수익률|추천|주식|사람들|정보)\\b",
        "\\b(회사|공시|종목|증권|반도체|제약|오후|분석|4월|3주차|최소)\\b",
        "\\b(여의도|수익|멤버|직장인|투자|장기프로그램|마감)\\b",
        "\\b(턴어라운드|매력적|인공지능|빅데이터|가상화폐|투기성|타점|분석)\\b",
        "\\b(ur|https?|www\\.|http[\\w=&#?,.:-]+|me2|opcn|a.to)\\b",
        "\\b(_percent_|[_\\-.]{2,})"
    )
    
    // Combine spam phrases and words with 'or' clause
    val spamPattern = spamPhrases.joinToString(separator = "|")
    val pattern = Pattern.compile(spamPattern, Pattern.CASE_INSENSITIVE)

    // Check if the message matches the spam pattern
    val matcher = pattern.matcher(message)
    return matcher.find()
}
