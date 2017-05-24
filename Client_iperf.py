#!/usr/bin/env python3

import iperf3
import time
global packet_lost
packet_lost="old"

def collect_info(Host):
        client = iperf3.Client()
            
        client.duration=2
        client.server_hostname =Host
        client.port = 5201
        client.protocol = 'udp'
        
          
        print('Connecting to {0}:{1}'.format(client.server_hostname, client.port))
        result = client.run()
        

        
       
        if result.error:
             print(result.error)
        else:   
                packet_lost=result.lost_percent
                print(packet_lost)
                print('')
                print('Test completed:')
                print('  started at         {0}'.format(result.time))
                print('  bytes transmitted  {0}'.format(result.bytes))
                print('  seconds         {0}'.format(result.seconds))
                print('  jitter (ms)        {0}'.format(result.jitter_ms))
                print('  packet_lost (ms)        {0}'.format(result.lost_percent))
                print('  avg cpu load       {0}%\n'.format(result.local_cpu_total))

                print('Average transmitted data in all sorts of networky formats:')
                print('  bits per second      (bps)   {0}'.format(result.bps))
                print('  Kilobits per second  (kbps)  {0}'.format(result.kbps))
                print('  Megabits per second  (Mbps)  {0}'.format(result.Mbps))
                print('  KiloBytes per second (kB/s)  {0}'.format(result.kB_s))
                print('  MegaBytes per second (MB/s)  {0}'.format(result.MB_s))
            
        return result.lost_percent,result.kB_s,result.jitter_ms

'''
    Simple socket server using threads
'''
def norm(Result):
    if(len(Result)<6):
        Result=Result+"0"
        Result=norm(Result)
    return Result
 
import socket
import sys
 
HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8081# Arbitrary non-privileged port
while 1:        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print( 'Socket created') 
        #Bind socket to local host and port
        try:
            s.bind((HOST, PORT))
        except socket.error as msg:
            print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()
            
        print ('Socket bind complete')
        
        #Start listening on socket
        s.listen(10)
        print ('Socket now listening')

        #now keep talking with the client

        conn, addr = s.accept()
        print ('Connected with ' + addr[0] + ':' + str(addr[1]))

'''
        packet_lost,debit,jitter=collect_info(addr[0])
        packet_lost=norm(str(packet_lost)[:6])
        debit=norm(str(debit)[:6])
        jitter=norm(str(jitter)[:6])
        print(packet_lost)
        print(debit)
        print(jitter)
        
        print(len("packet_lost : "+packet_lost+"\nDebit : "+str(debit)))

        conn.send(("packet_lost : "+packet_lost+"\nDebit : "+str(debit)).encode('utf-8'))
       '''
        conn.send(("ffffffffffffffffffffffffffffffffffffffffffffffffffffff").encode('utf-8'))

        s.close()


