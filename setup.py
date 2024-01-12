from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding='utf-16-le') as f:
    requirements = f.read().splitlines() 

setup(
    name='Booking_Breakdown_By_Origin',
    version='0.1',
    packages=find_packages(),
    install_requires= ["blinker==1.7.0",
"click==8.1.7",
"colorama==0.4.6",
"Flask==3.0.0",
"importlib-metadata==6.8.0",
"itsdangerous==2.1.2",
"Jinja2==3.1.2",
"MarkupSafe==2.1.3",
"pyperclip==1.8.2",
"Werkzeug==3.0.1",
"zipp==3.17.0"]
)
