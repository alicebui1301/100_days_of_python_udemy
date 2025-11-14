import smtplib
import datetime as dt
import random

my_email = "thuuyen.tcl@gmail.com"
my_password = "my_password_here"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:  # Monday
    with open("intermediate/32_send_email/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)

    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                        to_addrs=my_email, 
                        msg=f"Subject:Monday Motivation\n\n{random_quote}")