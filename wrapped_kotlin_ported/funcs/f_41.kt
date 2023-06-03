import java.util.regex.Pattern
 
fun isSpam(message: String): Boolean {
    // Check for common spam characteristics
    val urlRegex: Pattern = Pattern.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\\\(\\\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    val moneyRegex: Pattern = Pattern.compile("[\\d,]+원")
    val percentRegex: Pattern = Pattern.compile("\\d+%")
 
    // Check if message contains URL
    if (urlRegex.matcher(message).find()) {
        return true
    }
 
    // Check if message contains money or percentage expressions
    if (moneyRegex.matcher(message).find() || percentRegex.matcher(message).find()) {
        return true
    }
 
    // Check for suspicious leading/trailing whitespace
    if (message.trim() != message) {
        return true
    }
 
    // If none of the above checks have been met, consider the message as normal (non-spam)
    return false
}
