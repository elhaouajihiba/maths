from automate import Automate
from state import State
from transition import Transition
from parser import *

##-----------------------------------PRISE EN MAIN------------------------------------------

## creation d’etats
# s0 : State
s0 = State(0, True, False)
# s1 : State
s1 = State(1, False, False)
#s2 : State
s2 = State(2, False, True)

## creation de transitions

#t : Transition
t = Transition(s0,"a",s1)


# t1 : Transition

t1 = Transition(s0,"a",s0)
# t2 : Transition
t2 = Transition(s0,"b",s1)
# t3 : Transition
t3 = Transition(s1,"a",s2)
# t4 : Transition
t4 = Transition(s1,"b",s2)
# t5 : Transition
t5 = Transition(s2,"a",s0)
# t6 : Transition
t6 = Transition(s2,"b",s1)

# liste_trans : list[Transition]
liste_trans = [t,t1,t2,t3,t4,t5,t6]

# liste_etats : list[State]
liste_etats = [s0,s1,s2]

## creation de l’automate
# auto : Automate
auto = Automate(liste_trans)

# auto1 : Automate
auto1 = Automate(liste_trans, liste_etats)

# auto2 : Automate
auto2 = Automate.creationAutomate("auto.txt")


print(auto)
auto.show("exo1")

#print(auto1)
#auto1.show("exo1_2")

#print(auto2)
#auto2.show("exo1_3")

##----------------------------------MANIPULATION--------------------------------------

auto.removeTransition(t)

#print(auto)
#auto.show("exo2rem")

auto.addTransition(t)


#print(auto)
#auto.show("exo2add")

auto.removeState(s1)

#print(auto)
#auto.show("exo2rem_s")


auto.addState(s1)

print(auto)
auto.show("exo2add_s")



#s3 : State
s3 = State(0,True,False) 


auto.addState(s3)

print(auto)
auto.show("exo2add_s3")





















