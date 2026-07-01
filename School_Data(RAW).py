# s=0
def students_data (n,d,r):
    # s+=1
    f=open('student data','a')
    f.write(f'\n{r} = roll number, stuedents name = {n}, DOB = {d}')
    f.close()
def read_data():
    f=open('student data','r')
    print(f.read())
    f.close()
def read_specific_data(r):
    b=0
    f=open('student data','r')
    data = f.readlines()
    for i in data:
        if (i.startswith(r)):
            print(i)
            b=1
    f.close()
    if b==0:
        print('roll number not found')
    b=0
    

def delete_data(r):
    b=0
    f=open('student data','r')
    data = f.readlines()
    f.close()
    f=open('student data','w')
    for i in data :
        if not(i.startswith(r)):
            f.write(i)
        else:
            b=1
    f.close()
    if b==0:
        print('roll number not found')
     
    


def main():
    a=0
    while a!=5:
        print('\n type 1 for adding student \n type 2 for reading data \n type 3 for reading specific student data \n type 4 for deleting student data, \n enter 5 for exit')
        a=int(input())
    
        if a==1:
            students_data(str(input('Enter full name :',)),str(input('enter DOB in XX/XX/XXXX format as date/month/year :',)),(input('enter roll number :',)))

        elif a==2:
            read_data()
        elif a==3:
            read_specific_data(input())
        elif a==4:
            delete_data(input())
        elif a==5:
            a=5
        else:
            print('wrong input')
    
main()
 