class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = [[]]
        self.capacity = capacity

    def push(self, item):
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(item)

    def pop(self):
        if len(self.stacks[-1]) == 0 and len(self.stacks) > 1:
            self.stacks.pop()
        if len(self.stacks[-1]) == 0 and len(self.stacks) == 1:
            return None
        return self.stacks[-1].pop()

    def popAt(self, index):
        if index >= len(self.stacks):
         if len(self.stacks[-1]) == index and len(self.stacks) == index:
            return None
        return self.stacks[-1].pop(index)
 
s = SetOfStacks(5)
while True:
 print("1.Push\t2.Pop\t3.PopAt\n")

 choice = input("Enter your choice\n")
 if choice=="1":
  num = int(input("Enter a number\n"))
  s.push(num)
  print(s.stacks)
  print("\n")
   
 elif choice == "2":
  s.pop()
  print(s.stacks)
  print("\n")
 
 elif choice == "3":
  index = int(input("Index at which you want to pop\n"))
 
  s.popAt(index)