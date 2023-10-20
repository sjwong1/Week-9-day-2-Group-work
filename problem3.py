def problem3():
  # Problem 3 ################################################################
  age = int(input("How old are you?: "))
  if age < 4:
    print("The movie ticket is free!")
  elif age >= 5 and age <= 12:
    print("The movie ticket is 8 dollars.")
  elif age > 13 and age <= 59:
    print("the movie ticket is 12 dollars.")
  elif age >= 60:
    print("The movie ticket is 10 dollars.")
  else:
    print("Invalid response.")
