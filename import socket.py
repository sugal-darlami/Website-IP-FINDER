import socket
website= input("Enter the website name: ")
ip =socket.gethostbyname(website)
print(ip)