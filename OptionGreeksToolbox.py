import numpy as np
from scipy.stats import norm
from scipy.optimize import newton

class OptionGreeksToolbox:
    """
    A toolbox for option pricing and Greeks calculation using the Black-Scholes model.

    Attributes:
        S (float): Spot price of the underlying asset.
        K (float): Strike price of the option.
        T (float): Time to maturity of the option in years.
        sigma (float): Volatility of the underlying asset.
        r (float): Risk-free interest rate.
    """

    def __init__(self, spot_price, strike_price, maturity, volatility, interest_rate):
        """
        Initializes the OptionGreeksToolbox with the given parameters.

        Args:
            spot_price (float): Spot price of the underlying asset.
            strike_price (float): Strike price of the option.
            maturity (float): Time to maturity of the option in years.
            volatility (float): Volatility of the underlying asset.
            interest_rate (float): Risk-free interest rate.
        """
        self.S = spot_price
        self.K = strike_price
        self.T = maturity
        self.sigma = volatility
        self.r = interest_rate

    def black_scholes_european_call(self, S=None, T=None, sigma=None):
        """
        Calculates the European call option price using the Black-Scholes formula.

        Args:
            S (float, optional): Spot price of the underlying asset. Defaults to self.S.
            T (float, optional): Time to maturity of the option. Defaults to self.T.
            sigma (float, optional): Volatility of the underlying asset. Defaults to self.sigma.

        Returns:
            float: European call option price.
        """
        S = S if S is not None else self.S
        T = T if T is not None else self.T
        sigma = sigma if sigma is not None else self.sigma
        
        d1 = (np.log(S / self.K) + (self.r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        call_price = S * norm.cdf(d1) - self.K * np.exp(-self.r * T) * norm.cdf(d2)
        return call_price

    def black_scholes_european_put(self, S=None, T=None, sigma=None):
        """
        Calculates the European put option price using the Black-Scholes formula.

        Args:
            S (float, optional): Spot price of the underlying asset. Defaults to self.S.
            T (float, optional): Time to maturity of the option. Defaults to self.T.
            sigma (float, optional): Volatility of the underlying asset. Defaults to self.sigma.

        Returns:
            float: European put option price.
        """
        S = S if S is not None else self.S
        T = T if T is not None else self.T
        sigma = sigma if sigma is not None else self.sigma
        
        d1 = (np.log(S / self.K) + (self.r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        put_price = self.K * np.exp(-self.r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        return put_price

    def calculate_black_scholes_option_price(self, option_type='call'):
        """
        Calculates the Black-Scholes option price.

        Args:
            option_type (str): Type of the option, 'call' or 'put'. Defaults to 'call'.

        Returns:
            float: Black-Scholes option price.
        """
        if option_type == 'call':
            return self.black_scholes_european_call()
        elif option_type == 'put':
            return self.black_scholes_european_put()
        else:
            raise ValueError("Invalid option type. Use 'call' or 'put'.")

    def calculate_implied_volatility(self, market_price, option_type='call'):
        """
        Calculates the implied volatility given the market price of the option.

        Args:
            market_price (float): Market price of the option.
            option_type (str): Type of the option, 'call' or 'put'. Defaults to 'call'.

        Returns:
            float: Implied volatility.
        """
        def implied_volatility_func(sigma):
            if option_type == 'call':
                return self.black_scholes_european_call(sigma=sigma) - market_price
            elif option_type == 'put':
                return self.black_scholes_european_put(sigma=sigma) - market_price

        implied_volatility = newton(implied_volatility_func, x0=0.2)
        return implied_volatility

    def calculate_delta(self, option_type='call'):
        """
        Calculates the Delta of the option.

        Args:
            option_type (str): Type of the option, 'call' or 'put'. Defaults to 'call'.

        Returns:
            float: Delta of the option.
        """
        epsilon = 0.001
        if option_type == 'call':
            delta = (self.black_scholes_european_call(S=self.S + epsilon) - self.black_scholes_european_call(S=self.S)) / epsilon
        elif option_type == 'put':
            delta = (self.black_scholes_european_put(S=self.S + epsilon) - self.black_scholes_european_put(S=self.S)) / epsilon
        else:
            raise ValueError("Invalid option type. Use 'call' or 'put'.")
        return delta

    def calculate_gamma(self):
        """
        Calculates the Gamma of the option.

        Returns:
            float: Gamma of the option.
        """
        epsilon = 0.001
        gamma = ((self.black_scholes_european_call(S=self.S + epsilon) - 2 * self.black_scholes_european_call(S=self.S) + 
                  self.black_scholes_european_call(S=self.S - epsilon)) / epsilon ** 2)
        return gamma

    def calculate_theta(self, option_type='call'):
        """
        Calculates the Theta of the option.

        Args:
            option_type (str): Type of the option, 'call' or 'put'. Defaults to 'call'.

        Returns:
            float: Theta of the option.
        """
        if option_type == 'call':
            theta = (self.black_scholes_european_call(T=self.T - 1/252) - self.black_scholes_european_call(T=self.T)) / (1/252)
        elif option_type == 'put':
            theta = (self.black_scholes_european_put(T=self.T - 1/252) - self.black_scholes_european_put(T=self.T)) / (1/252)
        else:
            raise ValueError("Invalid option type. Use 'call' or 'put'.")
        return theta

    def calculate_vega(self):
        """
        Calculates the Vega of the option.

        Returns:
            float: Vega of the option.
        """
        epsilon = 0.001
        vega = (self.black_scholes_european_call(sigma=self.sigma + epsilon) - 
                self.black_scholes_european_call(sigma=self.sigma)) / epsilon
        return vega

