from demo import emailProcess, printMsg

def main():
    lstemail = ['hu123@gmail.com', 'ga3###232@gmail.com']
    for email in lstemail:
        Email_UserName, Email_Domain = emailProcess(email)
        printMsg(Email_UserName, Email_Domain)

if __name__ =="__main__":
    main()
