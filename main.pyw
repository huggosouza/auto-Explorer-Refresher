import os as os
from datetime import datetime
from time import sleep

# Install dependencies
os.system('pip install psutil')
import psutil

while True:
    # Iterate over all running processes
    for proc in psutil.process_iter():
        # Get process detail as dictionary
        pInfoDict = proc.as_dict(attrs=['name', 'memory_percent'])
        
        # Get the 'explorer.exe' memory usage percent
        if pInfoDict['name'] == "explorer.exe":
            pInfoDict['memory_percent'] = '{0:.1g}'.format(pInfoDict['memory_percent'])
            
            # Save the memory percent value
            mPercentValue = int(pInfoDict['memory_percent'])
            # Kill the process and start it again if memory percent >= 45
            if mPercentValue >= 45:
                os.system('taskkill /f /IM explorer.exe')
                print("Explorer killed. Restarting service...")
                os.system('start explorer.exe')
            mPercentValue = str(mPercentValue) + "%"
    # Just shows the time, for better visualization when on terminal (Useless on daily use)
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    print("Explorer memory usage:", mPercentValue, "at", time)
    # Sleep for 2 minutes before running again
    sleep(120)
