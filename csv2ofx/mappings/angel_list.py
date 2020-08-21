from __future__ import (
    absolute_import, division, print_function, unicode_literals)

from operator import itemgetter

# use net amount as current value for portfolio purposes. 
# TODO: use a sale date

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
