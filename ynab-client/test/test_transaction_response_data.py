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
from openapi_client.models.transaction_response_data import TransactionResponseData  # noqa: E501
from openapi_client.rest import ApiException

class TestTransactionResponseData(unittest.TestCase):
    """TransactionResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TransactionResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.transaction_response_data.TransactionResponseData()  # noqa: E501
        if include_optional :
            return TransactionResponseData(
                transaction = null
            )
        else :
            return TransactionResponseData(
                transaction = null,
        )

    def testTransactionResponseData(self):
        """Test TransactionResponseData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()