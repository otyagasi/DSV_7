import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5555))
s.listen(10)
data = input("メッセージ: ")
sizer_text = ""
for i in range(len(data)):
    if data[i].isalpha():
        sizer_text += chr(ord(data[i])+3)
    else:
        sizer_text += data[i]
print("server: ", sizer_text)
s.close()

