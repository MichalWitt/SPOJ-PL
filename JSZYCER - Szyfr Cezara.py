import sys
def string(n):
   if n == ' ':
      return ' '
   elif n == ('\n'):
      return (chr(ord(n)))
   elif n == 'X' or n == 'Y' or n == 'Z':
      return (chr(ord(n)-23))
   else:
      return (chr(ord(n)+3))

tekst = sys.stdin.read()
x = list(map(string, tekst))
x=''.join(x)
print(x)
