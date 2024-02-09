import logging
import logging.handlers
from .Config import Config

Config = Config()

# Set up logging (in this case to terminal)
log = logging.getLogger(__name__)
log_formatter = logging.Formatter('%(levelname)s %(message)s')
log_handler = logging.StreamHandler()
log_handler.setFormatter(log_formatter)
log.addHandler(log_handler)

if Config.get_log_level() == "DEBUG":
    log.root.setLevel(logging.DEBUG)
elif Config.get_log_level() == "INFO":
    log.root.setLevel(logging.INFO)
else:
    log.root.setLevel(logging.WARNING)
