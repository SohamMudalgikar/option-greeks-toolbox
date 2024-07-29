# Option Greeks Toolbox

The Option Greeks Toolbox is a Python module for pricing European options and calculating their Greeks using the Black-Scholes model. The toolbox provides functionality to compute option prices, implied volatility, and the Greeks (Delta, Gamma, Theta, and Vega).

## Features

- Calculate European call and put option prices using the Black-Scholes model
- Calculate implied volatility given the market price of the option
- Calculate the Greeks (Delta, Gamma, Theta, and Vega) for both call and put options


## Usage

### Importing the Toolbox

First, import the `OptionGreeksToolbox` class from the module:

```python
from option_pricing_toolbox import OptionGreeksToolbox
```

### Initializing the Toolbox

Create an instance of the `OptionGreeksToolbox` with the required parameters:

```python
toolbox = OptionGreeksToolbox(spot_price=100, strike_price=100, maturity=1, volatility=0.2, interest_rate=0.05)
```

### Calculating Option Prices

You can calculate the price of a call or put option using the Black-Scholes model:

#### Black-Scholes Formula

For a call option:

$\  C = S \cdot N(d1) - K \cdot e^{-rT} \cdot N(d2) \$

For a put option:
$\  P = K \cdot e^{-rT} \cdot N(-d2) - S \cdot N(-d1) \$

Where:
$\  d1 = \frac{\ln(S/K) + (r + \sigma^2 / 2)T}{\sigma \sqrt{T}} \$
$\  d2 = d1 - \sigma \sqrt{T} \$

```python
call_price = toolbox.calculate_black_scholes_option_price(option_type='call')
put_price = toolbox.calculate_black_scholes_option_price(option_type='put')

print(f"Call Price: {call_price}")
print(f"Put Price: {put_price}")
```

### Calculating Greeks

You can calculate the Greeks for both call and put options:

#### Delta

Delta for a call option:
$\  \Delta_{call} = N(d1) \$

Delta for a put option:
$\  \Delta_{put} = N(d1) - 1 \$

```python
delta_call = toolbox.calculate_delta(option_type='call')
delta_put = toolbox.calculate_delta(option_type='put')

print(f"Delta (Call): {delta_call}")
print(f"Delta (Put): {delta_put}")
```

#### Gamma

Gamma is the same for both call and put options:
$\  \Gamma = \frac{N'(d1)}{S \sigma \sqrt{T}} \$

```python
gamma = toolbox.calculate_gamma()
print(f"Gamma: {gamma}")
```

#### Theta

Theta for a call option:
$\  \Theta_{call} = -\frac{S N'(d1) \sigma}{2 \sqrt{T}} - rK e^{-rT} N(d2) \$

Theta for a put option:
$\  \Theta_{put} = -\frac{S N'(d1) \sigma}{2 \sqrt{T}} + rK e^{-rT} N(-d2) \$

```python
theta_call = toolbox.calculate_theta(option_type='call')
theta_put = toolbox.calculate_theta(option_type='put')

print(f"Theta (Call): {theta_call}")
print(f"Theta (Put): {theta_put}")
```

#### Vega

Vega is the same for both call and put options:
$\  \nu = S \sqrt{T} N'(d1) \$

```python
vega = toolbox.calculate_vega()
print(f"Vega: {vega}")
```

### Calculating Implied Volatility

You can also calculate the implied volatility given the market price of the option:

```python
market_price = 10
implied_volatility = toolbox.calculate_implied_volatility(market_price=market_price, option_type='call')
print(f"Implied Volatility: {implied_volatility}")
```

## Example Script

Here's a complete example script that uses the `OptionGreeksToolbox`:

```python
from option_pricing_toolbox import OptionGreeksToolbox

# Initialize the toolbox with example data
toolbox = OptionGreeksToolbox(spot_price=100, strike_price=100, maturity=1, volatility=0.2, interest_rate=0.05)

# Calculate option prices
call_price = toolbox.calculate_black_scholes_option_price(option_type='call')
put_price = toolbox.calculate_black_scholes_option_price(option_type='put')

print(f"Call Price: {call_price}")
print(f"Put Price: {put_price}")

# Calculate Greeks
delta_call = toolbox.calculate_delta(option_type='call')
delta_put = toolbox.calculate_delta(option_type='put')
gamma = toolbox.calculate_gamma()
theta_call = toolbox.calculate_theta(option_type='call')
theta_put = toolbox.calculate_theta(option_type='put')
vega = toolbox.calculate_vega()

print(f"Delta (Call): {delta_call}")
print(f"Delta (Put): {delta_put}")
print(f"Gamma: {gamma}")
print(f"Theta (Call): {theta_call}")
print(f"Theta (Put): {theta_put}")
print(f"Vega: {vega}")

# Calculate Implied Volatility
market_price = 10
implied_volatility = toolbox.calculate_implied_volatility(market_price=market_price, option_type='call')
print(f"Implied Volatility: {implied_volatility}")
```

## References

1. Black, F., & Scholes, M. (1973). The Pricing of Options and Corporate Liabilities. Journal of Political Economy, 81(3), 637-654.
2. Hull, J. C. (2012). Options, Futures, and Other Derivatives (9th Edition). Pearson.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

