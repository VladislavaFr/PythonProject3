class SMSSender():
    def send_sms(self, message):
        print("Send: ", message)

class PushSender():
    def send_push(self, message):
        print("Send: ", message)

class MailSender():
    def send_mail(self, message):
        print("Send: ", message)

class SuperSender(SMSSender, PushSender, MailSender):
    def send_all(self, message):
        self.send_sms(message)
        self.send_push(message)
        self.send_mail(message)

sender = SuperSender()
sender.send_all("text message")

