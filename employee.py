#Employee management

def addnewrec():
    try:
        with open("employee.txt","a+") as f:
            
            eid=input("Emplyee id: ")
            ename=input("Emplyee name: ")
            gen=input("Gender: ")
            doj=input("Date of joining: ")
            dept=input("Department: ")
            s=eid+" "+ename+" "+gen+" "+doj+" "+dept+" \n"
            f.write(s)
    except:
        pass


def viewrec():
    try:
        with open("employee.txt","r") as f:
            f.seek(0)
            x=f.readlines()
            for i in x:
                z=i.split()
                print("Eid:",z[0],"\tEname:",z[1],"\tGender:",z[2],"\tDOJ:",z[3],"\tDept:",z[4])
                print("\n")
    except:
        print("No records")

def editrec():
    try:
        with open("employee.txt","r+") as f:
            x1=[]
            x=f.readlines()
            id=input("Input eid: ")
            for i in x:
                i=str(i)
                z=i.split()

                if z[0]==id:
                    m=int(input("What to change: \n1.Name\n2.Gender\n3.DOJ\n4.Department\n"))
                    if m==1:
                        d=input("Name: ")
                        z[1]=d
                    elif m==2:
                        d=input("Gender: ")
                        z[2]=d
                    elif m==2:
                        d=input("DOJ: ")
                        z[3]=d
                    elif m==2:
                        d=input("Department: ")
                        z[4]=d
                    y=" ".join(z)
                    z=y+" \n"
                    i=z
                x1.append(i)
        with open("employee.txt","w") as f:
            f.writelines(x1)


    except:
        print("No records")

def delrec():
    try:
        with open("employee.txt","r+") as f:
            x1=[]
            x=f.readlines()
            id=input("Input eid: ")
            for i in x:
                i=str(i)
                z=i.split()
                print(z)
                if z[0]==id:
                   pass
                else:
                    y=" ".join(z)
                    z=y+" \n"
                    i=z
                    x1.append(i)



        with open("employee.txt","w") as f:
            f.writelines(x1)


    except:
        print("No records")



while True:
    ch=int(input("Choice: \n1.Add new record\n2.View record\n3.Edit record\n4.Delete record\n5.Exit\n"))
    if ch==1:
        addnewrec()
    elif ch==2:
        viewrec()
    elif ch==3:
        editrec()
    elif ch==4:
        delrec()
    elif ch==5:
        break
