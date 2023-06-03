def is_spam(message: str) -> bool:
    import re

    # Check if the message contains a URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)

    # Check if message contains non-alphanumeric characters
    non_alpha_pattern = re.compile(r'\W+')
    non_alpha = re.findall(non_alpha_pattern, message.replace(" ", ""))

    # Check if message contains random capitalization
    capitalization_pattern = re.compile(r'([A-Z][a-z]+|[a-z]+[A-Z])+')
    capitalization = re.findall(capitalization_pattern, message)

    # Estimate the length of the message with no spaces
    message_length = len(message.replace(" ", ""))

    # Define thresholds for spam criteria
    threshold_url = 0.15
    threshold_non_alpha = 0.30
    threshold_capitalization = 0.15
    threshold_message_length = 20

    # Calculate proportions of spam features
    if message_length == 0:
        return False
    else:
        url_ratio = len(urls) / message_length
        non_alpha_ratio = len(non_alpha) / message_length
        capitalization_ratio = len(capitalization) / message_length

        # Determine if the message is spam based on the calculated proportions
        if url_ratio > threshold_url or non_alpha_ratio > threshold_non_alpha or capitalization_ratio > threshold_capitalization:
            return True
        elif message_length > threshold_message_length:
            return True
        else:
            return False