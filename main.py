from dispatchees.send_sms import SendSMS

conv = SendSMS()
status = conv.send("+17404173920","Hello Ian!")
print(status)