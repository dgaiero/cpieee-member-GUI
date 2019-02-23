import ldap3
from colorama import Back, Fore, Style

class ldapServer:
    def __init__(self, server_uri, search_base, bind_user, bind_password):
        '''
        Initalize the class with necessary server bind parameters.
        '''
        self.server_uri = server_uri
        self.search_base = search_base
        self.bind_user = bind_user
        self.bind_password = bind_password

    def bind(self):
        print(
            f"{Back.YELLOW}{Fore.BLACK}Connecting to server ({self.bind_user})...{Style.RESET_ALL}")
        server = ldap3.Server(
            self.server_uri, get_info=ldap3.ALL, connect_timeout=4200)
        self.ldap_connection = ldap3.Connection(
            server, self.bind_user, self.bind_password)
        self.ldap_connection.start_tls()
        if not self.ldap_connection.bind():
            return(self.ldap_connection.result)

        return True

    def rebind(self, *args, **kwargs):
        return self.ldap_connection.rebind(*args, **kwargs)

    def unbind(self):
        self.ldap_connection.unbind()

    def search(self, search_query):
        self.ldap_connection.search(self.search_base, search_query, attributes=[
                                    "displayName", "member", "mail", "ieeeMemberNumber"], size_limit=1000)
        users_in_search = self.ldap_connection.entries
        return users_in_search
