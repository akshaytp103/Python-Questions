

n = int(input("Enter number of locker: "))
def calculate_amount(n):
    money_list = [] 
    for i in range(0, n): 
        ele = int(input('Enter the money in locker'))
        
    # adding the element
        money_list.append(ele) 
    # find toatl amount of money 
    
    res = [sum(money_list[i:: 2])
    for i in range(len(money_list) // (len(money_list) // 2))]
    total=res[0]
    
    # find alternate locker  
       
    money=money_list[::2]
    for i,mo in enumerate(money[::1]):
        print(f"you can Rob locker {i} (money= {mo}) Then ")
        
    print('Total amount you can rob',total)
calculate_amount(n)

