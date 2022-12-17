import math

# Function to Calculate Simmple Interest Rate
def simple_interest_rate(amount_paid: float, principle_amount: float, months: int):
    term = months / 12
    interest_paid = amount_paid - principle_amount
    rate = (interest_paid * 100) / (principle_amount * term)
    return rate


# Function to Calculate Loan Emi
def loan_emi(principle_amount: float, annual_rate: float, months: int):
    monthly_rate = annual_rate / 1200
    emi = (principle_amount * monthly_rate * (1 + monthly_rate) ** months) / (
        ((1 + monthly_rate) ** months - 1)
    )
    return emi


def future_sip(
    interval_investment: float, rate_of_return: float, number_of_payments: int
):
    interest = (rate_of_return / 100) / 12
    value = (
        interval_investment
        * ((1 + interest) ** number_of_payments - 1)
        * (1 + interest)
        / interest
    )
    return value


def payback_period(
    years_before_recovery: int, unrecovered_cost: float, cash_flow: float
):
    period = years_before_recovery + (unrecovered_cost / cash_flow)
    return period


# Function to Calculate Compound Intrest
def compound_interest(
    principal_amount: float, intrest_rate: float, years: int, compounding_period: int
):
    amount = principal_amount * (
        pow((1 + (intrest_rate / compounding_period)), (compounding_period * years))
    )
    print(amount)
    return amount


# Function to Calculate Inflation
def inflation(present_amount: float, inflation_rate: float, years: int):
    future_amount = present_amount * (pow((1 + inflation_rate/100), years))
    return future_amount


# Function to Calculate Effective Annual Rate
def effective_annual_rate(annual_interest_rate: float, compounding_period: int):
    EAR = pow((1 + (annual_interest_rate / compounding_period)), compounding_period) - 1
    return EAR


# Function to Calculate Certificate of Deposit (CD)
def certificate_of_deposit(
    principal_amount: float, interest_rate: float, yrs: int, compounding_per_yr: int
):
    cd = principal_amount * (1 + interest_rate / (100 * compounding_per_yr)) ** (
        compounding_per_yr * yrs
    )
    return float(cd)


# Function to Calculate Return on Investment
def return_on_investment(current_value_of_investment: float, cost_of_investment: float):
    roi = (current_value_of_investment - cost_of_investment) / cost_of_investment
    roi*=100
    return roi


# Function to calculate Compounded Annual Growth Rate (CAGR)
def compounded_annual_growth_rate(
    end_investment_value: float, initial_investment_value: float, years: int
):
    n = 1 / years
    cagr = (end_investment_value / initial_investment_value) ** n - 1
    return cagr


# Function to calculate Jensens Alpha
def jensens_alpha(
    return_from_investment: float,
    return_of_appropriate_market_index: float,
    risk_free_rate: float,
    beta: float,
):
    alpha = return_from_investment - (
        risk_free_rate + beta * (return_of_appropriate_market_index - risk_free_rate)
    )
    return alpha


# Function to calculate Weighted Average Cost of Capital (WACC)
def weighted_average_cost_of_capital(
    firm_equity: float,
    firm_debt: float,
    cost_of_equity: float,
    cost_of_debt: float,
    corporate_tax_rate: float,
):
    v = firm_debt + firm_equity
    wacc = (firm_equity * cost_of_equity / v) + (
        firm_debt * cost_of_debt * (1 - corporate_tax_rate) / v
    )
    return wacc


# Function to calculate variance of a two asset portfolio
def asset_portfolio(
    price_A: float,
    price_B: float,
    retrun1: float,
    return2: float,
    standard_dev_A: float,
    standard_dev_B: float,
    stock_correlation: float,
):
    weight_A = price_A / (price_A + price_B)
    weight_B = price_B / (price_A + price_B)
    cov = stock_correlation * standard_dev_A * standard_dev_B
    portfolio_variance = (
        weight_A * weight_A * standard_dev_A * standard_dev_A
        + weight_B * weight_B * standard_dev_B * standard_dev_B
        + 2 * weight_A * weight_B * cov
    )
    return portfolio_variance


# Function to calculate the future price in a put - call parity
def put_call_parity(call_price: float, put_price: float, strike_price: float):
    future_price = call_price + strike_price - put_price
    return future_price


