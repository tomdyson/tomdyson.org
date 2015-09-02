from fabric.api import local

def build():
    local("python manage.py staticsitegen")

def upload():
    "uploads new / modified files and purges the Cloudfront cache for them"
    local("s3cmd --cf-invalidate --verbose sync _build/ s3://tomdyson.org/")

def deploy():
    build()
    upload()
