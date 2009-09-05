from fabric.api import run, env

def staging():
    env.hosts = ['spectrum.webfactional.com']
    env.user = 'spectrum'

def deploy():
    run('cd /home/spectrum/webapps/cycleworks/Oktosys-CMS;git fetch;git rebase origin')
    run('touch /home/spectrum/webapps/cycleworks/myproject.wsgi')
