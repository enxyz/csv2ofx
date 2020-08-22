from __future__ import (
    absolute_import, division, print_function, unicode_literals)

from operator import itemgetter

# use net amount as current value for portfolio purposes. 
# TODO: use a sale date

# needs to go in header under <SONRS> 
            # <FI>
			# 	<ORG>3000</ORG>
			# </FI>
			# <INTU.BID>3000</INTU.BID>

#needs SECLIST!

# must be under 32 char
# <BROKERID>d0b51e9846050f97b0902d6f4865fe52</BROKERID>
# <ACCTID>7ff30011960c19a9b5fa0d8fa54b27e6</ACCTID>

# if there is no sell, need to show item exists in portfolio
# and have current value?
# => using a sell for yesterday for net amount seems like the way to go

mapping = {
    'has_header': True,
    'delimiter': ',',
    'bank': 'Angel List',
    'is_investment': True,
    'currency': 'USD',
    'account': itemgetter('Investment Entity'),
    'date': itemgetter('Invest Date'),
    'amount': itemgetter('Invested'),
    'payee': itemgetter('Company/Fund'),
    'notes': itemgetter('Round'),
    'type': 'Buy',
}
