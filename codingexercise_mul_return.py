def leap_year(year):
    if year % 4 == 0:
        
      if year % 100 == 0:
        
        if year % 400 == 0:
           print("Leap Year")
        else:
           print("Not Leap Year")
      else:
       print("Leap year")
def days_of_month(year,month):
   days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
   if leap_year and month==2:
      return 29
   else:
      return days_list[month-1]
year=int(input("Enter a year:"))
month=int(input("Enter a month:"))
days=days_of_month(year,month)
print(days)
