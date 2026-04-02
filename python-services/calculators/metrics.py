from calculators.finance import annual_debt_service

def annual_gross_rent(monthly_rent):
    return monthly_rent * 12


def effective_gross_income(monthly_rent, vacancy_rate_pct, other_income_annual=0):
    gross_rent = annual_gross_rent(monthly_rent)
    vacancy_loss = gross_rent * (vacancy_rate_pct / 100)
    return gross_rent - vacancy_loss + other_income_annual


def noi(
    monthly_rent,
    vacancy_rate_pct,
    taxes_annual,
    insurance_annual,
    utilities_annual,
    repairs_annual,
    maintenance_annual,
    management_annual,
    capex_annual,
    other_income_annual=0
):
    egi = effective_gross_income(monthly_rent, vacancy_rate_pct, other_income_annual)

    operating_expenses = (
        taxes_annual
        + insurance_annual
        + utilities_annual
        + repairs_annual
        + maintenance_annual
        + management_annual
        + capex_annual
    )

    return egi - operating_expenses


def annual_cash_flow(
    purchase_price,
    down_payment_pct,
    interest_rate_pct,
    loan_term_years,
    monthly_rent,
    vacancy_rate_pct,
    taxes_annual,
    insurance_annual,
    utilities_annual,
    repairs_annual,
    maintenance_annual,
    management_annual,
    capex_annual,
    other_income_annual=0
):
    property_noi = noi(
        monthly_rent,
        vacancy_rate_pct,
        taxes_annual,
        insurance_annual,
        utilities_annual,
        repairs_annual,
        maintenance_annual,
        management_annual,
        capex_annual,
        other_income_annual
    )

    debt = annual_debt_service(
        purchase_price,
        down_payment_pct,
        interest_rate_pct,
        loan_term_years
    )

    return property_noi - debt


def monthly_cash_flow(*args, **kwargs):
    return annual_cash_flow(*args, **kwargs) / 12


def cap_rate(property_noi, purchase_price):
    return property_noi / purchase_price


def cash_on_cash_return(
    annual_cashflow,
    purchase_price,
    down_payment_pct,
    closing_cost_pct,
    renovation_budget=0
):
    down_payment = purchase_price * (down_payment_pct / 100)
    closing_costs = purchase_price * (closing_cost_pct / 100)
    total_cash_invested = down_payment + closing_costs + renovation_budget

    if total_cash_invested == 0:
        return 0

    return annual_cashflow / total_cash_invested


def dscr(property_noi, annual_debt):
    if annual_debt == 0:
        return 0
    return property_noi / annual_debt


def rent_to_price_ratio(monthly_rent, purchase_price):
    if purchase_price == 0:
        return 0
    return monthly_rent / purchase_price
