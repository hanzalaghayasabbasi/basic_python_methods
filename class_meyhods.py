class Employee:
    Employee = "hanz"

    def __init__(self, roll):
        self.roll = roll

    @classmethod
    def detail(cls, input_obj):
        cls.Employee = input_obj.Employee
        print("The name of Employee is {0} and Roll No is {1}".format(cls.Employee, input_obj.roll))


o = Employee(2109)
print(o.Employee)
o.detail(Employee("Hanzala"))
