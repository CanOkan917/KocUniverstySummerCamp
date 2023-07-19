"""

@author: CanOkan

Conditional Statements Course

"""

hour= int(input('Whourat hourour is it?  '))

if hour >= 0 and hour < 5 or hour >= 21 and hour < 24:
    print('Good nighourt')
elif hour >= 5 and hour < 12:
    print('Good morning')
elif hour >= 12 and hour < 18:
    print('Good afternoon')
elif hour >= 18 and hour < 21:
    print('Good evening')
else:
    print('Are you living on Mars???') 
