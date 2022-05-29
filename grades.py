def grade_rate():
    grade = float(input())
    text = ''
    if 5.50 <= grade <= 6.00:
        text = "Excellent"
    elif 4.50 <= grade <= 5.49:
        text = "Very Good"
    elif 3.50 <= grade <= 4.49:
        text = "Good"
    elif 3.00 <= grade <= 3.49:
        text = "Poor"
    else:
        text = "Fail"
    print(text)


grade_rate()
