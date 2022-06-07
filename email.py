class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    information = input().split("")
    if information[0] == "Stop":
        break
    receiver = information[0]
    sender = information[1]
    content = information[2]
    email = Email(sender, receiver, content)
    emails.append(email)

sent_emails = [emails[int(x)].send for x in input().split(", ")]

for item in emails:
    print(item.get_info())
