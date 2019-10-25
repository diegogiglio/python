class Staff:
    @property
    def position(self):
        print("Getter Method")
        return self._position

    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Basic':
            self._position = value
        else:
            print('Position is invalid. No changes made.')


    def __init__ (self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print('Creating Staff Object')

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d"%(self._position, self.name, self.pay)

    def calculatePay(self):
        prompt = '\nEnter number of hours worked for %s: '%(self.name)
        hours = input(prompt)
        prompt = 'Enter the hourly rate for %s: '%(self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours)*int(hourlyRate)
        return print(self.pay)


officeStaff1 = Staff('Basic', 'Yvonne', 0)
officeStaff1.position = "Coitado"
print(officeStaff1.position)

'''
print(officeStaff1.name)
print(officeStaff1.position)
officeStaff1.calculatePay()
print(officeStaff1)
'''