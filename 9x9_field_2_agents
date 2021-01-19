#initialize a 9x9 random field and let 2 agents spawn who will search for each other
#fun project because I read about agents I wanted to know how to create a very small field with 2 agents searching for each other


import numpy as np
from random import *

agent_x = np.zeros([9, 9])
m_1 = randint(0, 8)
m_2 = randint(0, 8)

print(m_1)
print(m_2)

agent_x[m_1, m_2] = 1

print(agent_x)

agent_y = np.zeros([9, 9])
f_1 = randint(0, 8)
f_2 = randint(0, 8)

print(f_1)
print(f_2)

agent_y[f_1, f_2] = 1

print(agent_y)

if m_1 == f_1 and m_2 == f_2:
    print("Juhuu, die Agenten x und y haben sich gefunden!")
else:
    print("Sie müssen sich noch finden")

if m_1 != f_1:
    z = m_1 - f_1
    m_1 = m_1 - z
    print(m_1)
    print(f_1)

if m_2 != f_2:
    z_2 = m_2 - f_2
    m_2 = m_2 - z_2
    print(m_2)
    print(f_2)

agent_x = np.zeros([9, 9])
agent_x[m_1, m_2] = 1

agent_y = np.zeros([9,9])
agent_y[f_1, f_2] = 1
print(agent_x)
print(agent_y)
