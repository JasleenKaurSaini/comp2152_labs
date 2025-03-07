import platform
import socket
import os

print(f"Machine Type: {platform.machine()}\n")
print(f"CPU Architecture: {platform.architecture()}\n")

socket.setdefaulttimeout(50)
print(f"Current default Socket time out: {socket.getdefaulttimeout()}\n")

print(f"OS Type: {os.name}\n")
print(f"OS name: {platform.system()}\n")
print(f"Current PID: {os.getpaid()}\n")

file_name = "fdpractice.txt"
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"[PID: {os.getpaid()}] Opened the file_handle: {file_handle}\n")

file_object_TextID = os.fdopen(file_handle, "w+") 
file_object_TextID.write("Some string to write to the file")
file_object_TextID.flush()

print(f"\n\n[PID: {os.getpaid()}] Forking now...\n")
pid = os.fork()
# pid = 0

if pid == 0:
    print(f"[Child PID: {os.getpaid()}], [Parent PID: {os.getppid()}]\n")
else: