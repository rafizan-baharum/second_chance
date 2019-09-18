from portfolio.models import State, City

# =======================================================================================================================
# CITY AND STATE
# =======================================================================================================================

state = State()
state.code = 'WP'
state.name = 'Wilayah Persekutuan'
state.save()

city = City()
city.code = 'TTDI'
city.name = 'Taman Tun Dr Ismail'
city.state = State.objects.filter(code='WP').first()
city.save()
