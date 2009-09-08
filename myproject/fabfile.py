from fabric.api import run, env, cd, local

def staging():
    env.hosts = ['spectrum.webfactional.com']
    env.user = 'spectrum'
    env.base_dir = '/home/spectrum/webapps/cycleworks/Oktosys-CMS/'
    env.error_log = '/home/spectrum/webapps/cycleworks/apache2/logs/error_log'

def deploy():
    with cd(env.base_dir):
        run('git pull')
        run('touch myproject.wsgi')
        
def errors():
    run('tail %s' % env.error_log)

def install_reqs():
    with cd(env.base_dir):
        run('pip install -r requirements.txt')

def syncdb():
    install_reqs()
    with cd(env.base_dir):
        run('./manage.py syncdb')

def sd():
    "Shorcut for staging deploy"
    staging()
    deploy()    

def psd():
    staging()
    local("git push", capture=False)
    deploy()
