
import re

def is_spam(message: str) -> bool:
    # Look for common spam indicators such as excessive use of special characters, repetitions, and scrambled text
    special_chars_pattern = r"[^a-zA-Z0-9\s]+"
    repetitions_pattern = r"(\w)\1{2,}"
    scrambled_pattern = r"[A-Za-z]{1}[0-9]{1}[A-Za-z]{1}[0-9]{1}"
    
    special_chars_ratio = len(re.findall(special_chars_pattern, message)) / len(message)
    repetitions_count = len(re.findall(repetitions_pattern, message))
    scrambled_count = len(re.findall(scrambled_pattern, message))
    
    # Define thresholds to classify a message as spam
    special_chars_threshold = 0.3
    repetitions_threshold = 5
    scrambled_threshold = 3
    
    # Check if any of the thresholds are exceeded
    if (special_chars_ratio > special_chars_threshold or
        repetitions_count > repetitions_threshold or
        scrambled_count > scrambled_threshold):
        return True
    else:
        return False
