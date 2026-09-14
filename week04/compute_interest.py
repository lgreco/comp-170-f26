
principal_amount = 1_000
interest = 0.09
years_to_invest = 30
# Useless loop to compound interest over the years
for year in range(years_to_invest):
    amount_at_end_of_year = principal_amount * (1+interest)
    principal_amount = amount_at_end_of_year
# Loop is done, let's report the results
print(f"${principal_amount:,.2f}")

