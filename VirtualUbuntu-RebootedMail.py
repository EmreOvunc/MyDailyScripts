import os

# Emre Ovunc
# info@emreovunc.com

def reboot_func():
    receiver_mail = " info@emreovunc.com"
    mail_data= "mail -s "Virtual Ubuntu Rebooted!" + receiver_mail
    content = "\n[!!!] Virtual Ubuntu rebooted ! \'"
    rebooted = content + mail_data
    os.system(str(rebooted))

reboot_func()

