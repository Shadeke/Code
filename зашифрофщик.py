def  encode(w):
  i = 0
  n = 0
  code = ''
  if len(w)%2 == 0:
    for i in range(0,(len(w)//2)):
      code = code + w[len(w) - i - 1]
      code = code + w[i]
    return(code)

  if len(w)%2 == 1 and len(w) != 1:
    for i in range(0,(len(w)//2)):
      code = code + w[len(w) - i - 1]
      code = code + w[i]
      n = i
    code = code + w[n+1]
    return(code)

  if len(w) == 1:
    code = code + str(w[0])
    return(code)
    
def translate_layout(text):
  slow = ""
  layout_map = {
        'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']',
        'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': "'",
        'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.', 'ё': '`',
        'Й': 'Q', 'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T', 'Н': 'Y', 'Г': 'U', 'Ш': 'I', 'Щ': 'O', 'З': 'P', 'Х': '{', 'Ъ': '}',
        'Ф': 'A', 'Ы': 'S', 'В': 'D', 'А': 'F', 'П': 'G', 'Р': 'H', 'О': 'J', 'Л': 'K', 'Д': 'L', 'Ж': ':', 'Э': '"',
        'Я': 'Z', 'Ч': 'X', 'С': 'C', 'М': 'V', 'И': 'B', 'Т': 'N', 'Ь': 'M', 'Б': '<', 'Ю': '>', 'Ё': '~',
        '.': '.', ',': ',', '?': '?', '"': '"', '№': '№', ';': ';', ':': ':', ' ': ' ', '-': '-'
    }
  
  for i in range(len(text)):
   char = text[i]
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
      if q[i] == '.' or q[i] == ',' or q[i] == '?' or q[i] == ':':
        i = i +1
        break
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
word = input()
F1 = census(word)
F2 = []
for i in range (0, len(F1) - 1):
  F2.append(translate_layout(F1[i]))
F3 = []
for g in range(0, len(F2)):
  F3.append(encode(F2[g]))
result = ''
for j in range(0, len(F3)):
  result = result + F3[j]
print(result)




