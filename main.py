from flask import Flask

app = Flask(__name__)

Sales_Old = 0
Sales_Return_Old = 0

@app.route("/sales/<salesamount>/<location>")
def sales_happened(salesamount,location):
    global Sales_Old
    sale = int(salesamount)
    loc = location
    if sale > Sales_Old:
        print("Current Sale : "+str(sale-Sales_Old))
        print("Location : "+loc)
        Sales_Old = sale
    elif sale < Sales_Old:
        print("Sale Deleted : "+str(Sales_Old-sale))
        print("Location : "+loc)
        Sales_Old = sale
    else:
        print("You in Serious Trouble")
    return "Sales Updated"


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