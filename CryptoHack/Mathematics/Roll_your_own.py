import json
from pwn import *

r = remote('socket.cryptohack.org', 13403)

r.recvuntil("Prime generated: ")
q_raw = r.recvline().strip().decode().strip('"')
q = int(q_raw, 16)

g = q + 1
n = q**2

payload1 = json.dumps({"g": hex(g), "n": hex(n)})
r.sendlineafter("Send integers (g,n) such that pow(g,q,n) = 1: ", payload1)

r.recvuntil("Generated my public key: ")
h_raw = r.recvline().strip().decode().strip('"')
h = int(h_raw, 16)

x = (h - 1) // q

payload2 = json.dumps({"x": hex(x)})
r.sendlineafter("What is my private key: ", payload2)

print(r.recvall().decode())
