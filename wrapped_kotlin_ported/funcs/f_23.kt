import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Check for unusual characters and patterns often found in spam
    if (Pattern.compile("[^\\w\\s.!?]").matcher(message).find()) {
        return true
    }

    // Check if the message contains a suspicious URL
    if (Pattern.compile("http(s)?://[^\\s]+").matcher(message).find()) {
        return true
    }

    // Check if the message contains congratulatory phrases often found in spam
    if (Pattern.compile("축하(합니다|드립니다)").matcher(message).find()) {
        return true
    }

    // Check if the message contains secretive phrases often found in spam
    if (Pattern.compile("극비|차별화 된|무료로").matcher(message).find()) {
        return true
    }

    // Check if the message contains financial promises often found in spam
    if (Pattern.compile("수익|올랐다|상한가 확정|최신종목").matcher(message).find()) {
        return true
    }

    // If none of the above conditions are met, it is not spam
    return false
}
