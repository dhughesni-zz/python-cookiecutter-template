""" DEV and PRODUCTION config """
import os


def get_config():
    """ get_config returns DEV and else Production config"""
    try:
        if os.getenv("APP_ENV") == "DEV":
            return {
                "EXAMPLE_ID": "EXAMPLE",
            }
        # else return PRODUCTION
        return {
            "EXAMPLE_ID": os.getenv("EXAMPLE_ID"),
        }
    except Exception as exception:
        raise Exception(
            "Unable to get CONFIG:", exception)
