def problem6():
  # Problem 6 ################################################################

  day = input("What day of the week is it?").lower()
  if day == "saturday" or "sunday":
    print("It's the weekend!")
  elif day == "monday" or "tuesday" or "wednesday" or "thursday" or "friday":
    print("it's a weekday!")
  else:
    print("Invalid date entered")
