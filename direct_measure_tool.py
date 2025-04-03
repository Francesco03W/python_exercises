import math
import decimal

#Todo: Per migliorare uso
# togliere il troncamento dopo la 2a cifra significativa per incertezza
# togliere il troncamento dei decimali della stima al n° di cifre decimali dell'incertezza
# Riscrivere test per le modifiche


def input_values(n):
    """
    User input for list of values used in other functions

    n = number of values
    """
    if not n.isdigit():
        print("Input Error. Not an integer value")
        exit()
        
    n=int(n)

    print("Enter "+str(n)+" values")
    values=[]
    for i in range(n):
        values.append(float(input("Enter value ")))
    return values #returns list of floats
    

def uncertainty_R(nominal_R,tolerance_R):
    """
    Returns the uncertainty (standard deviation) of a measurement
    where average nominal value and percentage of tolerance 
    indicate the measurement interval (on which the 
    distribution is uniform). 2 significant digits are kept.
    B evaluation.
    (Il costruttore ritiene RAGIONEVOLE che il valore di resistenza sia tra
    (-a) - nominale - a. Non avendo altre informazioni assumo la distribuzione come
    uniforme.)

    nominal_R = nominal value of resistance
    tolerance_R = tolerance (%) value of resistance

    #>>> uncertainty_R(1000,1,1)
    5.8
    """
  
    nominal_R=int(nominal_R)
    tolerance_R=int(tolerance_R)
	#uniform distribution:
    a = (nominal_R*tolerance_R)/100
    ##u_R = format(a / math.sqrt(3.0),'.2g')
    u_R = a / math.sqrt(3.0)
    return u_R

def A_evaluation(values,n):
    """
    Returns a tuple with esteemd value and uncertainty of measurement.
    esteemd value is the average of the findings (esteemd expected value)
    uncertainty is esteemd standard deviation of the findings. (esteemd dev)

    values = list of values (float values)
    uncertainty has 2 significant digits
    esteem has many decimals as the uncertainty when the latter has 2 significant digits.
    """
    n=int(n)
    esteem_V=sum(values)/n

    #lista degli scarti quadratici (float)
    sqrt_diff=[]
    for i in range(n):
        sqrt_diff.append((values[i]-esteem_V)**2)
    #u_V=format(math.sqrt((1/(n*(n-1))*(math.fsum(sqrt_diff)))),'.2g') 
    u_V=math.sqrt((1/(n*(n-1))*(math.fsum(sqrt_diff))))

    #rappresento la stima della misura a seconda delle cifre decimali
    # dell'incertezza, una volta fissate le 2 cifre significative.
    #esteem_decimals=abs(decimal.Decimal(u_V).as_tuple().exponent)

    #troncamento della stima secondo i decimali dell'incertezza a 2 cifre sign.
    #esteem_V=format(esteem_V,f'.{esteem_decimals}f')

    return esteem_V,u_V

def correction_accuracy(rng,rng_coeff,rdg,rdg_coeff):
    #return (format((((float(rng_coeff)*float(rng))+(float(rdg_coeff)*float(rdg)))/math.sqrt(3)),'.2g')) 
    return (((float(rng_coeff)*float(rng))+(float(rdg_coeff)*float(rdg)))/math.sqrt(3))
   
if __name__ ==  "__main__":
    import doctest
    print("Measurement Uncertainty Tool")
    text = """
Insert A key - A evaluation of input measure
Insert B key - B evaluation of resistance measure
Insert C key - B evaluation of measurement accuracy
Insert any other key to close the program
"""
    #per chiudere il programma conviene ragionare con logica negata! più elegante
    print(text)
    choice = input("Enter choice: ").lower()

    if choice == 'a':
        num=input("Insert number of readings ")
        values=input_values(num)
        eval_result=A_evaluation(values,num)
        print(f'Esteem: {eval_result[0]} Uncertainty: {eval_result[1]}')
    else:
        if choice == 'b':
           nominal=input("Insert nominal value ")
           tolerance=input("Insert tolerance value (percentage) ")
           eval_result=uncertainty_R(nominal,tolerance)
           print(f'uncertainty: {eval_result}')
        else:
            if choice == 'c':
                rng=input("Insert measurement tool range ")
                rng_coeff=input("Insert rng coefficient ")
                rdg=input("Insert measurement tool reading ")
                rdg_coeff=input("Insert rdg coefficient ")

                #ipotizzo sempre distribuzione uniforme con stima 0
                eval_result=correction_accuracy(rng,rng_coeff,rdg,rdg_coeff)
                print(f'uncertainty: {eval_result}')
            else:
                exit()

