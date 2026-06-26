TAX_RATES = {
    "Chico": 0.50,
    "Groucho": 0.70,
    "Harpo": 0.50,
    "Zeppo": 0.40
}


def calculate_tax(amount, province, hour):

    tax_rate = TAX_RATES[province]

    effective_tax = tax_rate * (hour / 24)

    tax_amount = amount * effective_tax

    return amount + tax_amount
