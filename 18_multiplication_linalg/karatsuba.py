"""
pq = (a + b)(c + d)

(a + b)(c + d) = (a*c) + (a*d + b*c) + (b*d)
(a*d + b*c) = (a + b)(c + d) - (a*c) - (b*d) 

pq = (aX + b)(cX + d)
pq = (a*c)X^2 + (a*d + b*c)X  +(b*d)
pq = (a*c)X^2 + [(a + b)(c + d) - (a*c) - (b*d)]X  +(b*d)
=> only three recursive multiplications!

"""

def karatsuba(x: int, y: int) -> int:
    if x < 10 or y < 10: # expected runtime: O(n)
        return x * y
    else:
        n: int = max(len(str(x)), len(str(y)))
        half: int = n // 2

        # x => h1 + l1; y => h2 + l2
        h1: int = x // 10**half
        l1: int = x % 10**half
        h2: int = y // 10**half
        l2: int = y % 10**half

        # 
        z2: int = karatsuba(h1, h2)
        z1: int = karatsuba(h1 + l1, h2 + l2)
        z0: int = karatsuba(l1, l2)

        product = ((z2 * 10**(2*half)) + ((z1 - z2 - z0) * 10**half) + z0)
        
        return product
    
print(karatsuba(31415926, 27182818))
