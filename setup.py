import os
from pip.req import parse_requirements
from setuptools import setup
from sys import path

from zabbixdash import __version__ as VERSION


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

try:
    # parse_requirements() returns generator of pip.req.InstallRequirement objects
    reqs = [str(ir.req) for ir in parse_requirements(
        os.path.join(os.path.dirname(__file__), 'requirements.txt'))]
except:
    # Same as above but handle newer version of pip
    reqs = [str(ir.req) for ir in parse_requirements(
        os.path.join(os.path.dirname(__file__), 'requirements.txt'), session='')]

path.insert(0, '.')

NAME = "zabbixdash"


def gen_data_files(base_target, *dirs):
    results = []
    for src_dir in dirs:
        for root, dirs, files in os.walk(src_dir):
            if not files:
                continue
            clean_root = root.replace(src_dir + '/', '')
            target_root = os.path.join(base_target, clean_root)
            results.append((target_root, map(lambda f: root + "/" + f, files)))
    return results

TEMPLATES = gen_data_files('/usr/share/', NAME + '/templates')
STATIC = gen_data_files('/usr/share/', NAME + '/static')
DB = gen_data_files('/var/lib/', NAME + '/data')
CONFIG_FILES = [('/etc', ['myui.conf'])]

if __name__ == "__main__":

    setup(
        name=NAME,
        version=VERSION,
        description="description",
        long_description=read('README.md'),
        author="Tony Rogers",
        author_email="tony.rogers@rackspace.com",
        url="https://github.com/teriyakichild/zabbixdash",
        license='internal use',
        packages=[NAME, NAME + '.controllers'],
        package_dir={NAME: NAME},
        include_package_data=True,

        data_files=TEMPLATES + STATIC + DB + CONFIG_FILES,

        install_requires=reqs,
    )
