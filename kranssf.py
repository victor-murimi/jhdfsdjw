class Payroll:

    gross_salary=0

    nssf=0

    taxable_pay=0

    payee=0

    nhif=0

    total_deductions=0

    net_salary=0

 

    def __init__(self,basic,benefits):

      self.gross_salary=basic+benefits

      self.nssf()

      self.taxable_pay()

      self.payee()

      self.nhif()

      self.total_deductions()

      self.net_salary()

 

    def nssf(self):

       if self.gross_salary>0 and self.gross_salary<=17999:

        self.nssf=0.06*self.gross_salary

       else:

        self.nssf=1080    

            

    def taxable_pay(self):

        self.taxable_pay=self.gross_salary-self.nssf

    

    def payee(self):

       if  self.taxable_pay>0 and self.taxable_pay<=24000:

          self.payee=self.taxable_pay*0.1

       elif self.taxable_pay>24001 and self.taxable_pay<=32333:

           self.payee=((self.taxable_pay-2400)*0.25)+2400

       else:

           self.payee=(self.taxable_pay-(24000+8333))*0.3 +2400+2083.35

 

    def nhif(self):

      if self.taxable_pay<5999:

        self.nhif=150

      elif self.taxable_pay>=60000 and self.taxable_pay<=7999: 

        self.nhif=300

      elif self.taxable_pay>=80000 and self.taxable_pay<=11999:

        self.nhif=400

      elif self.taxable_pay>=120000 and self.taxable_pay<=14999:

        self.nhif=500

      elif self.taxable_pay>=150000 and self.taxable_pay<=19999:

        self.nhif=600

      elif self.taxable_pay>=20000 and self.taxable_pay<=24999:

        self.nhif=750

      elif self.taxable_pay>=25000 and self.taxable_pay<=29999:

        self.nhif=850

      elif self.taxable_pay>=30000 and self.taxable_pay<=34999:

        self.nhif=900  

      elif self.taxable_pay>=35000 and self.taxable_pay<=39999:

        self.nhif=950

      elif self.taxable_pay>=40000 and self.taxable_pay<=44999:

        self.nhif=1000

      elif self.taxable_pay>=45000 and self.taxable_pay<=49999:

        self.nhif=1100

      elif self.taxable_pay>=50000 and self.taxable_pay<=59999:

        self.nhif=1200

      elif self.taxable_pay>=60000 and self.taxable_pay<=69999:

        self.nhif=1300

      elif self.taxable_pay>=70000 and self.taxable_pay<=79999:

        self.nhif=1400 

      elif self.taxable_pay>=80000 and self.taxable_pay<=89999:

        self.nhif=1500 

      elif self.taxable_pay>=90000 and self.taxable_pay<=99999:

        self.nhif=1600

      else:

        self.nhif=1700

    

    def total_deductions(self):

      self.total_deductions=self.nhif+self.payee

    

    def net_salary(self):

      self.net_salary=self.taxable_pay-self.total_deductions

 

a=int(input("enter basic salary"))

b=int(input("enter benefits"))

victor=Payroll(a,b)

print(victor.net_salary)