class EmailClient:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def send_email(self, email, content):
        print(f"EMAIL send to {email}")

e1 = EmailClient('rahul.gopi@outlook.com', 'password')

e1.send_email('shinoj.shyane@gmail.com', "Hello how are you ??")