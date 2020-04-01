import os
import json
import logging
import logging.handlers as handlers

if not os.path.exists("logs"):
    os.makedirs("logs")

# read the config file 
with open('config.json') as config_file:
    config = json.load(config_file)


level = logging.getLevelName(config["logConfig"]["level"])
logging.basicConfig(
    filename=str(config["logConfig"]["filename"]),
    level=level,
    format=str(config["logConfig"]["format"])
)

logger = logging.getLogger(__name__)
