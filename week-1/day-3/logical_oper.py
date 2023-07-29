"""
Logical Operators
Answer -> bool (True/False)

physics>33      chemistry>33
AND
Condition 1     Condition 2     Result
    F               F              F
    T               F              F
    F               T              F
    T               T              T

OR
Condition 1     Condition 2     Result
    F               F              F
    T               F              T
    F               T              T
    T               T              T

NOT

Reverses the result
"""
physics = 22
chemistry = 19

print(physics > 33 and chemistry > 33)
print(not (physics > 33 or chemistry > 33))
print(physics > 33 and not chemistry > 33)
False and True
print(not physics > 22)
