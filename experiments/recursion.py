import time

def rec(count=0):
    count += 1
    print(count)
    if count > 5:
        return
    rec(count)

rec()
