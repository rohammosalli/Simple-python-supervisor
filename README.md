###### Simple python(mars) supervisor



Run the application

```bash

virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt

python mars.py --process_name nginx --input_command "systemctl start nginx"  --max_fail 3  --check_interval 1 --restart_interval 3

```


the logs are available in this path /logs/mars.logs the application after a run will generate this path 

note: be sure you run the script by a user who has permission to run the command
