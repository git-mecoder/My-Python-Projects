import modules.calculator as cl
import modules.converter as con

oper = input("What Tool you want to use [Calc, Conv, Rates] → ").strip()
if oper.lower() in ['calc', 'conv', 'rates']:
    if oper.lower() == 'calc':
        cl.calc()
    elif oper.lower() == 'conv':
        con.converter()
    elif oper.lower() == 'rates':
        print("we r working on it right now")
    else:
        print("wrong choice!! ")

