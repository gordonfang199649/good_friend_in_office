def is_substring_ignore_cases(substring: str, string: str) -> bool:
    if substring.lower() in string.lower():
        return True

    if substring.upper() in string.upper():
        return True

    return False

def calculate_track_duration(millisecond):
    pass
