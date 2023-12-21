from setuptools import setup

package_name = 'py_subscriber'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bisalgt',
    maintainer_email='bisalgt@gmail.com',
    description='py_subscriber_description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'listener = py_subscriber.subscriber_member_function:main',
        ],
    },
)
