#
#   Sample sundries store
#

from ast import Continue
from doctest import testfile


def main():
    # Declare variables
    boolSelection = True
    
    consItemPrice1 = 5.50
    consItemPrice2 = 6.00
    consItemPrice3 = 6.50

    varItemPrice = 0.00

    varItemQuantity1 = 0
    varItemQuantity2 = 0
    varItemQuantity3 = 0

    varItemQuantity = 0

    varSubTotal1 = 0.00
    varSubTotal2 = 0.00
    varSubTotal3 = 0.00

    varTotalAmtDue = 0.00

    # Start Item Selection
    while boolSelection:

        boolInputContinue = True
        boolInputQuantity = True

        # Accept item selection
        inputSelection = input("Please select one of the following items:\n1 - Pencil - 5.50\n2 - Pen - 6.00\n3 - Paper - 6.50\n")
        match inputSelection:
            case "1":
                varItemPrice = consItemPrice1
            case "2":
                varItemPrice = consItemPrice2
            case "3":
                varItemPrice = consItemPrice3
            case _:
                print("Please enter 1, 2 or 3.\n")
                boolInputContinue = False
                boolInputQuantity = False

        # Accept quantity
        while boolInputQuantity:
            inputQuantity = input("How many of this item do you wish to buy?\n")
            testInputQuantity = int(inputQuantity)
            boolInputQuantity = testInputQuantity.__int__
            
            if boolInputQuantity:
                varItemQuantity  = testInputQuantity
                boolInputQuantity = False
            else:
                print("Please enter a number:\n")
                boolInputContinue = False

        # Calculate subtotal
        varTotalAmtDue = varTotalAmtDue + (varItemQuantity * varItemPrice)
        
        while boolInputContinue:
            inputContinue = input("Do you still want to add another item? Y/N\n")
            if inputContinue == "N" or inputContinue == "n":
                boolInputContinue = False
                boolSelection = False
            elif inputContinue == "Y" or inputContinue == "y":
                boolInputContinue = False
            else:
                print("Please enter Y or N.\n")
                Continue

    # Print Totals here
    print("Your total amount due is", varTotalAmtDue,"\n")

    # Accept Payment
    boolLoopPayment = True

    while boolLoopPayment:
            inputPayment = input("How much is your payment?\n")
            testFloatPayment = float(inputPayment)
            boolInputPayment = testFloatPayment.__float__
            
            if boolInputPayment:
                if testFloatPayment == varTotalAmtDue:
                    print("I receive exact amount.\nThank you for shopping with us.")
                    boolLoopPayment = False
                elif testFloatPayment > varTotalAmtDue:
                    print("I receive,", testFloatPayment, ".\nYour change is", testFloatPayment - varTotalAmtDue, "\nThank you for shopping with us.")
                    boolLoopPayment = False    
                else:
                    print("Entered amount does not cover the cost of the items.\nPlease enter an amount greater than or equal to the amount due.\n")
                
            else:
                print("Please enter an amount:\n")
                
if __name__ == "__main__":
    main()