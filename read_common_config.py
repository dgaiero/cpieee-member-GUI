import configparser
import appdirs
import os
import pathlib

app_name = "cpieee_ldap_utilities"
app_author = "Cal Poly IEEE Student Branch"

user_config_dir = appdirs.user_config_dir(app_name, app_author)
site_config_dir = appdirs.site_config_dir(app_name, app_author)
user_log_dir = appdirs.user_log_dir(app_name, app_author)

user_config_file_location = pathlib.Path(user_config_dir,"config.ini")
site_config_file_location = pathlib.Path(site_config_dir, "config.ini")

class CommonConfig:

    def __init__(self):
        if user_config_file_location.is_file():
            raise NotImplementedError
        elif site_config_file_location.is_file():
            raise NotImplementedError
        else:
            raise NoConfigFoundError
        # raise NotImplementedError


class NoConfigFoundError(Exception):
    pass
