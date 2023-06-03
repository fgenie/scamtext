import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    val spamPatterns = arrayOf(
        "\\d{1,2}월\\d{1,2}일",
        "\\d{1,2}%↑",
        "https?://[\\w./]+",
        "[\\w.]+@[a-zA-Z0-9]+",
        "실력으로 보여드립니다",
        "무료거부\\s*0?80",
        "목표가(:\\s*|\\s+)[\\d]+",
        "상한가",
        "\\d{1,2}년 연혁",
        "금.{0,2}칙",
        "체험반",
        "참여",
        "상한가",
        "비밀번호",
        "\\d{1,2}배 이상",
        "\\d{7,15}",
        "me2\\.kr",
        "opcn\\-kakao\\.com",
        "무료로 <<\"2주일내에\" >>",
        "\\s+\\+\\s*한정\\s*",
        "\\%(?=\\s*이상|↓)",
        "\\d{1,2}월\\d{1,2}일",
        "\\d{1,4}%이상",
        "상위\\s*\\d{1,4}%",
        "대충\\s*\\d{1,4}%",
        "\\+상한가"
    )
    for (pattern in spamPatterns) {
        if (Pattern.compile(pattern).matcher(message).find()) {
            return true
        }
    }
    return false
}

