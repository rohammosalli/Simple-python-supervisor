import psutil
import subprocess
import os
import time
import schedule
import daemon
import args
import sys
#pas the arguments 
process_name = args.process_name
max_fail = args.max_fail
restart_interval = args.restart_interval
input_command = args.input_command
check_interval =args.check_interval


CUNT = 0 
timer = 0

daemon.logger.info("######## Logs ######## \n \
    \trestart_interval = %s, \n \
    \tmax_fail = %s , \n \
    \tprocess_name = %s , \n \
    \tcheck_interval = %s , \n \
    \tinput_command = %s \n ",
    restart_interval, max_fail, process_name, check_interval, input_command )




def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


# Check if any  process was running or not. then run it


def startpc():
    global CUNT
    if checkIfProcessRunning(process_name) is False:
        daemon.logger.info("  %s process is not run try to run",process_name)
        os.system(input_command)
        CUNT = CUNT + 1    
        if CUNT >= int(max_fail):
            daemon.logger.error("max number of retires reached")
            exit()
        time.sleep(int(restart_interval))
    else:
        daemon.logger.debug("is running with pid: %s", process_name)
        CUNT = 0
         


schedule.every(int(restart_interval)).seconds.do(startpc)

while 1:
    schedule.run_pending()
    time.sleep(1)