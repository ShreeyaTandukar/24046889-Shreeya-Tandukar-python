import random
import datetime
#updating detail of product in file product.txt using function
def updated_product(line_dict):
    #docstring
    """
    for updating the txt file named product with current product details
    Args:
        line_duct with datatype dict is used to store updated product details
    returns:
        None
    """
    try:
        file=open("product.txt","w")
        ''' looping by the help of line_dict which is being use for storing product detail.
            for each product here comma is used for joining product's detail '''
        for products in line_dict:
           product1=line_dict[products]
           update=",".join(product1) #joining the product details with comma
           file.write(update)# writing updated information of product to file
        file.close()#closing file
    except FileNotFoundError:
        print("Error: The text file named 'product.txt' was not found")# printing exception if file is not found
    except Exception as e:
        print("Error in updating products:",e)#printing exception if updation goes wrong

'''function used to calculate the Vat on product based on its price and quantity
along with computing price before VAT, calculating vat amount
and returns the total price including VAT'''
def calculate_vat(per_unit_price,quantity):
    #docstring
    """
    VAT, VAT amount, and total price including vat is used for calculation
    Args:
        per_unit_price with int datatype is used for storing price of one unit
        Quantity with int datatype is used to store number of units
    Returns:
        tuple of total_price_with_vat, vat_amount, price_before_vat
    """
    try:
        rate_of_vat=0.13 #assigning vat rate
        before_vat=per_unit_price*quantity #calculating price before VAT
        vat=before_vat* rate_of_vat #Calculate VAT
        total_price=before_vat+vat # Calculate total price including VAT
        return total_price,vat,before_vat # returning total price,VAT and price before VAT
    except Exception as e:
        print("Error in calculating vat: ",e) #Printing exception if any calculation error occurs
        return 0,0,0 # returning 0,0,0 if any calculation error occurs
