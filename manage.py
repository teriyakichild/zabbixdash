from tornado import template
import pdb
from os import path, walk, makedirs

this_dir = path.dirname(path.realpath(__file__))
skel_dir = '{0}/skel'.format(this_dir)
loader = template.Loader(skel_dir)
plugin_name = 'exampleplugin'

templates = {}
for root, dirs, files in walk(skel_dir, topdown=False):
    for filename in files:
        pieces = root.split('/')
        skel_pos = (pieces.index('skel') + 1)
        end_pos = (len(pieces) - 1)
        filepath = []
        while skel_pos <= end_pos:
            filepath.append(pieces[skel_pos])
            skel_pos += 1

        templates[path.join('/'.join(filepath), filename.replace('.tpl',''))] = loader.load(
            path.join('/'.join(filepath), filename)
        ).generate(
            plugin_name=plugin_name,
            app_title='Example Plugin',
            cookie_secret='this is the secert, broskis',
            github_username='teriyakichild',
            github_email='tony.rogers@rackspace.com',
            github_name='Tony Rogers',
            description='description',
            block_head_end='{% block head %}{% end %}',
            current_user='{{ current_user }}',
            link_name='<a href="{{ link }}">{{ name }}</a>',
            VERSION='{{ VERSION }}', 
            ifcurrent_user='{% if current_user is None %}',
            end='{% end %}',
            block_nav='{% block nav %}',
            block_body='{% block body %}',
            for_name='{% for name, link in nav_links %}',
            block_head='{% block head %}',
            block_title='{% block title %}',
            block_sidebar='{% block sidebar %}',
            else_v='{% else %}',
            error='{{ error }}',
            if_error='{% if error %}',
            extends_base='{% extends "base.html" %}',
            block_title_login='{% block title %} | Login{% end %}',
            title='Example Plugin - {{ title }}{% block title %}{% end %}'
        )
    for dirname in dirs:
        directory = path.join('/'.join(filepath), dirname)
        if not path.exists(directory):
            print 'Creating {0}'.format(dirname)
            makedirs(directory)


for filename, content in templates.items():
    f = open(filename, 'w+')
    print 'Writing {0}'.format(filename)
    f.write(content)


