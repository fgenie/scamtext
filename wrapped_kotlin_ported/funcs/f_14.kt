import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    val keywords = arrayOf(
        "실력입증", "추천주", "잠시 시간내서", "지원금받기", "무료교육", "주식상담",
        "광고)", "추.천", "해외선물", "무료거부", "정회원방", "kakaotalk.it", "me2.kr",
        "선입수", "프로모션", "초대합니다", "특별케어", "완성", "체험반", "차별", "체험", "너도나도",
        "로또", "지식교환", "신세계 상품권", "치킨", "커피"
    )

    fun containsKeyword(text: String): Boolean {
        for (word in keywords) {
            if (word in text) {
                return true
            }
        }
        return false
    }

    fun containsUrl(text: String): Boolean {
        val pattern: Pattern = Pattern.compile(
            "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\\\(\\\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        )
        return pattern.matcher(text).find()
    }

    return containsKeyword(message) && containsUrl(message)
}
