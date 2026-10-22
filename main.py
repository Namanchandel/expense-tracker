from datetime import date
def add_expense(task,expense,expense_list,expense_type):
    d={
        "date":date.today().isoformat(),
        "category":task.strip().upper(),
        "expense":expense,
        "expense_type": expense_type
    }
    expense_list.append(d)
#expense list for each day. 
expense_list=[]
total=0
while True:
    task=input("enter category ").strip()
    
    if(task.lower()=='done'):
        break
    if not task:
        print("category cannot be empty")
        continue
    while True:
        try:
            expense=int(input("enter amount "))
            if expense<=0:
                print("expense must be greater than zero")
                continue
            break
        except ValueError:
            print("please enter a whole number")

    while True:

        choice=input("enter choice 1 for regular, 2 for monthly ").strip()
        if(choice=="1"):
            expense_type="regular"
            break
        elif(choice=="2"):
            expense_type="monthly"
            break
        else:
            print("invalid choice, enter 1 for regular or 2 for monthly")
            

    add_expense(task,expense,expense_list,expense_type)
category_total=[]
for i in expense_list:
    found=False
    for j in category_total:
        if(i["category"] == j["category"]):
            j["expense"]=j["expense"]+i["expense"]
            found=True
            break
    if (found==False) :
        category_total.append({
            "category":i["category"],
            "expense":i["expense"]
    }
    )
print("category-total",category_total)
print("expense list ",expense_list)

