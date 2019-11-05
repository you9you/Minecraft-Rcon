import readline
import getopt
import sys
import re
from libs.rcon import MCRcon
from libs.command import Completer

import os
import json

def main():
    os.chdir(os.path.split(os.path.realpath(__file__))[0])
    
    try:
        with MCRcon(host, password, port) as mcr:
            completer = Completer()
            readline.parse_and_bind("tab: complete")
            readline.set_completer(completer.complete)
            while True:
                try:
                    command=input('> ')
                    if command == 'exit':
                        print('Bye')
                        sys.exit(0)
                    resp = mcr.command(command)
                    print(resp) #输出
                except KeyboardInterrupt:
                    print('^C\nBye')
                    sys.exit(0)
    except Exception as e:
        print('\n    ' + str(e) + '\n')
        sys.exit(1)


if __name__ == "__main__":
    host = ''
    port = 25575
    password = ''
    
    version = '0.1'
    argv = sys.argv
    usage = '\nusage:\n    ' + argv[0] + ' -H <server> [-p <port>] -P <password>\n\nOptions:\n    -h  --help\t\t查看帮助信息\n    -v  --version\t查看版本信息\n    -H  --host\t\t服务器地址\n    -p  --port\t\t服务器Rcon端口\n    -P  --password\t服务器Rcon密码\n'
    
    try:
        opts, args = getopt.getopt(argv[1:],'hvH:P:p:',['help','version',"host=","password=","port="])
    except getopt.GetoptError as e:
        print ('\n invalid syntax: ' + str(e) + '\n')
        print (usage)
        sys.exit(-1)
    
    if len(argv) == 1:
        print(usage)
        sys.exit(0)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print (usage)
            sys.exit(0)
        elif opt in ("-v", "--version"):
            print ('version: ' + version + '\n')
            sys.exit(0)
        elif opt in ("-H", "--host"):
            host = arg
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-P", "--password"):
            password = arg
    
    main()