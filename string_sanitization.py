def sanitize_phrase(phrase: str):
    phrase = phrase.lower()
    sanitized = []
    for char in phrase:
        if char.isalpha() or char == " ":
            sanitized.append(char)
    return "".join(sanitized)
