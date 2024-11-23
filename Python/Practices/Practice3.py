#Thursday, October 03, 2024

'''
Given the sale value of a product, you must calculate the General Sales Tax (GST).
which is 18% and from that, determine the final sale price
'''
#Request the user enter the sale value
salesPrice = float (input( "What is the sale price of the  product: "))
salesPrice = float (salesPrice)

#Determing General Sales Tax (18%)
gst = salesPrice * 0.18

#Determing final value
salesValue = salesPrice + gst

#Output
print (f' Price: {salesPrice:.2f} USD \n Sales Value: {salesValue} USD' )
