from datetime import datetime
import time

from GraphQuerier import GraphQuerier
from LEDPanel import LEDPanel

LEDPanel = LEDPanel()

def isWorkHours():
    now = datetime.now()
    today = datetime.today()

    return (now.hour > 7 and now.hour < 18 and today.weekday() < 5)

def setPresenceStatus(status):
    setPresenceStatus.status_color = {"Availible": "green",
                                      "Away": "yellow",
                                      "Busy": "red",
                                      "OutOfOffice": "purple"}
    LEDPanel.setColor(setPresenceStatus.update[status])

if __name__=="__main__":
    conn = GraphQuerier()
    while True:
        print('get Status at {}'.format(time.strftime("%H:%M:%S GMT",time.gmtime())))
        if isWorkHours():
            status = conn.getTeamsStatus()
        else:
            status = "OutOfOffice"
        
        setPresenceStatus(status)
        time.sleep(60 - time.time() % 60)