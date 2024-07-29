from option_pricing_toolbox import OptionPricingToolbox

# Initialize the toolbox with example data
toolbox = OptionPricingToolbox(spot_price=100, strike_price=100, maturity=1, volatility=0.2, interest_rate=0.05)

# Calculate option prices
call_price = toolbox.calculate_black_scholes_option_price(option_type='call')
put_price = toolbox.calculate_black_scholes_option_price(option_type='put')

print(f"Call Price: {call_price}")
print(f"Put Price: {put_price}")

# Calculate Greeks
delta_call = toolbox.calculate_delta(option_type='call')
gamma = toolbox.calculate_gamma()
theta_call = toolbox.calculate_theta(option_type='call')
vega = toolbox.calculate_vega()

print(f"Delta (Call): {delta_call}")
print(f"Gamma: {gamma}")
print(f"Theta (Call): {theta_call}")
print(f"Vega: {vega}")
