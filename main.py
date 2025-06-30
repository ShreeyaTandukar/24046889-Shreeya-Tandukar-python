#doctstring
"""
this is main program for the management system of WeCare store
Feature:
    displaying available products
    selling products to customer with offer of buy 3 get 1 free
    restocking the product via supplier purchase
    generating invoices for both sell and buy operations.
"""


#importing necessary functions from other modules
from read import displaying_product
from operation import sell, buy
from write import generate_invoice, generate_invoice1,calculate_vat
#initialize list to store items in invoices
sell_invoice_items=[]
buy_invoice_items=[]
#initialize variable for keeping trace on offering free items
total_free_items=0
# display menu options
print("choose any number from(1 to 4)\n")
print("1: Display")
print("2: Sell")
print("3: Buy")
print("4: Exit")
#distionary for storing option labels
options={
    1:"Display",
    2:"Sell",
    3:"Buy",
    4:"Exit"
    }

while True:
    try:
        choice=int(input("Enter a number from 1 to 4: "))
        if(choice==1):
            print("Products details are displayed")
            displaying_product()
        elif(choice==2):
            print("please fill up your necessity for selling")
            cont= True
            while cont==True:
                try:
                    id_=int(input("\nEnter ID of product you want to buy: "))
                    line_dict,counting= displaying_product()
                    #calling sell function
                    total_free_items=sell(id_,line_dict,counting,total_free_items,sell_invoice_items)
                except Exception as e:
                    print("Invalid input:",e)
                    break
                # asking for more purchase
                more=input("do you want to buy other thing ?(yes/no): ")
                if(more=="yes"):
                    continue
                elif(more=="no"):
                    invoice=input("Do you want to Generate invoice(yes/no)")
                    if(invoice.lower()=="yes"):
                        invoice1=int(input("Choose 1 for generating buying invoice: "))
                        if(invoice1==1):
                            generate_invoice(sell_invoice_items,total_free_items) # calling buy invoice function
                    elif(invoice.lower()=="no"):
                        print("Returning back...")
                    else:
                        print("sorry, no product left")
                    break
                cont=False
                break
                   
                           
                    
      
        # for restock        
        elif(choice==3):
            print("please fill up your necessity for buying")
            cont=True
            while cont==True:
                try:
                    #asking id of product for restocking the product
                    id_=int(input("\nEnter ID of product you want to buy: "))
                    line_dict,counting= displaying_product()
                    #call buy function
                    buy(id_,line_dict,counting,buy_invoice_items)
                except Exception as e:
                    print("Invalid input:",e)
                    break
                #asking for more sell by user
                more=input("do you want to buy other thing ?(yes/no): ")
                if(more=="yes"):
                    continue
                elif(more=="no"):
                    invoice=input("Do you want to Generate invoice(yes/no)")
                    if(invoice.lower()=="yes"):
                        invoice1=int(input("Choose 2 for generating buying invoice: "))
                        if(invoice1==2):
                            generate_invoice1(buy_invoice_items,total_free_items) # calling buy invoice function
                    elif(invoice.lower()=="no"):
                        print("Returning back...")
                    else:
                        print("input right choice")
                    break
                cont=False
                break
                   
        elif(choice==4):
            print("you are being exit") # exiting from program
            break
        else:
            print("Enter valid choice") #  for invalid id
    except Exception as e:
        print("ERROR:",e)
