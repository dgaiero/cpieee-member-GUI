import secrets
import time

from colorama import Back, Fore, Style

import ldap_connection


class PhoneNumberNotFoundException(Exception):
    def __init__(self, phone_number):
        super().__init__("Phone Number Not Found")
        self.message = "Phone Number Not Found"
        self.phone_number = phone_number


class LoginErrorException(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        self.message = message
        self.errors = error


def bind_user(bind_username, bind_password):
    admin_ldap = ldap_connection.ldapServer(
        secrets.DEFAULT_URI, secrets.SEARCH_BASE, secrets.BIND_USERNAME, secrets.BIND_PASSWORD)
    admin_ldap.bind()
    get_user_data = admin_ldap.search(f"(mobile={bind_username})")
    if len(get_user_data) == 0 or len(get_user_data) > 1:
        admin_ldap.unbind()
        raise PhoneNumberNotFoundException(bind_username)
    user_login_string = get_user_data[0].entry_dn
    admin_ldap.unbind()
    ldap = ldap_connection.ldapServer(secrets.DEFAULT_URI, secrets.SEARCH_BASE, user_login_string, bind_password)
    ldap_bind_result = ldap.bind()
    print(ldap_bind_result)
    if ldap_bind_result is not True: # This is set to != because it will only return true if successful (dictionary if error)
            print(f"{Back.RED}ERROR{Style.RESET_ALL}")
            print("Description: " + ldap_bind_result["description"])
            raise LoginErrorException("Login Not Found", ldap_bind_result)
            # sys.exit()
    return ldap
