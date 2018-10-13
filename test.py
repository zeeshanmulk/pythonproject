class Name:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        print (self.firstname + " " + self.lastname)

    def return_firstnamme(self):
        return self.firstname


n1 = Name("Zeeshan", "Mulk")
n1.print_name()


