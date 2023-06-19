#  Copyright (c) 2023. All rights reserved by Woliul Hasan. Fork me on https://github.com/hmwoliul

"""
  * Created in PyCharm.
  * Project Name: ftptest
  * User: woliul
  * Date: 6/19/23
  * Time: 11:48 AM
"""

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def ftp_server():
    address = ("127.0.0.1", 21)  # IP address and port Authentication may be needed for run this
    root_dir = "root"  # Set the root directory for the server
    username = "admin"  # FTP username
    password = "password"  # FTP password

    # Create a dummy authorizer for managing user authentication
    authorizer = DummyAuthorizer()
    authorizer.add_user(username, password, root_dir, perm="elradfmwMT")

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner string to be displayed when a client connects
    handler.banner = "Welcome to the FTP server"

    # Enable passive mode (PASV)
    handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on defined address and port
    server = FTPServer(address, handler)

    # Set a limit for the maximum number of connections
    server.max_cons = 10
    server.max_cons_per_ip = 5

    # Start the FTP server
    server.serve_forever()


if __name__ == "__main__":
    ftp_server()
