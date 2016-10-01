import click
import shelve

#create profile
#activate profile
#get current profile
#list profiles
#delete profile

db_file = "db_proxyguy"


@click.group()
def init():
    pass


@click.command()
@click.option('--profile-name', prompt='Profile Name',
              help='The name of the proxy configuration profile')
@click.option('--address', prompt='Proxy Address',
              help='The proxy server address')
@click.option('--port', default=80, prompt='Port Number',
              help='The name of the proxy configuration profile')
@click.option('--username', prompt='Username',
              help='The proxy username')
@click.option('--password', prompt='Password',
              help='The proxy password')
@click.option('--activate', type=click.BOOL, default=False, required=False)
def create_profile(profile_name, address, port, username, password, activate):
    """
    create a network proxy configuration profile
    """
    store = shelve.open(db_file)
    try:
        store[str(profile_name)] = {
            'address' : address,
            'port' : port,
            'username' : username,
            'password' : password
        }

        if activate:
            activate_profile(profile_name)
    finally:
        store.close()
    click.echo("-{}-   -{}-   -{}-   -{}-   -{}-".format(profile_name, address, port, username, password))


@click.command()
@click.argument('profile-name')
def activate_profile(profile_name):
    """
    activate a network proxy configuration profile
    """
    store = shelve.open(db_file);
    try:
        store['active'] = store[str(profile_name)]
    except KeyError:
        click.echo("No such profile '{}'".format(str(profile_name)))
    finally:
        store.close()


@click.command()
def list_profiles():
    """
    lists all stored proxy profiles
    """
    store = shelve.open(db_file)
    try:
        for s in store:
            click.echo(s)
    finally:
        store.close()


init.add_command(create_profile)
init.add_command(activate_profile)
init.add_command(list_profiles)

