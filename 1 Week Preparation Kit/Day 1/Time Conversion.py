def timeConversion(s):
    if s[-2:] == "PM":
        if s[:2] == '12':
            return s[:-2]
        else:
            return str(int(s[:2]) + 12) + s[2:-2]
    if s[-2:] == "AM":
        if s[:2] == '12':
            return str(int(s[:2]) - 12)+'0' + s[2:-2]
        else:
            return s[:-2]


if __name__ == '__main__':
    result = timeConversion("08:45:54PM")
    print(result)