# defining options for generating invoiced    
options1={
    1:"Sell Invoice",
    2:"Buy Invoice"
}
# function for generating selling invoice
def generate_invoice(items,total_free_items):
    #docstring
    """
    for generating customer sell invoice and writing in sell_invoice txt file
    Args:
        items with list datatype is used to list dictionaries having details on sold product
        total_free_items with int datatype is used for totaling number of free items given to customer
    Returns:
        None
    """
    '''this function helps in generating a sell invoice for the customer
    and takes a list of items that are sold as wellas generates an invoice number
    and writes the invoice details to file name sell_invoice.txt '''
    try:
        name=input("Enter your name") #asking the user for their name
        print("-"*82)
        random_num=random.randint(1,100) # for generating random invoice number
        a="WeCare" # for storing name
        date_time=str(datetime.datetime.now().year)+"/"+str(datetime.datetime.now().month)+"/"+str(datetime.datetime.now().day) # for getting current date
        
        # PREPARING INVOICE STRUCTURE
        invoice_lines=[
            "------------------------------------------------------------------------------------------------------------------\n"
            "\t\t\t Invoice",
            "\t\t\t######" + str(random_num)+"######",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
            "\t\t\t"+a,
            "Date: "+date_time+"\n",
            "Customer's Name: "+name+"\n",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            "\tS.N \tProduct Name       \tBrand     \tQuantity    \tPrice\n",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        ]
        final=0
        # looping using items and adding details to the invoice
        SN=1
        for product1 in items:
            free_items=product1["free"]  # for getting number of free items
            final+=product1["total1"]    # for suming total without free items
            invoice_lines.append(
                "\n"+"\t"+str(SN)+
                "\t"+product1["product_name"]+
                "\t\t"+product1["brand"]+
                "\t"+str(product1["quantity"])+
                "\t   "+str(product1["total1"])
                )
            SN+=1    #adding product name to invoice
            
        invoice_lines.append("-"*85)
        invoice_lines.append("\nTotal Amount is: "+str(final)) # for grand total if multiple items are sold
        invoice_lines.append("-"*85)

                                 
        invoice_lines.append("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        invoice_lines.append("\n\t\t Thank you for purchasing\n")
        invoice_lines.append("\t Congratulation! You got "+str(total_free_items)+"free items\n")
        invoice_lines.append("------------------------------------------------------------------------------------------------------")
        
        # writing selling details in sell_invoice.txt
        file=open("sell_invoice.txt","a")
        #using for loop for writing detail of each line in file and appending a new line
        for lines in invoice_lines:
            file.write(lines+"\n")
        file.close() # closing the write file
        #using for loop for storing each line detail in invoice_lines list and printing it to console
        for lines in invoice_lines:
            print(lines)
        print("invoice generated")
        return
    except FileNotFoundError:
        print("the file coundnot be found")# thorwing message when  no file exception occurs
    except Exception as e:
        print("Found error in generating Invoice: ",e)# throwing message when invoice could not be generated

    
#function for generating buy invoice
def generate_invoice1(items,total_free_items):
    #docstring
    """
    for generating supplier buy invoice and writing in buy_invoice txt file
    Args:
        items with list datatype is used to list dictionaries having details on purchased product
    Returns:
        None
    """

    
    
    ''' here this function is used for generating buy invoice for restocking products in store
        this also takes a list of purchased items and adds vat as well as write the purchase
        in buy_invoice.txt'''
    try:
        name=input("Enter your name")  # for suppiler name
        print("-"*82)
        random_num=random.randint(1,100)  #for generating random invoice number
        a="WeCare"  # for storing name
        date_time=str(datetime.datetime.now().year)+"/"+str(datetime.datetime.now().month)+"/"+str(datetime.datetime.now().day)  # for getting current date
        rate_of_vat=0.13 # for vat
         # PREPARING INVOICE STRUCTURE
        invoice_lines=[
            "--------------------------------------------------------------------------------------------------------\n"
            "\t\t\t Invoice",
            "\t\t\t######" + str(random_num)+"######",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
            "\t\t\t"+a,
            "Date: "+date_time+"\n",
            "Supplier's Name: "+name+"\n",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            "\tS.N. \tProduct Name      \tBrand     \tQuantity   \tPrice",
        ]
        ''' here final total amount is initialize with 0 and is being iterating through
            each products in the item list as well as extract qantity,price and free items
            then calculating Vat, total price and add it to the final total.
            also append each product detail to invoice '''
        final=0
        SN1=1
        for product1 in items:
            quantity=product1["quantity"] # for quantity being purchased
            per_unit_price=product1["unit_price"] # for per unit price
            free_items=product1["free"] # free items given if given any
            total_price,vat,before_vat=calculate_vat(per_unit_price,quantity) # for calculating total with Vat
            final+=total_price # adding price details to invoice
            #adding individual product details to invoice
            invoice_lines.append(
                "\n"+"\t"+str(SN1)+
                "\t"+product1["product_name"]+
                "\t\t"+product1["brand"]+
                "\t "+str(product1["quantity"])+
                "\t        "+str(total_price)+"\n"
                )
            SN1+=1
            
        invoice_lines.append("-"*90)   
        invoice_lines.append(" Vat Rate: "+str(rate_of_vat)+"\n")
        invoice_lines.append(" Vat Amount: "+str(vat)+"\n")

        

        invoice_lines.append("-"*90)
    
        invoice_lines.append("\nTotal Amount is: "+str(final))
   
        invoice_lines.append("-"*90)

                                 
        invoice_lines.append("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        invoice_lines.append("\n\t\t You got your product restored\n")
        #invoice_lines.append("\t Congratulation! You got "+str(free_items)+"free items\n")
        invoice_lines.append("----------------------------------------------")
        
        file=open("buy_invoice.txt","a")
        #using for loop for storing each line detail in invoice_lines list and printing it to text file

        for lines in invoice_lines:
            file.write(lines+"\n")
        file.close()
        #using for loop for storing each line detail in invoice_lines list and printing it to console

        for lines in invoice_lines:
            print(lines)
        print("invoice generated")
    except FileNotFoundError:
        print("the file coundnot be found")#thorwing message when  no file exception occurs
    except Exception as e:
        print("Found error in generating Invoice: ",e)
