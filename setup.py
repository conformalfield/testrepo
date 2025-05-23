from setuptools import setup, find_packages

setup(
    name='testrepo',  # Replace with your project's name
    version='0.1.0',
    description='A sample repository demonstrating standard project structure.',
    author='The Project Contributors', # Replace with your name or organization
    author_email='contact@example.com', # Replace with your contact email
    url='https://github.com/yourusername/testrepo', # Replace with your project's URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
