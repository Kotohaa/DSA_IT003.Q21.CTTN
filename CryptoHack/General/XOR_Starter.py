s = "label"
result = ""
for i in range(len(s)):
    result += chr(ord(s[i]) ^ 13)
print(result)
