from write import updated_product,calculate_vat
from read import displaying_product

def sell(id_ , line_dict, counting,total_free_items,sell_invoice_items):
    """
    for handling the sale of a product by a customer.
    Args:
        id_having datatype int and is used as id of product to sell
        line_dict with data structure dict and is used to store product details in it
        counting with datatype int which is used to total number of product in it
        total_free_items with datatype int which is used for counting total number of free item given
        sell_invoice_items with datatype list which is used to list stored sold item details for invoice
    Returns:
        with datatype int total number of free items after the sale is updated
    """

    if(id_ <= counting and id_!=0):
        try:
            quantity=int(input("\n Enter quantity of the product as 1,2,3...:"))
            # checking if quantity entered is valid or not
            if(quantity <=0):
                print("quantity must be greater then 0")
                return total_free_items
            #getting available quantity from the product dictionary
            quantity_remain=int(line_dict[id_][2])
            # if quantity is sufficient
            if(quantity<=quantity_remain and quantity>=0):
                print("you can continue your transaction")
                free=quantity//3 # calculating free products using buy 3 get 1 free offer
                total=quantity+free
                total_free_items+=free
                print("you got ",free,"products free")
                print("the product given:",str(total))
                #updating the product stock
                line_dict[id_][2]=str(quantity_remain-quantity)
                # price is doubled for unit price
                per_unit_price1=int(line_dict[id_][3])*2
                # product is updated in file or storage
                updated_product(line_dict)
                # appending
                sell_invoice_items.append({
                    "product_name":line_dict[id_][0],
                    "brand":line_dict[id_][1],
                    "quantity":total,
                    "free":free,
                    "unit_price":per_unit_price1,
                    "total1":per_unit_price1*quantity
                    })
            # if quantity is more than quantity remain then adjustment is done 
            elif(quantity>=quantity_remain and quantity_remain>0):
                    print("Only",quantity_remain,"products available.adjusting your order...")
                    free=quantity//3
                    total=quantity+free
                    total_free_items+=free
                    print("you got ",free,"products free")
                    print("the product given:",str(total))
                    # setting remaining quantity to zero as all stock are used
                    line_dict[id_][2]="0"
                    per_unit_price1=int(line_dict[id_][3])*2
                    #update and display products
                    updated_product(line_dict)
                    displaying_product()
                    #append
                    sell_invoice_items.append({
                        "product_name":line_dict[id_][0],
                        "brand":line_dict[id_][1],
                        "quantity":total,
                        "free":free,
                        "unit_price":per_unit_price1,
                        "total1":per_unit_price1*quantity
                        })
                    return total_free_items
            else:
                print("Sorry, there are no product left")
        except Exception as e:
            print("Invalid number of quantity: ",e)
    else:
        print("Invalid Id")# handling invalid menu input
    return total_free_items
            
def buy(id_ , line_dict, counting,buy_invoice_items):
    """
    for handling the sale of a product by a supplier.
    Args:
        id_having datatype int and is used as id of product to restock
        line_dict with data structure dict and is used to store product details in it
        counting with datatype int which is used to total number of product in it
        buy_invoice_items with datatype list which is used to list stored bought item details for invoice
    Returns:
       no

    """
    
    # checking if id entered is valid or not
    if(id_ <= counting and id_!=0):
        try:
            # for quantity of product restocking
            quantity=int(input("\n Enter quantity of products as 1,2,3... you want to add: "))
            if(quantity <=0):
                print("quantity must be greater then 0")
                return 
            quantity_added=int(line_dict[id_][2]) # assiging variable quantity
            per_unit_price=int(line_dict[id_][3])   #assinging variavle price part
            # calculating vat, total price and price before Vat
            total_price,vat,before_vat=calculate_vat(per_unit_price,quantity)
            #displaying price
            print("price before vat:",before_vat)
            print("Vat amount:",vat)
            print("total price is: ",total_price)
            #updating the quantity in the product list
            line_dict[id_][2]=str(quantity_added+quantity)
            print("product added sucessfully")
            updated_product(line_dict) # saving the updated detail in file
            #adiing detials to invoice
            buy_invoice_items.append({
                "product_name":line_dict[id_][0],
                "brand":line_dict[id_][1],
                "quantity":quantity,
                "unit_price":per_unit_price,
                "total1":per_unit_price*quantity,
                "free":0
                })
        except Exception as e:
            print("Invalid number of quantity: ",e)
    else:
        print("Invalid Id")# handling invalid menu input
