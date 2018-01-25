n = 9
pos = []
class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return chr(ord('A') + self.y) + str(self.x+1)
    def __repr__(self):
        return chr(ord('A') + self.y) + str(self.x+1)

x, y = 0, 0

def is_conflict(pos, x, y):
    for p in pos:
        if p.x == x or p.y == y or abs(p.x-x) == abs(p.y-y):
            return True
    return False

while(True):
    if y >= n:
        print(pos,'Finish')
        break
        x = n #当找到一个解时，令x=n来进行回溯
    if x >= n: #x走完当前行，回溯
        if (len(pos)==0): #如果全部回溯完
            print('End')
            break
        last = pos.pop()
        x = last.x+1
        y = last.y
        continue #x有可能再次越界，因此再从头循环检查x的值是否越界，如果x未越界，则进行下一次循环也是走下面的判断语句
    if is_conflict(pos, x, y):
        x += 1 #如果冲突，走同一行下一列
    else:#如果不冲突，就塞进pos,然后走到下一行第一个
        pos.append(Pos(x,y))
        x = 0
        y += 1