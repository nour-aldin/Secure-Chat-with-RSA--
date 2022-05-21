from ast import Continue
import sympy
import random
def GetP_Q():
      primeList=[0,0]
      while(primeList[0] == primeList[1]):
            for i in range(0, 2):
                  n = sympy.randprime(2, 2**8)
                  primeList[i] = n
      return primeList[0], primeList[1]
      #return 17,11

def GCD(x, y):
    if(y == 0):
        return x
    else:
        return GCD(y, x%y)
#get E
def Calculate_e(phi_n):
      e = 2
      while(e < phi_n):
            if GCD(e,phi_n) == 1:
                  print("GCD OF E AND PHI", GCD(e,phi_n))
                  return e   
            else:
                  e = e +1

#Convert Message to Asci code 
def to_Asci(M):
      ascii_values = []
      for character in M:
            ascii_values.append(ord(character))
      
      return ascii_values


#RSA Encryption
def Encryption(M, e, n ):
      C =[]
      MessageList = to_Asci(M)
      

      for m in MessageList:
            C.append((m ** e) % n)
      return C
#Extended Euclidean Algorithm
def ExtendedEuclid(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = ExtendedEuclid(b,a%b)
        s = s-((a//b) * t)
        return(gcd,t,s)

#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=ExtendedEuclid(e,r)
    if(gcd!=1):
        return None
    else:
        return s%r

#RSA Decryption
def Decryption(C, d, n):
      M = []
      print("D is ", d)
      for c in C:
            M.append((c ** d) % n)      
      
      return M
def toStr(asci):
      return (''.join(chr(i) for i in asci))

p, q = GetP_Q()
n = p  * q
phi_n = (p-1)* (q-1)
e = Calculate_e(phi_n)
m = "this is the Message"
M = to_Asci(m)
m_weight = max(M)

while(m_weight > n):
      p, q = GetP_Q()
      n = p  * q
      phi_n = (p-1)* (q-1)
      e = Calculate_e(phi_n)

chiper = Encryption(m, e, n)
print("The encrypted Message is ",chiper)
d = mult_inv(e, phi_n)
print("P is ",p)
print("q is ",q)
print("n is ",n)
print("phi_n is ",phi_n)
print("e is ",e)
print("d is ",d)

Message = Decryption(chiper,d, n )


print("finall message ",Message)
print("string ",toStr(Message))