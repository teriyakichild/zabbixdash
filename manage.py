from tornado import template
import pdb
import ConfigParser
from os import path, walk, makedirs
from sys import stdout, argv

class Manage(object):
    def __init__(self, verbose=False):
        self._Config = ConfigParser.ConfigParser()
        self._Config.read('plugin.conf')
        if self._Config.has_section('options'):
            self.options = dict(self._Config.items('options'))
            self.options.update(dict(self._Config.items('internal')))
        else:
            stdout.write('Unable to read config file (plugin.conf)\n')
            exit(2)
        self.skel_dir = '{0}/skel'.format(path.dirname(path.realpath(__file__)))
        self.loader = template.Loader(self.skel_dir)
        self.verbose = verbose
        if self.verbose:
            stdout.write('loading directory and file list..' + '\n')
        self.directories, self.files = self._load_dirs_files()

    def load_template(self, filename):
        ret = self.loader.load(filename).generate(
            **self.options
        )
        return ret

    def _load_dirs_files(self):
        ret = {'dirs': [], 'files': {}}
        for root, dirs, files in walk(self.skel_dir, topdown=False):
            # Let's use the relative path
            pieces = root.split('/')
            skel_pos = (pieces.index('skel') + 1)
            end_pos = (len(pieces) - 1)
            filepathlist = []
            while skel_pos <= end_pos:
                filepathlist.append(pieces[skel_pos])
                skel_pos += 1
            filepath = '/'.join(filepathlist)
            # Time to load the files
            for filename in files:
                filepath_real = path.join(filepath, filename)
                if self.verbose:
                    stdout.write('Found {0}\n'.format(filepath_real))
                ret['files'][filepath_real] = self.load_template(filepath_real)
            # Time to load the dirs
            for dirname in dirs:
                directory = path.join(filepath, dirname)
                if self.verbose:
                    stdout.write('Found {0}\n'.format(directory))
                ret['dirs'].append(directory)
        return (ret['dirs'], ret['files'])

    def create_dirs(self, prefix=None):
        #self.directories.append(prefix)
        for directory in self.directories:
            if prefix is not None:
                directory_real = path.join(prefix, directory)
            else:
                directory_real = directory
            if not path.exists(directory_real):
                if self.verbose:
                    stdout.write('Creating {0}\n'.format(directory_real))
                makedirs(directory_real)

    def write_files(self, prefix=None):
        self.create_dirs(prefix)
        for filename, content in self.files.items():
            if prefix is not None:
                filename_real = path.join(prefix, filename.replace('.tpl',''))
            else:
                filename_real = filename.replace('.tpl','')
            f = open(filename_real, 'w+')
            if self.verbose:
                stdout.write('Writing {0}\n'.format(filename_real))
            f.write(content)
            f.close()


if __name__ == '__main__':
    verbose = False
    if '--verbose' in argv or '-v' in argv:
        verbose=True
    manage = Manage(verbose=verbose)
    if 'install' in argv:
        manage.write_files('backup')
        manage.write_files()
    elif 'list' in argv:
        stdout.write('Directories:\n')
        for directory in manage.directories:
            stdout.write(directory + '\n')
        stdout.write('Files:\n')
        for filename in manage.files:
            stdout.write(filename + '\n')
