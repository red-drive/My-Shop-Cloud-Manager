# I'm a N00b I have used print instead of logging module.
from flask import Flask
import os
import requests

app = Flask(__name__)

bottoken = os.environ['BOT_TOKEN'] # This gets bot token from heroku

groupid = os.environ['GROUP_ID'] # Enter Channel ID here

P_Sales_Old = 0 # (Sale)For Recording old transaction to compare to next transaction
K_Sales_Old = 0
P_Sales_Return_Old = 0 # (Sales Return)For Recording old transaction to compare to next transaction
K_Sales_Return_Old = 0


@app.route("/")
def hello():
    return "Website is Up and Running"

@app.route("/sales/<salesamount>/<location>")
def sales_happened(salesamount,location):
    global P_Sales_Old,K_Sales_Old
    sale = int(salesamount) # String can't be used to compare with integer
    loc = location
    if location in ["Pulliparakunnu","pulliparakunnu","pulli"]:
        if sale > P_Sales_Old: # This happen when the new sale is higher than old sale
            try:
                requests.get("https://api.telegram.org/bot"+str(bottoken)+"/sendMessage?chat_id="+str(groupid)+"&text=🧾 Sales in Pulliparakunnu \nAmount of Rs. "+str(sale-P_Sales_Old))
            except:
                pass
            P_Sales_Old = sale # Update the new transaction to Sales Old because we need to be updated
        elif sale < P_Sales_Old: # This happens when the old sale is higher than new sale
            print("Sale Deleted : "+str(P_Sales_Old-sale)) # Gives us the difference
            print("Location : "+loc) # This will explain the location thing, where is the f***g shop
            try:
                requests.get("https://api.telegram.org/bot"+str(bottoken)+"/sendMessage?chat_id="+str(groupid)+"&text=❌ Sales Del in Pulliparakunnu \nAmount of Rs. "+str(P_Sales_Old-sale))
            except:
                pass
            P_Sales_Old = sale # Update the new transaction to Sales Old because we need to be updated
    elif location in ["Kalletumkara","kalletumkara","kta"]:
        if sale > K_Sales_Old:  # This happen when the new sale is higher than old sale
            print("Current Sale : " + str(sale - K_Sales_Old))  # Gives us the difference
            print("Location : " + loc)  # This will explain the location thing, where is the f***g shop
            try:
                requests.get("https://api.telegram.org/bot"+str(bottoken)+"/sendMessage?chat_id="+str(groupid)+"&text=🧾Sales in Kalletumkara \nAmount of Rs. " + str(sale - K_Sales_Old))
            except:
                pass
            P_Sales_Old = sale  # Update the new transaction to Sales Old because we need to be updated
        elif sale < K_Sales_Old:  # This happens when the old sale is higher than new sale
            print("Sale Deleted : " + str(K_Sales_Old - sale))  # Gives us the difference
            print("Location : " + loc)  # This will explain the location thing, where is the f***g shop
            try:
                requests.get("https://api.telegram.org/bot"+str(bottoken)+"/sendMessage?chat_id="+str(groupid)+"&text=❌ Sales Del in Kalletumkara \nAmount of Rs." + str(K_Sales_Old - sale))
            except:
                pass
            K_Sales_Old = sale  # Update the new transaction to Sales Old because we need to be updated
    else: # If the updated details are not high and not low and same this will be returned
        print("You in Serious Trouble, lol nothing serious")
    return "Sales Updated"


#  I haven't added guide over here I'm soo lazy.
@app.route("/salesreturn/<salesreturnamount>/<location>")
def sales_return_happened(salesreturnamount,location):
    global P_Sales_Return_Old,K_Sales_Return_Old
    sale_return = int(salesreturnamount)
    loc = location
    if location in ["Pulliparakunnu","pulliparakunnu","pulli"]:
        if sale_return > P_Sales_Return_Old:
            print("Current Sales Return : "+str(sale_return-P_Sales_Return_Old))
            print("Location : "+loc)
            try:
                requests.get("https://api.telegram.org/bot"+str(bottoken)+"/sendMessage?chat_id="+str(groupid)+"&text=🧾Return in Pulliparakunnu \nAmount of Rs. "+str(sale_return-P_Sales_Return_Old))
            except:
                pass
            P_Sales_Return_Old = sale_return
        elif sale_return < P_Sales_Return_Old:
            print("Sales Return Deleted : "+str(P_Sales_Return_Old-sale_return))
            print("Location : "+loc)
            try:
                requests.get("https://api.telegram.org/bot/"+str(bottoken)+"/sendMessage?chat_id="+str(groupid)+"&text=❌ Return in Pulliparakunnu \nAmount of Rs. "+str(P_Sales_Return_Old-sale_return))
            except:
                pass
            P_Sales_Return_Old = sale_return
    elif location in ["Kalletumkara","kalletumkara","kta"]:
        if sale_return > K_Sales_Return_Old:
            print("Current Sales Return : "+str(sale_return-K_Sales_Return_Old))
            print("Location : "+loc)
            try:
                requests.get("https://api.telegram.org/bot"+str(bottoken)+"/sendMessage?chat_id="+str(groupid)+"&text=🧾Return in Kalletumkara \nAmount of Rs. "+str(sale_return-K_Sales_Return_Old))
            except:
                pass
            K_Sales_Return_Old = sale_return
        elif sale_return < K_Sales_Return_Old:
            print("Sales Return Deleted : "+str(K_Sales_Return_Old-sale_return))
            print("Location : "+loc)
            try:
                requests.get("https://api.telegram.org/bot"+str(bottoken)+"/sendMessage?chat_id="+str(groupid)+"&text=❌ Return in Kalletumkara \nAmount of Rs. "+str(K_Sales_Return_Old-sale_return))
            except:
                pass
            K_Sales_Return_Old = sale_return
    else:
        print("You in a serious trouble")
    return("Sales Return Updated")
