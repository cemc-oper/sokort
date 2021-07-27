import os

# dummy for testing. Don't use this in production!
c.JupyterHub.authenticator_class = 'firstuseauthenticator.FirstUseAuthenticator'
# c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

# launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = 'graphics-hub-server'


# Explicitly set notebook directory because we'll be mounting a host volume to
# it.  Most jupyter/docker-stacks *-notebook images run the Notebook server as
# user `jovyan`, and set the notebook directory to `/home/jovyan/work`.
# We follow the same convention.
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
c.DockerSpawner.volumes = {
    'jupyterhub-user-{username}': notebook_dir,
    "/home/wangdp/project/graphics/operation/system": {
        "bind": "/srv/system",
        "mode": "ro",
    },
    "/sstorage1": {
        "bind": "/sstorage1",
        "mode": "ro",
    }
}

c.Authenticator.admin_users = {"windroc"}



# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
c.DockerSpawner.image = 'nwpc-oper/graphics-notebook'

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'jupyterhub'

# delete containers when the stop
c.DockerSpawner.remove = True

c.Spawner.default_url = '/lab'