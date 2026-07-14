
def calc_pv_values(data):
    try:
        consumption = float(data['elec_consumption'])
        performance = float(data['calc_pv_performance'])
        earning = float(data['spec_pv_earning'])
        self_consumption = float(data['self_consumption']) / 100
        price = float(data['elec_price'])
        feed_in_tariff = float(data['feed_in_tariff'])
        inv_cost = float(data['invest_cost'])
        period = float(data['anal_period'])
    except ValueError:
        return {"error": "Numbers only"}

    earning_year = performance*earning
    self_consumption_kwh  = earning_year*self_consumption
    feed_in_kwh = earning_year - self_consumption_kwh
    safings_self_consumption = self_consumption_kwh * price
    earning_feed_in = feed_in_kwh*feed_in_tariff
    total_earning_year = safings_self_consumption + earning_feed_in
    total_costs = inv_cost*earning_year
    payback_period = -1
    if total_earning_year>0:
        payback_period = total_costs/total_earning_year

    return {
        "earning_year" : round(earning_year),
    "self_consumption_kwh" : round(self_consumption_kwh),
    "feed_in_kwh" : round(feed_in_kwh),
    "safings_self_consumption" : round(safings_self_consumption),
    "earning_feed_in" : round(earning_feed_in),
    "total_earning_year" : round(total_earning_year),
    "total_costs" : round(total_costs),
    "payback_period" : round(payback_period)
    }