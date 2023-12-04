import socket
import pickle
from _thread import *
from Player import player

server = "192.168.1.6"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players=[player(0,0,70,50,(255,0,0)),player(500,500,50,70,(0,0,255))]

def threaded_client( conn , addr , player ):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print(addr," have been disconnected")
                break
            else:
                if player==1:
                    reply=players[0]
                else:
                    reply=players[1]
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer=0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,addr,currentPlayer ))
    currentPlayer += 1