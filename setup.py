
import os
from setuptools import setup

if os.getenv("ROS_VERSION", default=1) == '2':
    from setuptools import find_packages
    package_name = 'geneus'

    setup(
        name=package_name,
        version='0.0.0',
        packages=find_packages(where='src', exclude=['test']),
        package_dir={'': 'src'},
        data_files=[
            ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
            ('share/' + package_name, ['package.xml']),
        ],
        install_requires=['setuptools'],
        zip_safe=True,
        maintainer=['Kei Okada', 'Yoshiki Obinata'],
        maintainer_email=['k-okada@jsk.t.u-tokyo.ac.jp', 'obinata@jsk.imi.i.u-tokyo.ac.jp'],
        description='EusLisp ROS message and service typesupport library for ROS 2',
        license='BSD',
        extras_require={
            'test': [
                'pytest',
            ],
        },
        entry_points={
            'console_scripts': [
            ],
        },
    )

else:
    from catkin_pkg.python_setup import generate_distutils_setup

    d = generate_distutils_setup(
        packages=['geneus'],
        package_dir={'': 'src'},
        requires=['genmsg']
    )

    setup(**d)
