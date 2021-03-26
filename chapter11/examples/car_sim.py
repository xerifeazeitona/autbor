"""
Using an Assertion in a Trafﬁc Light Simulation
Say you’re building a trafﬁc light simulation program.
The data structure representing the stoplights at an intersection is a
dictionary with keys 'ns' and 'ew', for the stoplights facing
north-south and east-west, respectively.
The values at these keys will be one of the strings 'green', 'yellow',
or 'red'.
"""
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switch_lights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), f'Neither light is red! {stoplight}'

switch_lights(market_2nd)
