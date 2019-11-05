# Minecraft-Rcon
基于Python写的Minecraft服务端rcon控制台

### 命令行:
`python3 main.py -H <server> [-p <port>] -P <password>`

### 选项:
```shell
	-h  --help          查看帮助信息
	-v  --version       查看版本信息
	-H  --host          服务器IP地址/域名
	-p  --port          服务器Rcon端口
	-P  --password      服务器Rcon密码
```

### 默认端口连接(示例)
`python3 main.py -H 192.168.1.1 -P 123456`