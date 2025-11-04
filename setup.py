
from setuptools import setup, find_packages
setup(
    name='medical_chatbot',
    version='1.0.0',
    author='Harsh Navin',
    author_email="hnpk802313@gmail.com",
    packages=find_packages(),
    install_requires=[
        'langchain==0.3.26',
        'flask==3.1.1',
        'sentence-transformers==4.1.0',
        'pypdf==5.6.1',
        'langchain-pinecone==0.2.8',
        'langchain-openai==0.3.24',
        'langchain-community==0.3.26',
    ],
)