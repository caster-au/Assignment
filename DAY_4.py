altitude=int(input("Enter Altitude: "))
if altitude<=1000:
    print("Safe to land")
elif altitude>1000 and altitude<=5000:
    print("Come Down to 1000ft")
elif altitude>5000:
    print("Turn Around and Try next time to land")