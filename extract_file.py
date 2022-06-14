def extract_file(location):
    needed_info = location[-1].split('.')
    file = needed_info[0]
    extension = needed_info[1]
    print(f"File name: {file}")
    print(f"File extension: {extension}")


location = input().split("\\")
extract_file(location)
