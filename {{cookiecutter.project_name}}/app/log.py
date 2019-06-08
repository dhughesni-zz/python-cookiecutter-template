""" Base Logger implementation """
import logging


def get_log(name):
    """ Base Logger Configuration """
    try:
        log = logging.getLogger(name)
        logging.basicConfig(
            format="%(asctime)s %(levelname)s [%(name)s]: %(message)s",
            level=logging.INFO,
        )
        return log
    except Exception as exception:
        raise Exception("Unable to initialise LOG:", exception)
