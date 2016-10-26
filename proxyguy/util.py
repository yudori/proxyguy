import click


protocols = ['http', 'https', 'ftp', 'socks']
env_path = "/etc/environment"
apt_path = "/etc/apt/apt.conf"


def write(ls=None):
    """
    saves profile setting which includes username, password,
    address, port, profile name and list of protocols
    """
    clear_vars()

    if ls is not None:
        try:
            append_vars(ls)

        except KeyError:
            click.echo("Oops! an error occured!")


def append_vars(ls):
    """
    append variables and their values to file
    """

    url_snip = ls['username'] + ":" + ls['password'] + \
        "@" + ls['address'] + ":"+ str(ls['port']) + "/"

    #for environment variables
    val = "http://" + url_snip
    with open(env_path, "a") as f:
        for p in convert_protocol_to_vars():
            line = "{}={}\n".format(p, val)
            f.write(line)
            click.echo("({}) {} --> {}".format(env_path, p, val))

    #for apt variables
    with open(apt_path, "a") as f:
        for p in protocols:
            line = "Acquire::{}::proxy \"{}://{}\";\n".format(p, p, url_snip)
            f.write(line)
            click.echo("({}) --> {}".format(apt_path, line))


def clear_vars():
    """
    deletes all supported proxy environment variables
    """

    #clear environment variables
    for p in convert_protocol_to_vars():
        try:
            with open(env_path, "r") as f :
                lines = f.readlines()
            with open(env_path, "w") as f :
                for line in lines:
                    if p not in line:
                        f.write(line)
        except IOError:
            pass

    #clear apt variables
    for p in protocols:
        try:
            with open(apt_path, "r") as f :
                lines = f.readlines()
            with open(apt_path, "w") as f:
                for line in lines:
                    if p not in line:
                        f.write(line)
        except IOError:
            pass


def convert_protocol_to_vars():
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
