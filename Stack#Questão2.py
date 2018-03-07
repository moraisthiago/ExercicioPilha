class Pilha:
  def __init__ (self):
    self.pilha = list()
   
  def isEmpty(self, list):
    if len(self.pilha) == 0:
      return True
      
  def push(self, item):
    for i in self.pilha:
      if i != item:
        self.pilha.append(item)
   
  def pop(self):
    return self.pilha.pop()
 
  def peek(self):
    return self.items[len(self.items)-1]

  def length(self):
    return len(self.pilha)
pilha = Pilha()