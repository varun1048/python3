from  requests import get 

res  = get("http://184.95.52.42/examresults/online/report/onlineResult.jsp")
print(res.text)

# onlineResultInner.jsp registerno &iden=1