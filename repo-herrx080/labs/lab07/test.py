p = "A man, a plan, a canal... Panama!"

s = p

for ch in ". ! ,":
    s = s.replace(ch, "")


print(s)
