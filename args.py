import argparse 
import daemon



### This file is reponsible for arguments and also  parameter validation



#to have parameter I used argparse
ARG_PARSER = argparse.ArgumentParser()
ARG_PARSER.add_argument(
    '--restart_interval',
    help="Seconds wait between attempts to restart service",
    required=False)
ARG_PARSER.add_argument(
    '--max_fail',
    help="Number of attempts",
    required=False)
ARG_PARSER.add_argument(
    '--process_name',
    help="Name of the process",
    required=False)
ARG_PARSER.add_argument(
    '--check_interval',
    help="Check interval in seconds",
    required=False)
ARG_PARSER.add_argument(
    '--input_command',
    help="Command to start the process",
    required=False)

ARGUMENTS = ARG_PARSER.parse_args()

restart_interval = ARGUMENTS.restart_interval
max_fail = ARGUMENTS.max_fail
process_name = ARGUMENTS.process_name
check_interval = ARGUMENTS.check_interval
input_command = ARGUMENTS.input_command




if process_name is None:
    process_name = input("Name of the process: ")
    
if input_command is None:
    input_command = input("command to start the process: ")    

if check_interval is None:
    check_interval = input(" check interval in seconds: ")

if max_fail is None:
    max_fail = input("Number of attempts: ")
   
if restart_interval is None:
    restart_interval = input("Seconds wait between attempts to restart service: ")




# parameter validation
if not restart_interval.isdigit() or int(restart_interval) < 0:
    print("restart_interval must be a positive number")
    daemon.logger.error("restart_interval must be a positive number")
    exit()

if not max_fail.isdigit() or int(max_fail) < 0:
    print("max_fail must be a positive number")
    daemon.logger.error("max_fail must be a positive number")
    exit()

if not check_interval.isdigit() or int(check_interval) < 0:
    print("check_interval must be a positive number")
    daemon.logger.error("check_interval must be a positive number")
    exit()