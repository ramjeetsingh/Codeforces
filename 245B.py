s = input()

protocol = ""
if s[0:4] == "http":
    protocol = "http"
    s = s[4:]
else:
    protocol = "ftp"
    s = s[3:]

domain = ""
for i in range(0,len(s)-1):
    if s[i:i+2] == "ru":
        if i == 0:
            continue
        else:
            domain = s[0:i]
            s = s[i:]
            break

context = ""
if s != "ru":
    context = "/" + s[2:]

print(protocol + "://" + domain + ".ru" + context)