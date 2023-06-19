#  Copyright (c) 2023. All rights reserved by Woliul Hasan. Fork me on https://github.com/hmwoliul

"""
  * Created in PyCharm.
  * Project Name: ftptest
  * User: woliul
  * Date: 6/19/23
  * Time: 11:48 AM
"""

import ftplib


def ftp_client():
    # Connect to the FTP server
    ftp = ftplib.FTP("127.0.0.1")
    ftp.login(user="admin", passwd="password")

    print("Connected to FTP server.")

    while True:
        print("\n--- Menu ---")
        print("1. List files")
        print("2. Download file")
        print("3. Upload file")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # List files and directories
            files = ftp.nlst()
            print("Files and directories on the server:")
            for file in files:
                print(file)

        elif choice == "2":
            # Download file
            filename = input("Enter the filename to download: ")
            with open(filename, "wb") as file:
                ftp.retrbinary("RETR " + filename, file.write)
            print(f"File '{filename}' downloaded successfully.")

        elif choice == "3":
            # Upload file
            filename = input("Enter the filename to upload: ")
            with open(filename, "rb") as file:
                ftp.storbinary("STOR " + filename, file)
            print(f"File '{filename}' uploaded successfully.")

        elif choice == "4":
            # Quit
            ftp.quit()
            print("FTP client terminated.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    ftp_client()
