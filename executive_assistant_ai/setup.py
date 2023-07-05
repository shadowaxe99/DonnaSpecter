from setuptools import setup, find_packages

setup(
    name='executive_assistant_ai',
    version='1.0',
    description='A robust and intuitive AI executive scheduling assistant',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/executive_assistant_ai',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'nltk',
        'tensorflow',
        'keras',
        'flask',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'executive_assistant_ai=executive_assistant_ai.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
    ],
)