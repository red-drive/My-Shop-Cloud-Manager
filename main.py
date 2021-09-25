# I'm a N00b I have used print instead of logging module.
from flask import Flask

app = Flask(__name__)

Sales_Old = 0 # (Sale)For Recording old transaction to compare to next transaction
Sales_Return_Old = 0 # (Sales Return)For Recording old transaction to compare to next transaction

@app.route("/sales/<salesamount>/<location>") 
def sales_happened(salesamount,location):
    global Sales_Old
    sale = int(salesamount) # String can't be used to compare with integer
    loc = location
    if sale > Sales_Old: # This happen when the new sale is higher than old sale
        print("Current Sale : "+str(sale-Sales_Old)) # Gives us the difference
        print("Location : "+loc) # This will explain the location thing, where is the f***g shop
        Sales_Old = sale # Update the new transaction to Sales Old because we need to be updated
    elif sale < Sales_Old: # This happens when the old sale is higher than new sale
        print("Sale Deleted : "+str(Sales_Old-sale)) # Gives us the difference
        print("Location : "+loc) # This will explain the location thing, where is the f***g shop
        Sales_Old = sale # Update the new transaction to Sales Old because we need to be updated
    else: # If the updated details are not high and not low and same this will be returned
        print("You in Serious Trouble, lol nothing serious")
    return "Sales Updated"


#  I haven't added guide over here I'm soo lazy.
@app.route("/salesreturn/<salesreturnamount>/<location>")
def sales_return_happened(salesreturnamount,location):
    global Sales_Return_Old
    sale_return = int(salesreturnamount)
    loc = location
    if sale_return > Sales_Return_Old:
        print("Current Sales Return : "+str(sale_return-Sales_Return_Old))
        print("Location : "+loc)
        Sales_Return_Old = sale_return
    elif sale_return < Sales_Return_Old:
        print("Sales Return Deleted : "+str(Sales_Return_Old-sale_return))
        print("Location : "+loc)
        Sales_Return_Old = sale_return
    else:
        print("You in a serious trouble")
    return("Sales Return Updated")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5500)