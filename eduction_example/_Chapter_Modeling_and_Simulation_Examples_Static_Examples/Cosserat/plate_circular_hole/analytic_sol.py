


import numpy as np 

lambda_ = 10 
mu = 1e7
chi = 1e8
pi1 = 10
pi2 = 10
pi3 = 1e9

R = 1


c_2 = pi3 * (mu + chi) / chi / (2. * mu + chi )
b_2 = pi3 / 2. / ( 2. * mu + chi )
poisson = lambda_ / ( 2 * lambda_ + 2 * mu + chi)

c = np.sqrt(c_2)


print (" R/c = " + str( R/c) )
print ("c = " + str(c) )
print ("b_2/c_2 = " + str(b_2/c_2) )

F1 = 8. * ( 1. - poisson ) * b_2 /c_2 / ( 4. + R*R /c_2 + 2. * R / c )

print ("F1 = " + str(F1) )


stress_Concent_ratio = ( 3. + F1 ) / ( 1. + F1 ) 

print ("stress_Concent_ratio = " + str(stress_Concent_ratio) )






