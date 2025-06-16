import socket
import datetime
now =str(datetime.datetime.now())
# サーバーソケットを作成
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5555))
s.listen(10)
data = input("メッセージ:")
print("server: ", now)
s.close()

