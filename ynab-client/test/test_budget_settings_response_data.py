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
from openapi_client.models.budget_settings_response_data import BudgetSettingsResponseData  # noqa: E501
from openapi_client.rest import ApiException

class TestBudgetSettingsResponseData(unittest.TestCase):
    """BudgetSettingsResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BudgetSettingsResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.budget_settings_response_data.BudgetSettingsResponseData()  # noqa: E501
        if include_optional :
            return BudgetSettingsResponseData(
                settings = openapi_client.models.budget_settings.BudgetSettings(
                    date_format = openapi_client.models.date_format.DateFormat(
                        format = '0', ), 
                    currency_format = openapi_client.models.currency_format.CurrencyFormat(
                        iso_code = '0', 
                        example_format = '0', 
                        decimal_digits = 56, 
                        decimal_separator = '0', 
                        symbol_first = True, 
                        group_separator = '0', 
                        currency_symbol = '0', 
                        display_symbol = True, ), )
            )
        else :
            return BudgetSettingsResponseData(
                settings = openapi_client.models.budget_settings.BudgetSettings(
                    date_format = openapi_client.models.date_format.DateFormat(
                        format = '0', ), 
                    currency_format = openapi_client.models.currency_format.CurrencyFormat(
                        iso_code = '0', 
                        example_format = '0', 
                        decimal_digits = 56, 
                        decimal_separator = '0', 
                        symbol_first = True, 
                        group_separator = '0', 
                        currency_symbol = '0', 
                        display_symbol = True, ), ),
        )

    def testBudgetSettingsResponseData(self):
        """Test BudgetSettingsResponseData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
