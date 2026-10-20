from datetime import date
def add_expense(task,expense,expense_list):
    d={
        "date":date.today().isoformat(),
        "category":task,
        "expense":expense
    }
    expense_list.append(d)
#expense list for each day. 
expense_list=[]
total=0
while True:
    task=input("enter category ").strip()
    
    if(task.lower()=='done'):
        break
    expense=int(input("enter amount "))
    add_expense(task,expense,expense_list)
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

