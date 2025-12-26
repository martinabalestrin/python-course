# just doing a lot of tests, this doesn't makes sense at all

temperature = 45
forecast = "rainy"
raining = True

if temperature > 80:
    print("It's too hot!")
    print("Stay inside!")

elif raining:
    print("Stay inside!")

elif not forecast == "rainy":
    print("Go outside!")

elif temperature < 60:
    print("It's too cold!")
    print("Stay inside!")

else:
    print("Enjoy the outdoors!")

