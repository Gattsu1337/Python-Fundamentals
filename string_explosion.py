def explosion(text):
    power = 0
    result = ''
    for current_ch in range(len(text)):
        if text[current_ch] != '>' and power > 0:
            power -= 1
        elif text[current_ch] == '>':
            power += int(text[current_ch+1])
            result += text[current_ch]
        else:
            result += text[current_ch]

    print(result)


text = input()
explosion(text)
