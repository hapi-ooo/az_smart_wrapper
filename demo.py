import subprocess

p1 = subprocess.run('which az', shell=True, capture_output=True, text=True)

print(p1.stdout)
print(p1)