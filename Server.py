from socket import *
serverport = 5678
serversocket = socket(AF_INET, SOCK_DGRAM)
serversocket.bind(('', serverport))
print("The server is listening...")
while True:
    message, clientaddress = serversocket.recvfrom(2048)
    message_str = message.decode()
    char_count = len(message_str)
    response_message = f"Number of characters: {char_count}\nUppercase message: {message_str.upper()}"
    serversocket.sendto(response_message.encode(), clientaddress)
