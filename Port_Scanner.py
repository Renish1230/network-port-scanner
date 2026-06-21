
import socket,time

COMMON={21:'FTP',22:'SSH',25:'SMTP',53:'DNS',80:'HTTP',443:'HTTPS'}

target=input("Host/IP: ")
start=int(input("Start Port: "))
end=int(input("End Port: "))

ip=socket.gethostbyname(target)
print(f"Resolved IP: {ip}")

open_ports=[]
start_time=time.time()

for port in range(start,end+1):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.3)
    result=s.connect_ex((ip,port))
    s.close()

    if result==0:
        service=COMMON.get(port,"Unknown")
        open_ports.append((port,service))
        print(f"OPEN: {port} ({service})")

print("\nSummary")
print("-"*30)
print("Open Ports:",len(open_ports))
print("Duration:",round(time.time()-start_time,2),"seconds")
