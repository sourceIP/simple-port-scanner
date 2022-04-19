import cowsay
import socket, subprocess, sys
from datetime import datetime

# Blank your screen
subprocess.call('clear', shell=True)

ascii_banner = print(cowsay.get_output_string('trex', 'Simple Port Scanner'))
print(ascii_banner)

startTime = datetime.now()


target = input("Input Host to scan: ")

t_IP  = socket.gethostbyname(target)




print("_" * 60 + '\n')
print("Please wait, engaging scanner on host: ", t_IP)
print("_" * 60 + '\n')



try:


    for port in range (1, 500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((t_IP, port))
        ps = len(str(port))
        if result == 0:
            print ("Port" + ((" "*(5-ps)) +  "{}:   Open".format(port)))
            s.close()
    endTime = datetime.now()

    print('\n' + 'Scan Complete' + '\n')
    print("Total Scan Duration: " + str(endTime - startTime))
    

except KeyboardInterrupt:
        print("\n Ctrl+C Entered, Exiting Program")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved")
        sys.exit()
except socket.error:
        print("\ Target not responding")
        sys.exit()