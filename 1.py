#physics calculater progarm
#NO CODE IS RUN HERE,IT IS TELLING US WHAT WE WILL DO LATER
#HERE WE WILL DEFINE OUR FUNCTIONS
#THIS PRINT THE MAIN MENU AND PROMPTS FOR A CHOICE

def menu():
   #print what options you have
   print "welcome to calculator.py"
   print "your options are:"
   print ""
   print "1)surface energy"
   print "2)Moment of inertia"
   print "3)latent heat"
   print "4)entorpy"
   print "5)quit program"
   print ""
   return input("choose your option:")

#THIS DIVIDES TWO NUMBERS GIVEN
def div(a,b):
    print a,"/",b,"=",a/b
#THIS MULTIPIES TWO NUMBERS GIVEN
def mul(a,b):
    print a,"*",b ** 2 ,"=",a*(b**2)

#NOW THE PROGRAM REALLY STARTS,AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
  choice = menu()
  if choice == 1:
      div(input("work:"),input("area:"))                                                       
  elif choice == 2:
      mul(input("mass:"),input("distance:"))
  elif choice == 3:
      div(input("heat:"),input("mass:"))
  elif choice == 4:
      div(input("heat:"),input("temperture:"))
  elif choice == 5:
      loop =0
print "thank u for using physics calculator.py!"
print "made by Ro706"
#NOW THE PROGRAM REALLY FINISHES
