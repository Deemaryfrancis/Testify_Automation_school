# Writing  a  well-documented  code  creates  a  function  that calculates simple interest

#Call a SimpleInterest Function

def simpleInterest(Principal, Rate, Time):
    #The Interest accured in 5years
    interest = (Principal * Rate * Time) / 100

    #Total amount accured in 5years
    TotalAmount = Principal + ((Principal * Rate * Time) / 100)

    print("Interest = ", interest)
    print("Total Amount accrued = ", TotalAmount)
    return (TotalAmount, interest)

simpleInterest(5000,50,5)

