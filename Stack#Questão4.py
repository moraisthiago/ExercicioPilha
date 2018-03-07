class Pilha:
  def __init__ (self):
    self.pilha = list()
   
  def isEmpty(self, list):
    if len(self.pilha) == 0:
      return True
      
  def push(self, item):
    self.items = [15, 40, 70]
    a = []
    if len(self.items) != 0:
      for i in range(len(self.items)):
		    x.append(self.items.pop())
      return (a)
      return sum(a)

  def pop(self):
    return self.pilha.pop()
 
  def peek(self):
    return self.items[len(self.items)-1]

  def length(self):
    return len(self.pilha)
pilha = Pilha()