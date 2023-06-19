# ftptest

FTP Server Project Distributed System Lab

Copyright (c) 2023. All rights reserved by Woliul Hasan. Fork me on https://github.com/hmwoliul

## Note:

* This project Used **Pycharm 2023.1.2**
* Folder `venv` used for this project only
* Import packages from **IDE** or import using Pip
* Use **Python 3.9.6** and **pip 22.3.1**

## Requirements:

* ````ftplib```` module built in with python so no need to install

  ````pip install pyftpdlib````


* If authentication failed after run ````server.py```` then use ````sudo```` in linux or run cmd as
  ***run as administrator*** in windows

* **run in terminal or cmd**

  ````
  python server.py
  ````
* **or use sudo & run in terminal**
  ````
    sudo python server.py
    ````
* **Connect different FTP server eg: Adobe ftp**

  ````
  ftp = ftplib.FTP("ftp.adobe.com")
  ftp.login(user="", passwd="")`
  ````
