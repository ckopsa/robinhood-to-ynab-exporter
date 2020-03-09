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
from openapi_client.models.bulk_response import BulkResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestBulkResponse(unittest.TestCase):
    """BulkResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BulkResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.bulk_response.BulkResponse()  # noqa: E501
        if include_optional :
            return BulkResponse(
                data = openapi_client.models.bulk_response_data.BulkResponse_data(
                    bulk = openapi_client.models.bulk_response_data_bulk.BulkResponse_data_bulk(
                        transaction_ids = [
                            '0'
                            ], 
                        duplicate_import_ids = [
                            '0'
                            ], ), )
            )
        else :
            return BulkResponse(
                data = openapi_client.models.bulk_response_data.BulkResponse_data(
                    bulk = openapi_client.models.bulk_response_data_bulk.BulkResponse_data_bulk(
                        transaction_ids = [
                            '0'
                            ], 
                        duplicate_import_ids = [
                            '0'
                            ], ), ),
        )

    def testBulkResponse(self):
        """Test BulkResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
