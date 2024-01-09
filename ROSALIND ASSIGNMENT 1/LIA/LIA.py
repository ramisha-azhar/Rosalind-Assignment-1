import math   

k = 6                                                                        
n = 16                                                                        
p = 2**k                                                                       
prob = 0      

for i in range(n, p + 1):                                                      
    calc_prob = (math.factorial(p) /(math.factorial(i) * math.factorial(p - i))) * ((1/4)**i) * ((3/4)**(p - i))                                                        
    prob += calc_prob                                                        
print(prob)   