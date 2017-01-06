import sys
import os
import paramiko
import time

def main():
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('xxx.xxx.xxx.xxx', username='ENTER USER', password='ENTER PASS')

        sftp = client.open_sftp()
        sftp.put('remote_script.py', '/root/remote/remote_script.py')

        stdout = client.exec_command('python /root/remote/remote_script.py')

        time.sleep(10)
        sftp.get('/root/remote/report.txt', 'report.txt')
        
        sftp.close()
        client.close()
       
        print stdout

if __name__ == '__main__':
    main()
