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
from openapi_client.models.month_summary import MonthSummary  # noqa: E501
from openapi_client.rest import ApiException

class TestMonthSummary(unittest.TestCase):
    """MonthSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MonthSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.month_summary.MonthSummary()  # noqa: E501
        if include_optional :
            return MonthSummary(
                month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                note = '0', 
                income = 56, 
                budgeted = 56, 
                activity = 56, 
                to_be_budgeted = 56, 
                age_of_money = 56, 
                deleted = True
            )
        else :
            return MonthSummary(
                month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                income = 56,
                budgeted = 56,
                activity = 56,
                to_be_budgeted = 56,
                deleted = True,
        )

    def testMonthSummary(self):
        """Test MonthSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
