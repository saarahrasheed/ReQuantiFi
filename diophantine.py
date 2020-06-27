def gcd(a, b):
    # Equation we are concerned with:
    # d = gcd(a, b) = a*x + b*y
    # assert a >= b >= 0 and a + b > 0
    if b == 0:
        d, x, y = a, 1, 0
    else:
        d, p, q = gcd(b, a % b)
        x = q
        y = p - q*(a//b)
    assert a % d == 0 and b % d == 0
    assert d == a*x + b*y
    return d, x, y

def diophantine(a, b, c):
  assert c % gcd(a, b)[0] == 0
  d, xbar, ybar = gcd(a, b)
  t = c // d
  x, y = xbar*t, ybar*t
  assert a*x + b*y == c 
  return (x, y)

if __name__ == '__main__':
  diophantine(10, 6, 14)