import socket
text = """HTTP/1.1 200 OK\r
Connection:close\r 
Content—Type:text/html\r
\r
\r 
<!DOCTYPE html>\r
<html lang="ja">\r
<head>\r
<meta charset="UTF-8">\r
<title>第4回目 Webデザイン</title>\r
</head>\r
<body>\r
<h1>カレーライスのレシピ</h1>\r
</body>\r
</html>\r
"""
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("start server")
s.bind(('', 5555))
s.listen(10)
c, addr = s.accept()
print("connect")
data = c.recv(1024)
c.send(bytes(text, "utf-8"))
s.close()
