import random
import datetime
#reading txt file from product.txt
''' function for reading file ,parsing the product details
and displaying them in good table format along with using dictionary to store each products detail
and assigning Id to each product'''
def displaying_product():
    """
    for reading and displaying product details from txt file named product in proper format
    Returns:
        tuples:
            line_dict with datatype dict is used for tracing id to the field
            counting with int datatype is used for totaling number of product with increasement in Id
    """
    '''line_dict={}
    counting=1
    '''
    
    
    try:
        file=open("product.txt","r")#opening file in read mode
        lines=file.readlines()#reading the each line from  file content and put it on list 
        file.close() #closing the file

        #for header
        print("-"*82)
        print("|ID|\t|ProductName|\t  |Brand|\t|Quantity|\t|CP|\t|SP|\t|Origin|")
        print("-"*82)
        #dictionary to store each product's detail
        line_dict={}
        counting=1# for starting with id 1

        #looping each line
        for line in lines:
            fields=line.split(",")#spliting the line by commas
            line_dict[counting]=fields# storing counting as key in dictionary
            print(counting,end="\t")# for printing ID

            #index for knowing on which field we are in
            i=0
            for field in fields:
                if i==3:
                    quantity=int(field)
                    price=quantity*2
                    print("\t",field,end="\t")
                    print(price,end="\t")
            
                elif i==1:
                    #asumming field to be productname with spacing
                    print(field,end="\t ")
    
                else:
                    #for other fields with proper spacing
                    print(field,end="\t ")
                i=i+1# moving to next column
    
            print()#moving to next line for next products
            counting=counting+1#moving to next id
        print("-"*82)#printing footer
    except FileNotFoundError:
        print("Error: The text file named 'product.txt' was not found")
    except Exception as e:
        print("Error in displaying products:",e)
    return line_dict,counting