# Function to calculate break even point
def break_even_point(fixed_cost: float, selling_price: float, variable_cost: float):
    contribution_margin = selling_price - variable_cost
    units = fixed_cost // contribution_margin
    rupees = fixed_cost // (contribution_margin / selling_price)
    return units, rupees


# Function to calculate free cash flow to firm
def free_cash_flow_to_firm(
    sales: float,
    operating_cost: float,
    depreciation: float,
    interest: float,
    tax_rate: float,
    fcInv: float,
    wcInv: float,
):
    ebitda = sales - operating_cost
    ebit = ebitda - depreciation
    ebt = ebit - interest
    eat = ebt - ebt / (tax_rate * 0.01)
    wcInv = abs(wcInv)

    return (ebit * (1 - tax_rate * 0.01)) + depreciation - fcInv - wcInv


# Function to calculate the Price-to-Earning ratio (P/E ratio):
def price_to_earning_ratio(share_price: float, earnings_per_share: float):
    p_e_ratio = share_price // earnings_per_share
    return p_e_ratio



# Function to calculate the Dividend yield ratio:
def dividend_yield_ratio(dividend_per_share: float, share_price: float):
    dividend_yield = dividend_per_share // share_price
    return dividend_yield


# Function to calculate the dividend payout ratio
def dividend_payout_ratio(dividend_per_share: float, earnings_per_share: float):
    dividend_payout = dividend_per_share // earnings_per_share
    return dividend_payout


# Function to calculate the debt-to-income ratio (DTI ratio):
def debt_to_income_ratio(annual_income: float, total_debt_per_month: float):
    income_per_month = annual_income / 1200
    DTI = total_debt_per_month // income_per_month
    return DTI


# Function to calculate the Fixed-charge coverage ratio :
def fixed_charge_coverage_ratio(
    earnings_before_interest_taxes: float,
    fixed_charge_before_tax: float,
    interest: float,
):
    a = earnings_before_interest_taxes + fixed_charge_before_tax
    b = interest + fixed_charge_before_tax
    fccr = a // b
    return fccr


# Function to calculate Inventory Shrinkage
def inventory_shrinkage_rate(recorded_inventory: float, actual_inventory: float):
    inventory_shrinkage_rate = (
        recorded_inventory - actual_inventory
    ) / recorded_inventory
    return inventory_shrinkage_rate


# Function to calculate Markup Percentage
def markup_percentage(price: float, cost: float):
    markup_percentage = ((price - cost) / cost) * 100
    return markup_percentage

# Function to calculate Sharpe Ratio
def sharpe_ratio(portfolio_return: float, risk_free_rate: float,standard_deviation_of_portfolio: float):
    sharpe_ratio = (portfolio_return - risk_free_rate)/standard_deviation_of_portfolio
    return sharpe_ratio
    
    
#Function to calculate Purchasing Power
def purchasing_power(initial_amount:float,annual_inflation_rate:float,time:float):
    a= initial_amount* ((100/(100+annual_inflation_rate))**time)
    return a

#Function to create Monthly EMI 
def monthly_emi(loan_amt:float,interest_rate:float,number_of_installments:float):
    emi = loan_amt * interest_rate * ((1+interest_rate)**number_of_installments)/((1+interest_rate)**number_of_installments - 1)
    return emi

#Function to calculate doubling time
def doubling_time(r:float):
    t= math.log(2)/math.log(1+ (r/100))
    return t


#Function to calculate Weighted Average
def weighted_average(ratio:list,rates:list):
    wa=0
    for i in range(len(ratio)):
        wa= wa+ ratio[i]*rates[i]
    # print("Weighted Average returns: ",wa)
    return wa 


# Function to calculate calculate Capital Asset Pricing Model
def Capital_Asset_Pricing_Model(risk_free_interest_rate: float, beta_of_security: float, expected_market_return: float):
    capital_asset_expected_return = risk_free_interest_rate + beta_of_security*(expected_market_return - risk_free_interest_rate)
    return capital_asset_expected_return

