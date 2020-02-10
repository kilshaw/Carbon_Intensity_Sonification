import urllib.request
import json
import socket
import time
region_number = 15
HOST = "127.0.0.1"
PORTA = 6255
PORTB = 6256
PORTC = 6257
PORTD = 6258
PORTE = 6259
PORTF = 6260
PORTG = 6261
PORTH = 6262
PORTI = 6263
PORTJ = 6264
PORTK = 6265
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
def shoot():
    
    contents = urllib.request.urlopen("https://api.carbonintensity.org.uk/regional").read()
    varab = json.loads(contents)
   
    ##print(contents)
    
    print(varab['data'][0]['regions'][region_number]['shortname'])
    name = (varab['data'][0]['regions'][region_number]['shortname'])
    print(varab['data'][0]['regions'][region_number]['generationmix'][0]['perc'])
    biomass = varab['data'][0]['regions'][region_number]['generationmix'][0]['perc']
    print(varab['data'][0]['regions'][region_number]['generationmix'][1]['perc'])
    coal = varab['data'][0]['regions'][region_number]['generationmix'][1]['perc']
    print(varab['data'][0]['regions'][region_number]['generationmix'][2]['perc'])
    imports = varab['data'][0]['regions'][region_number]['generationmix'][2]['perc']
    print(varab['data'][0]['regions'][region_number]['generationmix'][3]['perc'])
    gas = varab['data'][0]['regions'][region_number]['generationmix'][3]['perc']
    print(varab['data'][0]['regions'][region_number]['generationmix'][4]['perc'])
    nuclear = varab['data'][0]['regions'][region_number]['generationmix'][4]['perc']
    print(varab['data'][0]['regions'][region_number]['generationmix'][5]['perc'])
    other = varab['data'][0]['regions'][region_number]['generationmix'][5]['perc']
    print(varab['data'][0]['regions'][region_number]['generationmix'][6]['perc'])
    hydro = varab['data'][0]['regions'][region_number]['generationmix'][6]['perc']
    print(varab['data'][0]['regions'][region_number]['generationmix'][7]['perc'])
    solar = varab['data'][0]['regions'][region_number]['generationmix'][7]['perc']
    print(varab['data'][0]['regions'][region_number]['generationmix'][8]['perc'])
    wind = varab['data'][0]['regions'][region_number]['generationmix'][8]['perc']
    print(varab['data'][0]['regions'][region_number]['intensity']['forecast'])
    intensity = varab['data'][0]['regions'][region_number]['intensity']['forecast']
    print(varab['data'][0]['regions'][region_number])
          
    s.sendto(str(biomass).encode('utf-8'),(HOST,PORTA))
    s.sendto(str(coal).encode('utf-8'),(HOST,PORTB))
    s.sendto(str(imports).encode('utf-8'),(HOST,PORTC))
    s.sendto(str(gas).encode('utf-8'),(HOST,PORTD))
    s.sendto(str(nuclear).encode('utf-8'),(HOST,PORTE))
    s.sendto(str(other).encode('utf-8'),(HOST,PORTF))
    s.sendto(str(hydro).encode('utf-8'),(HOST,PORTG))
    s.sendto(str(solar).encode('utf-8'),(HOST,PORTH))
    s.sendto(str(wind).encode('utf-8'),(HOST,PORTI))
    s.sendto(str(name).encode('utf-8'),(HOST,PORTJ))
    s.sendto(str(intensity).encode('utf-8'),(HOST,PORTK))
    return
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
###########
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
     print (data.decode('utf-8'))
     if data.decode('utf-8') == "d":
            region_number = 1
            shoot()
     if data.decode('utf-8') == "e":
            region_number = 2
            shoot()
     if data.decode('utf-8') == "f":
            region_number = 3
            shoot()
     if data.decode('utf-8') == "g":
            region_number = 4
            shoot()
     if data.decode('utf-8') == "h":
            region_number = 5
            shoot()
     if data.decode('utf-8') == "i":
            region_number = 6
            shoot()
     if data.decode('utf-8') == "j":
            region_number = 7
            shoot()
     if data.decode('utf-8') == "k":
            region_number = 8
            shoot()
     if data.decode('utf-8') == "l":
            region_number = 9
            shoot()
     if data.decode('utf-8') == "m":
            region_number = 10
            shoot()
     if data.decode('utf-8') == "n":
            region_number = 11
            shoot()
     if data.decode('utf-8') == "o":
            region_number = 12
            shoot()
     if data.decode('utf-8') == "p":
            region_number = 13
            shoot()
     if data.decode('utf-8') == "q":
            region_number = 14
            shoot()
     if data.decode('utf-8') == "r":
            region_number = 15
            shoot()
     if data.decode('utf-8') == "s":
            region_number = 16
            shoot()
     if data.decode('utf-8') == "t":
            region_number = 17
            shoot()
     
    
        
           

    
