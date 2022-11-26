from sys import argv

def main():
    # Taking input from user
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()







    # Stocks Information
    objectList={	'TSHIRT':{'Category':'Clothing','Price':1000,'Discount':0.1},'JACKET':{'Category':'Clothing','Price':2000,'Discount':0.05},'CAP':{'Category':'Clothing','Price':500,'Discount':0.2},'NOTEBOOK':{'Category':'Stationery','Price':200,'Discount':0.2},'PENS':{'Category':'Stationery','Price':300,'Discount':0.1},'MARKERS':{'Category':'Stationery','Price':500,'Discount':0.05}	}
    cart={}
    addItem=['ADD_ITEM']
    printItem=['PRINT_BILL']
    maxItems={'Clothing':2,'Stationery':3}
    
    for line in lines:
        #split the line into commands
        command=line.split(' ')
        for i in range(len(command)):
        	command[i]=''.join(command[i].split())
        
        # Adding to cart
        if(command[0] in addItem):
        	cart.setdefault(command[1],0)
        	temp=cart[command[1]]+int(command[2])
        	if(temp>maxItems[objectList[command[1]]['Category']]):
        		#tag print(str(cart)+command[1]+command[2]) Quantity exceed
        		print('ERROR_QUANTITY_EXCEEDED')
        	else:
        		cart[command[1]]+=int(command[2])
        		print('ITEM_ADDED')
        
        #calculating and printing the bill
        elif(command[0] in printItem):
        	total=0
        	discount=0
        	output = ''
        	for item in cart:
        		discount=discount+((objectList[item]['Discount']*objectList[item]['Price'])*cart[item])
        		total=total+(objectList[item]['Price']*cart[item])
        	if(total>=1000):
        		total=total-discount
        	else:
        		discount=0
        	if(total>=3000):
        		discount+=total*0.05
        		total=total-(total*0.05)
        	print('TOTAL_DISCOUNT '+str("%.2f"%discount))
        	total=total+(total*0.1)
        	print('TOTAL_AMOUNT_TO_PAY '+str("%.2f"%total))
        	cart.clear()
        
        #irrelevant input
        else:
        	print('Invalid Command')
        	
        #process the input command and get the output
        # Once it is processed print the output using the command System.out.println()
      
if __name__ == "__main__":
    main()
