class Pilha:
  def __init__ (self):
    self.pilha = list()
   
  def isEmpty(self, list):
    if len(self.pilha) == 0:
      return True
      
  def push(self, item):
    if len(self.pilha) <= 20:
      self.pilha.append(item)
    else:
      print ("Error")
  def pop(self):
    return self.pilha.pop()
 
  def peek(self):
    return self.items[len(self.items)-1]

  def length(self):
    return len(self.pilha)
pilha = Pilha()