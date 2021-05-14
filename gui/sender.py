from smtplib import*

def send(**inner):
    smt = SMTP("smtp.gmail.com",587)
    smt.starttls()
    smt.login("mk.varun2002@gmail.com","bponykwcjkpxhics")

    msg="Subject :"+inner['subject']+"\n"+inner['message']

    out = (smt.sendmail(inner['fromE'],
        inner['toE'],msg))
    
    smt.quit()
    if out:
        return "problem" 
    else:
        return "DONE"
    


# data=dict(fromE="mk.varun2002@gmail.com",
#     toE="mk.varun420@gmail.com",
#     subject="kalai",
#     message="message")
# print(send(**data))


