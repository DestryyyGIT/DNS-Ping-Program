## Program for taking list of DNS names and automatically pinging them to obtain their IPs

import socket, os

def processOutputFile(addresses): # writes the IP addresses to the text file
    addr = open("addresses.txt", "w")
    addr.write('\n'.join(addresses))
    
    return

def processInputFile(): # strip DNS names into a list
    names = []
    
    f = open('names.txt','r')
    names = [line.strip() for line in open('names.txt')]
    f.close()

    #print(len(names))
    return names

def main():
    names = processInputFile()
    addresses = []
    
    length = len(names)
    
    for i in range(length): # pings the DNS names and returns "" for unresolved hosts
        try:   
            addresses.append(socket.gethostbyname(names[i]))
        except socket.gaierror:
            addresses.append("")
    
    #print(addresses)   
    result = processOutputFile(addresses)
    os.startfile('addresses.txt')
    
if __name__ == '__main__':
    print("Grabbing IP addresses...")
    main()
