import math


def down_payment_amount(purchase_price, down_payment_pct):
    return purchase_price * (down_payment_pct / 100)


def loan_amount(purchase_price, down_payment_pct):
    return purchase_price - down_payment_amount(purchase_price, down_payment_pct)


def closing_costs(purchase_price, closing_cost_pct):
    return purchase_price * (closing_cost_pct / 100)


def monthly_mortgage_payment(purchase_price, down_payment_pct, interest_rate_pct, loan_term_years):
    loan = loan_amount(purchase_price, down_payment_pct)
    monthly_rate = (interest_rate_pct / 100) / 12
    total_payments = loan_term_years * 12

    if monthly_rate == 0:
        return loan / total_payments

    payment = loan * (
        monthly_rate * (1 + monthly_rate) ** total_payments
    ) / ((1 + monthly_rate) ** total_payments - 1)

    return payment


def annual_debt_service(purchase_price, down_payment_pct, interest_rate_pct, loan_term_years):
    return monthly_mortgage_payment(
        purchase_price,
        down_payment_pct,
        interest_rate_pct,
        loan_term_years
    ) * 12
