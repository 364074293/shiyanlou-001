#!/usr/bin/env python3
import sys


try:

    def get_salary(ratio,deductions):
       
        salary_after=tax_before - (taxable*ratio-deductions)
 
        print(ID+':'+format(salary_after,'.2f'))
    
    
    def get_salary_after():
        if taxable>80000:
            get_salary(0.45,13505)
        elif 55000<taxable<=80000:
            get_salary(0.35,5505)
        elif 35000<taxable<=55000:
            get_salary(0.3,2755)
        elif 9000<taxable<=35000:
            get_salary(0.25,1005)
        elif 4500<taxable<=9000:
            get_salary(0.2,555)
        elif 1500<taxable<=4500:
            get_salary(0.1,105)
        elif 0<taxable<=1500:
            get_salary(0.03,0)
        elif -3500<taxable<0:
            get_salary(0,0)
        else:
            print('输入有误')
    sys.argv.pop(0)
    for i in sys.argv:
        ID=i.split(':')[0]
        salary_before=i.split(':')[1]

        try:
            tax_before=int(salary_before)*(1-0.165)
            taxable=tax_before-3500
            get_salary_after()
        except:  
            print("Parameter Error")
	

        
except (IndexError,ValueError):
    print("请输入:'id:salary_before'")

