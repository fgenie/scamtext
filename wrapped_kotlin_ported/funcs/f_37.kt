
import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Check for common spam phrases and patterns
    val spamPhrases = arrayOf(
        "특별", "상승", "배당", "파이널", "금일", "최대", "무료", "VIP", "차별화", "종목", "시작", "추천주", "단독입수", "단타", "매매", "건설", "수익", "어째", "정보",
        "관심종목", "참고로", "희망", "여행관련주", "가상화폐", "털보임",
        "정상적인 문자형식",
        "교수의", "국제유가",
        "원칙입니다.",
        "도운",
        "한농화성",
        "여행주가",
    )

    // Check for URL shortening services
    val urlShorteners = arrayOf(
        "https://tuney.kr", "http://bit.ly", "https://me2.kr", "https://vvd.bz", "https://bit.ly", "https://ls38.xyz", "https://0xf.kr", "https://tr.im"
    )

    // Check for excessive special characters
    val specialCharPattern = Pattern.compile("[!@#$%^&*()-_=+\\[\\]{}\\/?.,;:]+")

    if (spamPhrases.any { it in message }) {
        return true
    }
    if (urlShorteners.any { it in message }) {
        return true
    }
    if (specialCharPattern.matcher(message).find() && specialCharPattern.matcher(message).groupCount() > 4) {
        return true
    }

    return false
}

