from datetime import datetime
import time

from GraphQuerier import GraphQuerier
from LEDPanel import LEDPanel

def isWorkHours():
    now = datetime.now()
    today = datetime.today()

    return (now.hour > 7 and now.hour < 18 and today.weekday() < 5)

def setPresenceStatus(status):
    setPresenceStatus.update = {"away": print}
    setPresenceStatus.update[status](f"Matt is currently away.")

if __name__=="__main__":
    conn = GraphQuerier()
    while True:
        print('get Status at {}'.format(time.strftime("%H:%M:%S GMT",time.gmtime())))
        if isWorkHours():
            status = conn.getTeamsStatus()
        else:
            status = "away"
        
        setPresenceStatus(status)
        time.sleep(60 - time.time() % 60)