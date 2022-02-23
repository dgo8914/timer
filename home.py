import time

place = "XXXX"
action  = "YYYYY"

print (" I " + action + " my " + place)

seconds = int(input("time remaining"))
for i in range(seconds) :
     print (str(seconds - i) + " seconds " )
     time.sleep(1)
