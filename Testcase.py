from RSA2 import *
with open('testCase.txt', 'r') as fileReader:
    for line in fileReader:
            m =line.rstrip()
            print(m)
            p, q = GetP_Q()
            n = p  * q
            phi_n = (p-1)* (q-1)
            e = Calculate_e(phi_n)
            M = to_Asci(m)
            print("x")
            m_weight = max(M)
            while(m_weight > n):
                  print("x")
                  p, q = GetP_Q()
                  n = p  * q
                  phi_n = (p-1)* (q-1)
                  e = Calculate_e(phi_n)
            print("x")
            chiper = Encryption(m, e, n)
            d = mult_inv(e, phi_n)
            Message = Decryption(chiper,d, n )
            file = open('result.txt', 'w')
            file.write("p = " + str(p) + "\n")
            file.write("q = " + str(q) + "\n")
            file.write("n = " + str(n) + "\n")
            file.write("phi_n = " + str(phi_n) + "\n")
            file.write("e = " + str(e) + "\n")
            file.write("cipher = " + str(chiper) + "\n")
            file.write("d = " + str(d) + "\n")
            file.write("Message = " + str(toStr(Message)) + "\n")
            file.close()

      

fileReader.close()
