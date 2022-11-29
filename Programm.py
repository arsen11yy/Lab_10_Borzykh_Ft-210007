class Programm:
  n = int(input("Введите натуральное число N = "))
  d = 64
  while n > 0:
    k = n // d
    if k > 0:
        print("{0} - {1}".format(d, k))
        n = n % d
    d = d // 2

