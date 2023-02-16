import smtplib


class SendMessage:
    def __init__(self, name, their_email, message):
        self.contact_info = f" {name}/ {their_email}/ {message}"
        self.to_email = 'libre.urea@gmail.com'
        self.from_email = "libre.urea@hotmail.com"
        self.password = "1234best"

    def contactme(self):
        with smtplib.SMTP("smtp.office365.com") as connection:
            connection.starttls()
            connection.login(user=self.from_email, password=self.password)
            connection.sendmail(from_addr=self.from_email,
                                to_addrs=self.to_email,
                                msg=f"Subject:Hello\n\n{self.contact_info}")
