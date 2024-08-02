import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'tb3'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
  	    (os.path.join('share', package_name,'meshes'), glob('meshes/*')),
  	    (os.path.join('share', package_name,'worlds'), glob('worlds/*')),
  	    (os.path.join('share', package_name,'models/tb3_model'), glob('models/tb3_model/*')),
  	    (os.path.join('share', package_name,'urdf'), glob('urdf/*')),
  	    (os.path.join('share', package_name), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gabriel',
    maintainer_email='gabriel@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'scan_map=tb3.scan_subscriber:main',
        ],
    },
)
