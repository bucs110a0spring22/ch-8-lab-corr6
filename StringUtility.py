class StringUtility:
  def __init__(self, string):
    self.string = string
    
  def __str__(self):
    return str(self.string)
    
  def vowels(self):
    vowels = "aeiouAEIOU"
    count = 0
    for i in self.string:
      if i in vowels:
        count += 1
      if count >= 5:
        return "many"
    return str(count)
    
  def bothEnds(self):
    if len(self.string) <= 2:
      return ""
    else:
      return (self.string[:2] + self.string[-2:])

  def fixStart(self):
    new = ""
    if len(self.string) <= 1:
      return str(self.string)
    else:
      firstchar = self.string[0]
      for i in self.string[1:]:
        if i == firstchar:
          new += "*"
        else:
          new += str(i)
      return str(firstchar) + str(new)

  def asciiSum(self):
    asciisum = 0
    for i in self.string:
      asciisum += ord(i)
    return asciisum

  def cipher(self):
    ciph = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    inc = len(self.string)
    for i in self.string:
      if i in alphabet:
        letter = chr(ord(i)+inc)
        while ord(letter) >= 91 and i.isupper():
          letter = chr(ord(letter) - 26)
        while ord(letter) >= 123 and i.islower():
          letter = chr(ord(letter) - 26)
      else:
        letter = i
      ciph += letter
    return ciph
        
