def timeConversion(s):
    """Convert 12-hour hh:mm:ssAM/PM to 24-hour hh:mm:ss."""
    hour = int(s[:2]) % 12          # 12 -> 0, so 12AM = 00 and 12PM = 12 after the shift below
    if s[-2:] == "PM":
        hour += 12
    return f"{hour:02d}{s[2:8]}"


if __name__ == "__main__":
    print(timeConversion(input().strip()))
