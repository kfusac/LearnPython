import subprocess

print('$ nslookup www.python.org with no input')
r=subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)

print('==================================')
print('$ nslookup with input')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk',errors='ignore'))
print('Exit code:', p.returncode)