from django.test import TestCase
from lipisha import Lipisha

# Create your tests here.
LIPISHA_API_KEY = "d727744fb1ebc29ce87018212e4b4f70"
LIPISHA_API_SIGNATURE = "CXlGBfUzTY3Zk47UBZCa/fn7X4AZlVcXprN2MmsL3AcmMhV0r9rBI7o31jf/eLyX8RsG6eAgOwaEjEizJujH69d9j+ysTyU7VtJ97jriI3KNHRdmYVQIyM9joc3gslWBzNDZ7giwEreWOvhxiFnVyKGGMnbr1YVDSnmvDUnI/ks="
lipisha = Lipisha(LIPISHA_API_KEY, LIPISHA_API_SIGNATURE, api_environment='test')
ACC_NO = '01996'

class MPESATest(TestCase):
	def setUp(self):
		self.mpesa_kwargs = dict(
			account_number=ACC_NO,
			mobile_number='0702495084',
			reference='HSUIDH63GJ238',
			amount='1000',
			method='Paybill (M-Pesa)'
			)
	def test_mpesa_pay(self):
		result = lipisha._make_api_call(
			api_method='request_money',
			**self.mpesa_kwargs
			)
		print result


class CreditCardTest(TestCase):
	def setUp(self):
		self.credit_kwargs = dict(
			account_number=ACC_NO,
			card_number='4242424242424242',
			address1='1000',
			expiry='082020',
			name='dfd',
			country='Nyeri',
			state='asda',
			zip='123234',
			amount='1000',
			currency='KES',
			security_code='1218'
			)
		self.settle_kwargs=dict(
			account_number=ACC_NO,
			amount='1000'
			)

	def test_credit_card_auth(self):
		"""Authorize credit card usage"""
		result = lipisha._make_api_call(
			api_method='authorize_card_transaction',
			**self.credit_kwargs
			)
		results = {
			'transaction_reference': result['content']['transaction_reference'],
			'transaction_index': result['content']['transaction_index'],
		}
		self.credit_card_complete(results)
		# self.credit_card_reverse(results)

	def credit_card_complete(self, kwargs):
		"""Complete credit card transaction"""
		result = lipisha._make_api_call(
			api_method='complete_card_transaction',
			**kwargs
			)
		print result
		# print self.credit_card_request_settlement(**self.settle_kwargs)

	def credit_card_reverse(self, kwargs):
		"""Reverse credit card transaction"""
		result = lipisha._make_api_call(
			api_method='reverse_card_authorization',
			**kwargs
			)
		return result

	def credit_card_request_settlement(self, kwargs):
		result = lipisha._make_api_call(
			api_method='request_settlement',
			**kwargs
			)
		print result
		return result