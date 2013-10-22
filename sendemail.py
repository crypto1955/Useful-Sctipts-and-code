import smtplib

server = 'smtp.sendgrid.net'
user = 'syncNscan'
password = 'pass@word2'

recipients = ['sbpraveen34@iitj.ac.in','sbpraveen34@gmail.com']
sender = 'sbpraveen34@iitj.ac.in'
message = 'Hello World'

session = smtplib.SMTP(server,port=587)
# if your SMTP server doesn't need authentications,
# you don't need the following line:
print session.login(user, password)
print "login success"
print session.sendmail(sender, recipients, message)