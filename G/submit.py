import sys

n = int(sys.stdin.readline().strip().split()[0])

password = list("aAaA00!walid")
print(''.join(password))
for i in range(n-1):
    password[0] = chr((ord(password[0]) - ord('a') + 1) % 26 + ord('a'))
    password[1] = chr((ord(password[1]) - ord('A') + 1) % 26 + ord('A'))
    if (i+1) % 26 == 0 and i != 0:
        password[2] = chr((ord(password[2]) - ord('a') + 1) % 26 + ord('a'))
        password[3] = chr((ord(password[3]) - ord('A') + 1) % 26 + ord('A'))
    if (i+1) % (26*26) == 0 and i != 0:
        password[4] = chr((ord(password[4]) - ord('0') + 1) % 10 + ord('0'))
        password[5] = chr((ord(password[5]) - ord('0') + 1) % 10 + ord('0'))
    print(''.join(password))
