class Emp:
    def __init__(self,fname,lname,dep,des,empno):
        self.fname=fname
        self.lname=lname
        self.dep=dep
        self.des=des
        self.empno=empno

    def disp(self):
        print("Employee name is ",self.fname," ",self.lname)
        print("Employee department is ",self.dep)
        print("Employee designation is ",self.des)
        print("Employee number is ",self.empno)


def main():
    print("Welcome to EMS!")
    l=[]
    cont=1
    counter=0

    while cont == 1:
        d=0
        print("1 for add record, 2 for delete record, 3 for search, 4 for close")
        c=int(input())
        if c == 1:
            print("Enter first name: ")
            fname=input()
            print("Enter last name: ")
            lname=input()
            print("Enter department: ")
            dep=input()
            print("Enter designation: ")
            des=input()
            print("Enter employee number: ")
            empno=int(input())
            l.append(Emp(fname,lname,dep,des,empno))
            counter=counter+1
            print("Do you wish to continue? (1/0): ")
            cont=int(input())
        elif c == 2:
            print("Enter employee number which you want to delete: ")
            dno=int(input())
            i=0
            while i < counter:
                if dno == l[i].empno:

                    print("Record of ", l[counter].fname," ",l[counter].lname," deleted! ")
                    del l[i]
                    counter=counter-1
                    d=1
                i=i+1
            if d==0:
                print("Employee does not exist!")
            print("Do you wish to continue? (1/0): ")
            cont = int(input())
        elif c==3:
            print("Enter employee number you wish to search: ")
            sno=int(input())
            i=0
            while i<counter:
                if sno==l[i].empno:
                    l[i].disp()
                i=i+1
            print("Do you wish to continue? (1/0): ")
            cont = int(input())
        elif c==4:
            break

main()









