
import telnetlib
import time
login = ""
print("Подключаюсь к 192.168.1.201")
telnet = telnetlib.Telnet("192.168.1.201")
login += str(telnet.read_until(b'Username:'))
#print(login)
telnet.write(b'root\n')
login += str(telnet.read_until(b'Password:'))
#print(login)
telnet.write(b',kby4brb154560+\n')
login += str(telnet.read_until(b'#'))
#print(login[-2])
if "#" in login:
    print("Connect is Ok")

telnet.write(b'show clock\n')
time.sleep(1)
print(telnet.read_very_eager().decode('ascii'))
telnet.close()