import time

from GraphQuerier import GraphQuerier
from LEDPanel import LEDPanel

if __name__=="__main__":
    print('get connection')
    conn = GraphQuerier()
    while True:
        print('get Status at {}'.format(time.strftime("%H:%M:%S GMT",time.gmtime())))
        conn.getTeamsStatus()
        print('Convert status to lights')
        print('update lights')
        time.sleep(60 - time.time() % 60)