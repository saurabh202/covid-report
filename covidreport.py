class CovidError(Exception):
    def __init__(self,a,b):
        self.oxy=a
        self.report=b

    def __str__(self):
        return 'Oxygen level: '+str(self.oxy)+' and HRTC report: '+str(self.report)

class Patient:
    def __init__(self):
        self.name=input('Enter Patient name: ')
        self.age=int(input('Enter Patient age: '))
        self.oxy=float(input('Enter oxygen level: '))
        self.report=int(input('Enter HRCT report: '))
        
        try:
            if(self.oxy<90 or self.report>10):
                raise CovidError(self.oxy,self.report)
            else:
                self.display()
        except CovidError as co:
            self.display()
            print('*********************************')
            print(co)
            print(self.name+' is Covid Positive !!')
        finally:
            print('Take care :)')   

    def display(self):
        print('*********************************')
        print('Name:',self.name)
        print('Age:',self.age)
        print('Oxygen level:',self.oxy)
        print('HRTC Report:',self.report)

ob=Patient()
