import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Patterns to detect spam
    val urlPattern: Pattern = Pattern.compile("https?://\\S+|www\\.\\S+") // URLs
    val numPattern: Pattern = Pattern.compile("\\d{4,}") // Large numbers (4 or more digits)
    val specialCharPattern: Pattern = Pattern.compile("[!\"#\$%&'()*+,-./[\\\\\\]^_`{|}~]") // Special characters

    // Filters to identify spam
    val hasUrl: Boolean = urlPattern.matcher(message).find()
    val hasLongNum: Boolean = numPattern.matcher(message).find()
    val hasSpecialChars: Boolean = specialCharPattern.matcher(message).find()

    // If the message contains URLs, large numbers or special chars, classify it as spam
    return hasUrl || hasLongNum || hasSpecialChars
}
