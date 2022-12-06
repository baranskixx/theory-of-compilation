import sys
import scanner


if __name__ == '__main__':
  # pobranie ścieżki do pliku
  # jeśli ścieżka nie jest podana zakończ działanie programu
  if len(sys.argv) > 1:
    filepath =  sys.argv[1]
  else:
    print('No datasource specified!')
    sys.exit(-1)
  # próba otwarcia pliku
  # jeśli takowe niepowiedzie się zakończ pracę programu
  try:
    file = open(filepath, 'r')
  except IOError:
    print('File specified with path: %s cannot be opened!', filepath)
    sys.exit(-1)
  
  # konstrukcja analizatora wraz z załadowaniem doń pobranego z pliku tesktu
  lexer = scanner.lexer
  lexer.input(file.read())

  for tkn in lexer:
    print("%d: %s(%s)" %(tkn.lineno, tkn.type, tkn.value))



    
