def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    e = d.removeprefix("£")
    return(float(e))
    print(float(e))


def percent_to_float(p):
    q = p.removesuffix("%")
    q = (float(q))*0.01
    return q

main()
