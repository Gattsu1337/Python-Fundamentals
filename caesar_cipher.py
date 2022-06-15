def encrypt(txt):
    encrypted_txt = ''.join([chr(ord(x) + 3) for x in txt])
    print(encrypted_txt)

txt = input()
encrypt(txt)
