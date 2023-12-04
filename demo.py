def emailProcess(email):
    #youtube@gmail.com
    email_UserName = email[0:email.index("@")]
    email_Domain = email[email.index("@")+1:]
    return [email_UserName, email_Domain]

def printMsg(email_UserName, email_Domain):
    # ghi ra username và emaildomain
    print(f"User Name is {email_UserName};Email domain is {email_Domain}")

def main():
    # nhập email
    email = input('Please enter your email: ').strip()
    username, domain = emailProcess(email)
    printMsg(username, domain)
    
if __name__ =="__main__":
    main()
     