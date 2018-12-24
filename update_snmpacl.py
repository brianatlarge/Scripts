import paramiko

ips = [
"192.168.1.1",
"192.168.1.2"
]

for ip in ips:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()

    ssh.connect(ip, username='sshuser', password='sshpass')

    channel = ssh.invoke_shell()
    stdin = channel.makefile('wb')
    stdout = channel.makefile('rb')

    stdin.write('''
    conf t
    access-list 67 permit 10.0.0.1
    end
    wr mem
    exit
    ''')
    print stdout.read()

    print stdout.read()
    stdout.close()
    stdin.close()
    ssh.close()
