from setuptools import setup

setup(
    name='socompile',
    author="Mara Cielanga Colclough",
    version="0.1",
    packages=["socompile"],
    package_dir={'socompile': 'socompile'},
    entry_points={
        'console_scripts': [
            'socompile = socompile.command:compile',
        ]
    },
    python_requires='>=3.5',
)