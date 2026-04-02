
from calculators.finance import annual_debt_service
from calculators.metrics import noi, annual_cash_flow, cash_on_cash_return, dscr
from calculators.score import deal_score

purchase_price = 300000
down_payment_pct = 20
interest_rate_pct = 7.0
loan_term_years = 30
closing_cost_pct = 3

monthly_rent = 3200
vacancy_rate_pct = 5
taxes_annual = 4200
insurance_annual = 1800
utilities_annual = 1200
repairs_annual = 1500
maintenance_annual = 1500
management_annual = 2400
capex_annual = 1200
other_income_annual = 0
renovation_budget = 5000
value_add_score = 0.8

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

annual_cf = annual_cash_flow(
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
    other_income_annual
)

coc = cash_on_cash_return(
    annual_cf,
    purchase_price,
    down_payment_pct,
    closing_cost_pct,
    renovation_budget
)

my_dscr = dscr(property_noi, debt)

score = deal_score(
    coc_return=coc,
    cap_rate=property_noi / purchase_price,
    dscr=my_dscr,
    rent_to_price_ratio=monthly_rent / purchase_price,
    value_add_score=value_add_score
)

print("NOI:", round(property_noi, 2))
print("Annual Debt Service:", round(debt, 2))
print("Annual Cash Flow:", round(annual_cf, 2))
print("Cash on Cash Return:", round(coc, 4))
print("DSCR:", round(my_dscr, 4))
print("Deal Score:", round(score, 4))


