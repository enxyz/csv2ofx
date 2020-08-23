from __future__ import (
    absolute_import, division, print_function, unicode_literals)

from operator import itemgetter

# use net amount as current value for portfolio purposes. 

# must be under 32 char
# <BROKERID>d0b51e9846050f97b0902d6f4865fe52</BROKERID>
# <ACCTID>7ff30011960c19a9b5fa0d8fa54b27e6</ACCTID>


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
