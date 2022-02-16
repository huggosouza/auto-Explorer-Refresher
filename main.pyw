import os as os
from datetime import datetime
from time import sleep

# Install dependencies
os.system('pip install psutil')
import psutil

# Iterate over all running processes
while True:
    for proc in psutil.process_iter():
        # Get process detail as dictionary
        pInfoDict = proc.as_dict(attrs=['name', 'memory_percent'])
        if pInfoDict['name'] == "explorer.exe":
            pInfoDict['memory_percent'] = '{0:.1g}'.format(pInfoDict['memory_percent'])
            mPercentValue = int(pInfoDict['memory_percent'])
            if mPercentValue >= 45:
                os.system('taskkill /f /IM explorer.exe')
                print("Explorer killed. Restarting service...")
                os.system('start explorer.exe')
            mPercentValue = str(mPercentValue) + "%"

    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    print("Explorer memory usage:", mPercentValue, "at", time)
    sleep(120)
