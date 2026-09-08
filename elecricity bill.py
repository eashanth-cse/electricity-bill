def billGenarator(units):

    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + (( units - 100 ) * 7)
    elif units <= 300:
        bill = (100 * 5) + (100 * 7) + (( units - 200 ) * 10)
    else:
        bill = (100 * 5) + (100 * 7) + (100 * 10) + (( units - 300 ) * 15)
    
    return  bill

units = int(input('enter your units:'))

total_bill = billGenarator(units)

print(f'your total bill{units} - {total_bill}/-')
        
