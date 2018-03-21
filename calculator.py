#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv # ???? csv ??


# ????????
class Args(object):

    def __init__(self):
        self.args = sys.argv[1:]
    def read_path(self):
        if len(self.args) == 6:
            return self.args[1],self.args[3]
        else:
            print("Parameter Error")
            print(sys.argv[0], "srcfile dstfile")
            sys.exit(-1)
        sys.exit(0)


args=Args()

# ?????
class Config(object):

    def __init__(self):
        self.config = self._read_config()

    # ??????????
    def _read_config(self):
        config = {'total':0}
        path1=args.read_path()[0]
        with open(path1,'r') as list:
            for i in list.readlines():
                i=i.split('=')
                
                sum_num=0
                num= i[0].strip()
                prop =float(i[1].strip())
                if num == 'JiShuL' or num == 'JiShuH':
                    config[num]=float(prop)
                else:
                    config['total'] += prop
        return config 
                
        
      #  for key,values in config.items():
       #     if key=='JishuH' or key=='JishuL':   
       #         pass
       # else:
       #     print(values)
              #  sum_prop+=values
     #   print(sum_prop)
        """
        ?????
        1. ??????????????????????????? config ???.
        2. ?? strip() ? split() ?????????????????.
        3. ???????????.
        """
c=Config()
read_config=c._read_config()
print(read_config)
# ?????
class UserData(object):

    def __init__(self):
        self.userdata = self._read_users_data()

    # ??????????
    def _read_users_data(self):
        userdata = []
        path=args.read_path()[1]
        with open(path,'r') as list:
            for i in list.readlines():
                i=i.split(',')
                tuple1=(int(i[0]),int(i[1]))
                userdata.append(tuple1)
        return userdata      
        print(userdata)
        """
        ?????
        1. ?????????????????? ID ?????.
        2. ???????????????????? userdata ???.
        3. ???????????.
        """
user=UserData()
list_userdata=user._read_users_data()

 
# ???????

class IncomeTaxCalculator(object):

    # ?????????????
    def calc_for_all_userdata(self):
        pass


    def get_salary(ratio,deductions):
       
        salary_after=tax_before - (taxable*ratio-deductions)
 
        print(str(ID)+':'+format(salary_after,'.2f'))
    
    
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
            print('????')
    for i,j in list_userdata:
        print(i,j)
        print(insurance=j*config['total'])
#            tax_before=int(salary_before)*(1-0.165)
 #           taxable=tax_before-3500
  #          get_salary_after()
	
'''        
except (IndexError,ValueError):
    print("???:'id:salary_before'")
        """
        ?????
        1. ????????????????????.
        2. ?????????.
        3. ?????????????????.
        """

    # ?? CSV ????
    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
        with open("???????????????") as f:
            writer = csv.writer(f)
            writer.writerows(result)

'''
# ??
if __name__ == '__main__':
    """
    ?????????
    """
    print(args.read_path())
