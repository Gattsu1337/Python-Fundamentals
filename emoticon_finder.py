def emotion_finder(text):
    emotions = [text[x] + text[x + 1] for x in range(len(text)) if text[x] == ':' and text[x + 1] != ' ']
    print('\n'.join(emotions))

text = input()
emotion_finder(text)