from stanfordkarel import *


class ktools:
  def m(self):
     """shorthand for move"""
     move()
  def tl(self):
    """turn left"""
    turn_left()
  def tr(self):
    """turn right"""
    self.tl()
    self.tl()
    self.tl()
  def ta(self):
      """turn around
      self.tl()
      self.tl()
 def pick(self)
      """put beeper"""
      put_beeper()

      def put2(self):
      self.put()
      self.m()
      self.put()

      def put5(self):
        self.put2()
        self.move()
        self.put2()
        self.move()
        self.put()

        def h(self):
          """print H using beeper"""
          self.tl()
          self.put5()
          self.tr()
          self.m()
          self.m()
          self.m()
          self.tr()
          self.put5()
          self.ta()
          self.m()
          self.m()                       
          self.tl()
          self.m()
          self.put2()
          self.tl()
          self.m()
          self.m()
          self.tl()
          self.m()
          self.m()
          self.m()
          self.m()
def main():
    """ Karel code goes here! """
   
    pass


if __name__ == "__main__":
    run_karel_program()