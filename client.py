import socket
import os
from os.path import exists

IP = '127.0.0.1'
PORT = 8080

class ClientSocket():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def fileSend(self):
        fileName = input("Input your file name : ")
    
        self.socket.sendto(fileName.encode(), (IP, PORT))
        if not exists(fileName):
            return 
        fileSize = os.path.getsize(fileName)
        self.socket.sendto(str(fileSize).encode(), (IP, PORT))
        
        data_transferred = 0
        print("File Transmit Start.....")
        with open(fileName, 'rb') as f:
            try:
                data = f.read(1024)
                while data:
                    data_transferred += self.socket.sendto(data, (IP,PORT))
                    data = f.read(1024)
                    print("current_size / total_size = %s/%s, %f%%" %(data_transferred, fileSize, data_transferred/fileSize*100))  
            except:
                print("failed transfer")
        
        print("ok")
        print("file_send_end")
        self.socket.close()

    def main(self):
        self.fileSend()

if __name__ == '__main__':

    client_socket = ClientSocket()
    client_socket.main()

