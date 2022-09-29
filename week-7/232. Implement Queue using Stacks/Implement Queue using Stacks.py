class MyQueue:
  '''
  class myqueue
  '''

    def __init__(self):
      '''
      initialization
      '''
        self.sec_lis = []

    def push(self, x: int) -> None:
      '''
      pushing to the stack
      '''
        self.sec_lis.append(x)
        

    def pop(self) -> int:
      '''
      poping from the first
      Return:
          removed element
      '''
        fir_elm = self.sec_lis[0]
        self.sec_lis.pop(0)
        return fir_elm

    def peek(self) -> int:
      '''
      Return:
          the first elem
          '''
        return self.sec_lis[0]
        

    def empty(self) -> bool:
      '''
      Retrun:
          true if the stack is empty
          '''
        if not self.sec_lis:
            return True
        else:
            return False
        
