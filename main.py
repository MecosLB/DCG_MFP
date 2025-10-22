#!/usr/bin/env python
"""Scrapes a specific cardset from the official Digimon Card Game website.

"""

import yaml
from modules.watcher import Watcher
from modules.validator import Validator
from modules.uploader import Uploader
from modules.processor import Processor

__author__ = "Sebastian Rangel D Rugama"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastian Rangel D Rugama"
__email__ = "sebokiabot@gmail.com"
__status__ = "Development"
    
# Main method
if __name__ == "__main__":
    # Opens the config.yaml file to set all the config values in our Uploader instance. 
    with open('config.yaml') as file:
        config = yaml.safe_load(file)
        
    validator = Validator(16)
    uploader = Uploader(config['snowflake']['connection'], config['snowflake']['table'])
    processor = Processor(validator, uploader, 'processed', 'error')
    watcher = Watcher('dropzone', processor)
    
    watcher.start()