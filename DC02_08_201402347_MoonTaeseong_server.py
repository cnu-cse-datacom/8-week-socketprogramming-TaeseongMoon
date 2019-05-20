import socket

IP = "127.0.0.1"
PORT = 8080

class ServerSocket():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((IP, PORT))

    def receive(self):
        fileName, addr = self.socket.recvfrom(1024)
        print("file recv start from ", addr[0])
        print(fileName)
        fileName = fileName.decode()
        print("File Name ", fileName)
        fileSize = self.socket.recvfrom(1024)
        fileSize = int(fileSize[0])
        print("File Size:",fileSize)
        
        data, addr = self.socket.recvfrom(1024)
        data_transferred = 0
        with open("copy"+fileName, 'wb') as f:
            try:
                while data:
                    f.write(data)
                    data_transferred += len(data)
                    print("current_size / total_size = %s/%s, %f%%" %(data_transferred,fileSize, data_transferred/fileSize*100))  
                    if data_transferred/fileSize*100 >= 100:
                        break
                    data, addr = self.socket.recvfrom(1024)
            except:
                print("filed transfer")
        print("file received")
        self.socket.close()

    def main(self):
        self.receive()

if __name__ == '__main__':

    server_socket = ServerSocket()
    server_socket.main()

