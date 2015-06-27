# -*-coding:utf-8-*-


import os
from setuptools import setup


def get_static_files(root):
    return [os.path.join(path, name)
            for path, subdirs, files in os.walk(root)
            for name in files]
package_data = sum(map(get_static_files,
                       ["luiti/java/",
                        "luiti/webui/assets/",
                        "luiti/webui/bower_components/",
                        ]), [])
package_data += ["luiti/webui/index.html"]


setup(
    name='luiti',
    version='0.1.5',
    url='http://github.com/17zuoye/luiti/',
    license='MIT',
    author='David Chen',
    author_email=''.join(reversed("moc.liamg@emojvm")),
    description='Luiti = Luigi + time',
    long_description=open("README.markdown").read(),
    packages=[
                'luiti',
                'luiti/daemon',
                'luiti/daemon/ptm',
                'luiti/luigi_decorators',
                'luiti/luigi_extensions',
                'luiti/manager',
                'luiti/task_templates/',
                'luiti/task_templates/time',
                'luiti/task_templates/other',
                'luiti/utils', ],
    scripts=[
        'bin/luiti',
    ],

    package_data={'luiti': package_data},
    include_package_data=True,

    zip_safe=False,
    platforms='any',
    install_requires=[
        # 1. luigi related
        "luigi         == 1.1.2",
        "snakebite     ~= 2.5",
        "protobuf      ~= 2.6",
        "tornado       ~= 4.0",
        "mechanize     ~= 0.2",
        "python-daemon ~= 1.6",
        "MySQL-python  ~= 1.2",
        "pymongo       ~= 2.7",

        # 2. luiti self
        "etl_utils     ~= 0.1",
        "arrow         ~= 0.4",
        "inflector     ~= 2.0",
        "pygments      ~=2.0",
        "ujson",
        "jsonpickle",
        "six",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
