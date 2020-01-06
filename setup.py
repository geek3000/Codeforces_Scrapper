from setuptools import setup, find_packages

setup(
    name='codeforces_scrapper_geek',
    version='0.1',
    description='A GUI to get user info by yandle',
    url='https://github.com/geek3000/Codeforces_Scrapper',
    author='geek123',
    author_email='jonathantchuente@gmail.com',
    license='MIT',
    install_requires=['requests', 'PIL'],
    packages=find_packages(),
    entry_points=dict(
        gui_scripts=['codeforces_scrapper_geek=codeforces_scrapper_geek.main']
    )
)
