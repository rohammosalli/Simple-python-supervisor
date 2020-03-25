import psutil
import subprocess
import os
import time
import schedule
import daemon
import args

#pas the arguments 
process_name = args.process_name
max_fail = args.max_fail
restart_interval = args.restart_interval
input_command = args.input_command
check_interval =args.check_interval
CUNT = 0 

daemon.logging.getLogger('schedule').propagate = False

daemon.logger.info("######## Logs ######## \n \
    \trestart_interval = %s, \n \
    \tmax_fail = %s , \n \
    \tprocess_name = %s , \n \
    \tcheck_interval = %s , \n \
    \tinput_command = %s \n ",
    restart_interval, max_fail, process_name, check_interval, input_command )



def life_check():
    global CUNT

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
if checkIfProcessRunning(process_name):
    daemon.logger.info("  %s process is running",process_name)
    print("  {0} process is running".format(process_name))
else:
    CUNT = CUNT + 1
    if CUNT >= int(max_fail):
        daemon.logger.error("  max number of retires reached, unable to start")
        print("program unable to start")
        exit()
        time.sleep(int(restart_interval))    
    else:
        print('No {0} process is running'.format(process_name))
        try:
            print('The {0} process is running now'.format(process_name))
            subprocess.call([input_command])
            
        except OSError:
            print (input_command,' this command  does not exist')
            daemon.logger.error("this command {0} does not exist".format(input_command))
            exit()


schedule.every(int(check_interval)).seconds.do(life_check)

while 1:
    schedule.run_pending()
    time.sleep(1)