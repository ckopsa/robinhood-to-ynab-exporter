# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.bulk_transactions import BulkTransactions  # noqa: E501
from openapi_client.rest import ApiException

class TestBulkTransactions(unittest.TestCase):
    """BulkTransactions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BulkTransactions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.bulk_transactions.BulkTransactions()  # noqa: E501
        if include_optional :
            return BulkTransactions(
                transactions = [
                    openapi_client.models.save_transaction.SaveTransaction(
                        account_id = '0', 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        amount = 56, 
                        payee_id = '0', 
                        payee_name = '0', 
                        category_id = '0', 
                        memo = '0', 
                        cleared = 'cleared', 
                        approved = True, 
                        flag_color = 'red', 
                        import_id = '0', )
                    ]
            )
        else :
            return BulkTransactions(
                transactions = [
                    openapi_client.models.save_transaction.SaveTransaction(
                        account_id = '0', 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        amount = 56, 
                        payee_id = '0', 
                        payee_name = '0', 
                        category_id = '0', 
                        memo = '0', 
                        cleared = 'cleared', 
                        approved = True, 
                        flag_color = 'red', 
                        import_id = '0', )
                    ],
        )

    def testBulkTransactions(self):
        """Test BulkTransactions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
