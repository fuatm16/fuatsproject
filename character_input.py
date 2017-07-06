__author__ = 'fuat'
name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2017 - age)+100)
print(name + " will be 100 years old in the year " + year)
if ( age%2 == 0 ):
    print("you are in even age!" )
else:
    print("you are in odd age!")


def tekrardene(retries=0):
    if retries >10:
        exit(0)

    try:
        tekrardene.num = int(input("Please choose a number to divide: "))
        if (tekrardene.num < 0 and retries<10 ):
            print("Lutfen 0 dan buyuk bir sayi giriniz")
            retries += 1
            if retries > 10:
                exit(0)
            tekrardene()
    except ValueError:
        retries+=1
        print ("ValueError hatasi alindi")
        tekrardene()

tekrardene()

listRange = list(range(1,tekrardene.num+1))


divisorList = []
for number in listRange:

    if tekrardene.num % number == 0:

        divisorList.append(number)

print(divisorList)