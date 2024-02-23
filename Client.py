from socket import *
servername = "127.0.0.1"
serverport = 5678
clientsocket = socket(AF_INET, SOCK_DGRAM)
message = "Anushika Chauhan (2210994763)"
clientsocket.sendto(message.encode(), (servername, serverport))
serverReply, serveraddress = clientsocket.recvfrom(2048)
char_count, received_message = serverReply.decode().split("\n")
print("Received Message:", received_message)
print("Number of Characters:", char_count.split(":")[1].strip())
clientsocket.close()
