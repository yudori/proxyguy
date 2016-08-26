import os
import shelve


protocols = ['http', 'https', 'ftp', 'socks']


class Profile:

    def __init__(self, profile_name, address, port, username, password,
                 allowed_protocols=protocols):
        self._profile_name = profile_name
        self._address = address
        self._port = port
        self._username = username
        self._password = password
        self._allowed_protocols = allowed_protocols

    def activate(self):
        """
        saves profile setting which includes username, password,
        address, port, profile name and list of protocols
        :return:
        """
        clear_vars()
        s = "http://" + self._username + ":" + self._password + \
            "@" + self._address + ":"+ self._port + "/"

        for p in get_vars_from_protocols(self._allowed_protocols):
            os.environ[p] = s


def clear_vars():
    """
    deletes all supported proxy environment variables
    :return:
    """
    for p in get_vars_from_protocols(protocols):
        del os.environ[p]


def get_vars_from_protocols(protocols):
    """
    converts a list of protocol names to its environment variable list
    equivalent if the names are valid protocol names. This is done by
    appending '_proxy' and converting the resulting string to both
    lower and upper case variables. This is necessary to account for
    systems that access them using one over the other.
    :param protocols: iterable list of protocols
    :return: list of environment variable equivalent
    """
    ps = []
    for protocol in protocols:
        p_name = protocol + "_proxy"
        ps.append(p_name.lower())
        ps.append(p_name.upper())
    return ps
