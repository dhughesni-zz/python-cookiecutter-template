
from config import get_config
from log import get_log

# get + set app config
CONFIG = get_config()

# set log
LOG = get_log(__name__)

if __name__ == "__main__":
    LOG.info("App Running")
