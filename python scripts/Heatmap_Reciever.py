from network import UDPReciever
from network import TCPSocket
import threading
import heatmapBackend_generator
import math


USock = UDPReciever('127.0.0.1',5501)
# TSock = TCPSocket('127.0.0.1',5502)

# data
#
# def UDPRecieveWorker():
#     while True:
#
#         data = USock.recv(1024)
#         data = data.split(',')
#         x=float(data[0])
#         y=float(data[1])
#         data[2]=int(data[2])
#         x = x * 1280
#         y = y * 720
#
#         if(x>1280):
#             x=1280
#         if(x<0):
#             x=0
#         if(y<0):
#             y=0
#         if(y>720):
#             y=720
#
#     return
#
# threads = []
# t = threading.Thread(target=UDPRecieveWorker)
# threads.append(t)
# t.start()
SuperList=[]
SendCount=0
while True:

    SendCount+=1;
    if(SendCount==10):
        heatmapBackend_generator.heatmapper(SuperList)
        SuperList=[]
        SendCount=1
    data = USock.recv(1024)
    data = data.split(',')
    x=float(data[0])
    y=float(data[1])
    data[2]=int(data[2])
    x = math.floor(x * 1280)
    y = math.floor(y * 720)

    if(x>1280):
        x=1280
    if(x<0):
        x=0
    if(y<0):
        y=0
    if(y>720):
        y=720
    SuperList.append((int(x),int(y)))
