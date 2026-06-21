def uncode(w):
  i = 0
  I = 0
  u = 0
  n = 0
  Slist = []
  Clist = []
  code = ''
  for I in range(0,len(w)):
    Slist.append(w[I])
    Clist.append(I)
  
  if len(w)%2 == 0:
    for i in range (0,len(w)//2):
      Clist[len(w) - i - 1]  = Slist[u]
      Clist[i] = Slist[u+1]
      u+=2
      
  elif len(w) == 1:
    Clist[0] = Slist[0]

  else:
    for i in range (0,len(w)//2):
      Clist[len(w) - i - 1]  = Slist[u]
      Clist[i] = Slist[u+1]
      u+=2
    Clist[len(Clist)//2] = Slist[len(Slist)-1]
    
  for n in range (0,len(w)):
    code = code + str(Clist[n])
  return code

def transleit(t):
  slow = ''
  layout_map = {  
        'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ',
        'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": "э",
        'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '`': 'ё',
        'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш', 'O': 'Щ', 'P': 'З', '[': 'Х', ']': 'Ъ',
        'A': 'Ф', 'S': 'Ы', 'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д', ':': 'Ж', '"': 'Э',
        'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь', '<': 'Б', '>': 'Ю', '~': 'Ё',
        '-': '-', '!' : '1', '@' : '2', '#':'3', '$':'4', '%':'5','^':'6', '&' : '7', '*' : '8', '(':'9', ')':'0'
    }
  for i in range (0,len(t)):
    char = t[i]
    slow = slow + layout_map.get(char, char)
  return slow

def census(q):
  slowo = []
  q = q + 'ff'
  while q != '':
    i = 0
    e = 0
    E = ''
    for i in range (0,len(q)-1):
      if q[i] == ' ':
        break
    for e in range (0,i):
      E = E + q[e]
    if E != '':
      slowo.append(E)
      slowo.append(' ')
    q = (q[(i + 1):])
  return(slowo)

word = ''
word = input('Введите слово или предложение, которое хотите расшифровать ')
F1 = census(word)
F2 = []
for i in range (0, len(F1) - 1):
  F2.append(transleit(F1[i]))
F3 = []
for g in range(0, len(F2)):
  F3.append(uncode(F2[g]))
result = ''
for j in range(0, len(F3)):
  result = result + F3[j]
print(result)
