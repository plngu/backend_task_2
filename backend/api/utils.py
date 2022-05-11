def calculate_mortgage(deposit, term, price, percent):
    percent_per_month = percent / 100 / 12
    price_wo_deposit = price - deposit
    month = term * 12
    general_interest_rate = (1 + percent_per_month) ** month
    monthly_payment = (price_wo_deposit
                       * percent_per_month
                       * general_interest_rate) / (general_interest_rate - 1)
    return int(monthly_payment)
