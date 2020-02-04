"""Write a Program in Python to calculate salary of an employee given
his basic pay (take as input from user). Calculate gross salary of
employee. Let HRA be 10 % of basic pay and TA be 5% of basic
pay. Let employee pay professional tax as 2% of total salary.
Calculate net salary payable after deductions."""
basic_pay=(input("enter your basic pay"))
if (basic_pay).isdigit()==False:
    print("invalid entry")
else:
    basic_pay=float(basic_pay)
    if basic_pay<=0:
        print("invalid entry")
    else:
        name=input("enter name")
        id=input("enter id")
        HRA=(10/100)*basic_pay
        TA=(5/100)*basic_pay
        total_salary=basic_pay+TA+HRA
        tax=(2/100)*total_salary
        final_salary=total_salary-tax
        print(name)
        print(id)
        print(basic_pay)
        print(HRA)
        print(TA)
        print(tax)
        print(total_salary)
        print(final_salary)
	print("thank you")
