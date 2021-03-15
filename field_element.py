class FieldElement:
  def __init__(self, num, prime):
    if num >= prime or num < 0:
      error = 'Num {} not in field range 0 to {}'.format(num, prime - 1)
      raise ValueError(error)
    self.num = num
    self.prime = prime
  
  def __repr__(self):
    return 'FieldElement_{}({})'.format(self.prime, self.num)
  
  def __eq__(self, other):
    if other is None:
      return False
    return self.num == other.num and self.prime == other.prime

  def __ne__(self, other):
    return not (self.num == other.num and self.prime == other.prime)

  def __add__(self, other):
    if self.prime != other.prime:
      raise TypeError('Cannot add two numbers in different Fields')
    num = (self.num + other.num) % self.prime
    return self.__class__(num, self.prime)

  def __sub__(self, other):
    if self.prime != other.prime:
      raise TypeError('Cannot sub two numbers in different Fields')
    num = (self.num - other.num) % self.prime
    return self.__class__(num, self.prime)

  def __mul__(self, other):
    if self.prime != other.prime:
      raise TypeError('Cannot mul two numbers in different Fields')
    num = (self.num * other.num) % self.prime
    return self.__class__(num, self.prime)
    
  def __pow__(self, exponent):
    n = exponent % (self.prime - 1)
    num = pow(self.num, exponent, self.prime)
    return self.__class__(num, self.prime)

  def __truediv__(self, other):
    if self.prime != other.prime:
      raise TypeError('Cannot div two numbers in different Fields')
    # b^(p - 1) % p = 1
    # b^(p - 2) % p = b^(-1)
    # a / b = a * b^(-1) = a * b^(p - 2)
    num = self.num * pow(other.num, self.prime - 2, self.prime) % self.prime
    return self.__class__(num, self.prime)
