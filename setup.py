from setuptools import setup

requirements = {
    'install': [
        'distribute',
        ],
    'extras': {
        'docs': [
            'sphinx>=1.1',
            'agoraplex.themes.sphinx>=0.1.2',
            ],
        },
    }

# write requirements for ReadTheDocs...
with open("reqs/rtfd.txt", "w") as rtfd:
    rtfd.write('\n'.join(requirements['extras']['docs']) + '\n')


setup(
    name='agoraplex.platform',
    version='0.0.0',
    author='Tripp Lilley',
    author_email='tripplilley@gmail.com',
    packages=[],
    namespace_packages=[],
    url='https://github.com/agoraplex/platform',
    license='BSD',
    description='Meta-project for Agoraplex platform components.',
    long_description=open('README.rst').read(),
    install_requires=requirements.get('install', None),
    tests_require=requirements.get('extras', {}).get('tests', None),
    extras_require=requirements.get('extras', None),
)
