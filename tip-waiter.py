def total_calc(bill_amount,tip_perc):
    total=bill_amount*(1+0.01*tip_perc)
    total=round(total,2)
    print("Please pay,", total)
bill_amount=int(input("Please enter the bill amount: "))
tip_perc=int(input("Please enter the percentage of the bill you want to tip: "))
total_calc(bill_amount,tip_perc)
