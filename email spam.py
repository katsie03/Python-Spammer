import smtplib
import random


fromaddress = input("Please type in the adress you want to send the email from")
toaddress = input("To the adress of your reciptent who you want to email")


username = "yourusername"
password = "yourpassword"



message = input("Please enter your message") 



server =smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

spam = input("How many times do you want to send the message?")
for i in range(0, int(spam)):
 server.sendmail(fromaddress,toaddress,message)
 print("Your e-mail has sent")
 print("© 2018")

server.quit()

exit()
