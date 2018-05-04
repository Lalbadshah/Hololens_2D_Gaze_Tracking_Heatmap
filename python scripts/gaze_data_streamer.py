import zmq_receiver,zmq,json,msvcrt
from network import UDPSender

''' Init Sender and Receiver '''
# streamer = UDPSender('127.0.0.1',5500)
Heatmap_pyt_streamer = UDPSender('127.0.0.1',5501)
print ('gaze streaming initialised!')

ctx = zmq.Context()

req = zmq_receiver.init_requester(ctx,50020)

''' Send & Get Loop '''
while True :

    ''' Subscribe latest data '''
    g_sub = zmq_receiver.create_subscriber(ctx,req,u'gaze')

    ''' Get Data '''
    g_data = zmq_receiver.get_data(g_sub)

    ''' Extract data '''
    norm_pos = g_data['norm_pos']
    eye_id = g_data['base_data'][0]['id']
    if len(g_data['base_data']) > 1 :
        eye_id = 2

    ''' Filter Data '''
    if g_data['confidence'] > 0.6 :

        ''' Send Data '''
        # streamer.send('%s,%s,%s'%(str(norm_pos[0]),str(norm_pos[1]),eye_id))
        Heatmap_pyt_streamer.send('%s,%s,%s'%(str(norm_pos[0]),str(norm_pos[1]),eye_id))

        ''' Press Space = Print data '''
        if msvcrt.kbhit():
            if ord(msvcrt.getch()) == 32:
                print 'g',g_data['norm_pos'],g_data['timestamp'],g_data['confidence'],len(g_data['base_data']),g_data['base_data'][0]['id']
