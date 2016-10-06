

protocols = ['http', 'https', 'ftp', 'socks']
filepath = "/etc/environment"


def write(ls=None):
    """
    saves profile setting which includes username, password,
    address, port, profile name and list of protocols
    """
    clear_vars()
    if ls is not None:
        try:
            s = "http://" + ls['username'] + ":" + ls['password'] + \
                "@" + ls['address'] + ":"+ str(ls['port']) + "/"
            append_vars(s)

        except KeyError:
            print "Oops! an error occured!"


def append_vars(val):
    """
    append variables and their values to file
    """
    f = open(filepath, "a")
    for p in get_vars():
        line = "{}={}\n".format(p, val)
        f.write(line)
        print "{} --> {}".format(p, val)


def clear_vars():
    """
    deletes all supported proxy environment variables
    """
    for p in get_vars():
        try:
            f = open(filepath, "r")
            lines = f.readlines()
            f.close()
            f = open(filepath, "w")
            for line in lines:
                if p not in line:
                    f.write(line)
        except IOError:
            pass
        finally:
            f.close()


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
