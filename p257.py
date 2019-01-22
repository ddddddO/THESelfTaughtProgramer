# stack TODO: やりなおす。与えられた入力をpushする感じで
class Stack:
    def __init__(self, iterable):
        self.stack = []
        if isinstance(iterable, str):
            for i in range(len(iterable)):
                self.stack.append(iterable[i])
        self.stack = iterable

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return self.stack == []
    
    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

#1
moziretu = Stack("yesterday")
print(moziretu.size())
reverse = ""
while moziretu.size() > 0:
    reverse += moziretu.pop()
print(reverse)
print(moziretu.size())

print()

#2
nums = Stack([1, 2, 3, 4, 5])
print(nums.size())
reverse_nums = []
while nums.size() > 0:
    reverse_nums.append(nums.pop())
print(reverse_nums)
print(nums.size())