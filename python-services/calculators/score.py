def deal_score(coc_return, cap_rate, dscr, rent_to_price_ratio, value_add_score):
    return (
        (coc_return * 0.40)
        + (cap_rate * 0.25)
        + (dscr * 0.15)
        + (rent_to_price_ratio * 0.10)
        + (value_add_score * 0.10)
    )
