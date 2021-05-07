from setuptools import setup

def read(fname):
    with open(fname, 'r') as f:
        return f.read()

setup(name             = 'python-numa',
      description      = 'Python libnuma ctypes wrapper',
      long_description = read('README.md'),
      py_modules       = ['numa'],
      version          = '0.1',
      author           = 'Xiulong Yuan, Zhan Lu, Zheng Zeng',
      author_email     = 'yuanxl19@mails.tsinghua.edu.cn, lu-z18@mails.tsinghua.edu.cn',
      url              = 'https://github.com/eedalong/pynuma',
      license          = 'License :: OSI Approved :: MIT License',
      platforms        = 'Linux',
      classifiers      = [
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python'
          ],
      )