import os
import shelve


protocols = ['http', 'https', 'ftp', 'socks']


def activate(ls):
    """
    saves profile setting which includes username, password,
    address, port, profile name and list of protocols
    :return:
    """
    clear_vars()
    s = "http://" + ls['username'] + ":" + ls['password'] + \
        "@" + ls['address'] + ":"+ str(ls['port']) + "/"

    for p in get_vars():
        print "{} --> {}".format(p, s)
        os.environ[p] = s


def clear_vars():
    """
    deletes all supported proxy environment variables
    :return:
    """
    for p in get_vars():
        try:
            del os.environ[p]
        except KeyError:
            pass


def get_vars():
    """
    converts a list of protocol names to its environment variable list
    equivalent.
    :return: list of environment variables
    """
    ps = []
    for protocol in protocols:
        p_name = protocol + "_proxy"
        ps.append(p_name.lower())
        ps.append(p_name.upper())
    return ps