#Function to calculate cost of equity:
def cost_of_equity(risk_free_rate_of_return:float,Beta:float,market_rate_of_return:float):
    costOfEquity = risk_free_rate_of_return + Beta *(market_rate_of_return-risk_free_rate_of_return)
    return costOfEquity    

# Function to calculate cost of goods sold
def cost_of_goods_sold(beginning_inventory:float,purchases:float,ending_inventory:float):
    cogs = beginning_inventory + purchases - ending_inventory
    return cogs
# Function to calculate Rule of 72
def rule_of_72(rate_of_roi:float):
    time_period = 72/rate_of_roi
    return time_period

# Function to calculate Acid test ratio
def acid_test_ratio(cash:float,marketable_securitie:float,accounts_receivable:float,current_liabilities:float):
    ratio = (cash + marketable_securitie + accounts_receivable) / current_liabilities
    return round(ratio,2)
# Function to calculate inflation adjusted return
def inflation_adjusted_return(
    beginning_price:float,
    ending_price:float,
    dividends:float,
    beginning_cpi_level:float,
    ending_cpi__level:float
    ):
        stock_return = (ending_price-beginning_price+dividends) / beginning_price
        
        inflation = (ending_cpi__level - beginning_cpi_level) / beginning_cpi_level
        
        inflation_adj = ((1+stock_return)/(1+inflation) -1)*100 
        return round(inflation_adj,2)
# Function to calculate compound annual growth rate
def compound_annual_growth_rate(beginning_value:float,ending_value:float,years:int):
    rate = (pow((beginning_value/ending_value),1/years)-1) * 100
    return round(rate,1)

# Function to calculate current liability coverage ratio
def current_liability_coverage_ratio(net_cash_from_operating_activities: float, total_current_liabilities: float, number_of_liabilities: int):
    average_current_liabilities = total_current_liabilities/number_of_liabilities
    current_liability_coverage_ratio = net_cash_from_operating_activities/average_current_liabilities
    return current_liability_coverage_ratio

#Function to calculate Levered beta:
def levered_beta(unlevered_beta:float,tax_rate:float,debt:float,equity:float):
    l_beta = unlevered_beta*(1+(1-tax_rate)*(debt//equity))
    return l_beta

#Function to calculate Duration With Convexity Adjustment
def duration(rate:float,coupon_rate:float,frequency:float,face_value:float,settlement_date:float,maturity_date:float):
    import numpy as np 
    import pandas as pd 
    try:
        settlement_date=pd.to_datetime(settlement_date,format="%d/%m/%Y")

    except:
        settlement_date=pd.to_datetime(settlement_date,format="%d-%m-%Y")

    try:
        maturity_date=pd.to_datetime(maturity_date,format="%d/%m/%Y")
    except:
        maturity_date=pd.to_datetime(maturity_date,format="%d-%m-%Y")

    data=pd.DataFrame()
    rate=rate/100
    coupon_rate=coupon_rate/100

    n=pd.to_numeric(((pd.to_datetime(maturity_date)-pd.to_datetime(settlement_date))/365).days)
    total_payment=n*frequency
    coupon_payment=coupon/frequency*face_value 
    payment=[coupon_payment]*(total_payment-1)+[coupon_payment+face_value]
    data['period']=pd.DataFrame(np.arange(1,total_payment+1))
    data['payment']=pd.DataFrame(payment)
    data['dcoupon']=data['payment']/((1+rate/frequency)**data['period'])
    data['pv']=data['dcoupon']/frequency*data['period']/data['dcoupon'].sum()
    duration=data['pv'].sum()
    m_duration=duration/(1+rate/frequency)

    factor=1/(data['dcoupon'].sum()*(1+rate/frequency)**2)
    data['cf']=data['dcoupon']*(data['period']**2+data['period'])/(1+rate/frequency)**data['period']
    convexity=factor*data['cf'].sum()
    
    result=round(duration,3)

    return result



# Function to calculate SIP (Systematic Investment Plan)
def calculate_sip(principal, rate, time, frequency):
  si = (principal * rate * time) / 100
  total_invested = frequency * principal
  total_return = si + total_invested
  return total_return

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period: "))
frequency = int(input("Enter the frequency of investment (in months): "))

total_return = calculate_sip(principal, rate, time, frequency)
print(f"Total return on investment: {total_return}")
