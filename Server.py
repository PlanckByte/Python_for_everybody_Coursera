import socket
import time 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
total_data = 0 
picture_bytes = b''

while True:
    data = mysock.recv(5120)
    if (len(data)<1):
        break
    time.sleep(0.25)
    total_data = total_data + len(data)
    print(len(data), total_data)
    picture_bytes = picture_bytes + data
mysock.close()
#look for the end of Header
pos=picture_bytes.find(b'\r\n\r\n')
print('Header Length',pos) #prints bytes of headers
print(picture_bytes[:pos].decode()) #prints headers up until but not including the two blank lines
picture_bytes=picture_bytes[pos+4:] #now the picture bytes are the bytes after the header
fhand=open('image.jpg','wb') #open file in writing binary mode hence "wb"
fhand.write(picture_bytes)
fhand.close()
