# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class HybridTransactionAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'parent_transaction_id': 'str',
        'account_name': 'str',
        'payee_name': 'str',
        'category_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'parent_transaction_id': 'parent_transaction_id',
        'account_name': 'account_name',
        'payee_name': 'payee_name',
        'category_name': 'category_name'
    }

    def __init__(self, type=None, parent_transaction_id=None, account_name=None, payee_name=None, category_name=None, local_vars_configuration=None):  # noqa: E501
        """HybridTransactionAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._parent_transaction_id = None
        self._account_name = None
        self._payee_name = None
        self._category_name = None
        self.discriminator = None

        self.type = type
        if parent_transaction_id is not None:
            self.parent_transaction_id = parent_transaction_id
        self.account_name = account_name
        if payee_name is not None:
            self.payee_name = payee_name
        if category_name is not None:
            self.category_name = category_name

    @property
    def type(self):
        """Gets the type of this HybridTransactionAllOf.  # noqa: E501

        Whether the hybrid transaction represents a regular transaction or a subtransaction  # noqa: E501

        :return: The type of this HybridTransactionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HybridTransactionAllOf.

        Whether the hybrid transaction represents a regular transaction or a subtransaction  # noqa: E501

        :param type: The type of this HybridTransactionAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["transaction", "subtransaction"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def parent_transaction_id(self):
        """Gets the parent_transaction_id of this HybridTransactionAllOf.  # noqa: E501

        For subtransaction types, this is the id of the parent transaction.  For transaction types, this id will be always be null.  # noqa: E501

        :return: The parent_transaction_id of this HybridTransactionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._parent_transaction_id

    @parent_transaction_id.setter
    def parent_transaction_id(self, parent_transaction_id):
        """Sets the parent_transaction_id of this HybridTransactionAllOf.

        For subtransaction types, this is the id of the parent transaction.  For transaction types, this id will be always be null.  # noqa: E501

        :param parent_transaction_id: The parent_transaction_id of this HybridTransactionAllOf.  # noqa: E501
        :type: str
        """

        self._parent_transaction_id = parent_transaction_id

    @property
    def account_name(self):
        """Gets the account_name of this HybridTransactionAllOf.  # noqa: E501


        :return: The account_name of this HybridTransactionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this HybridTransactionAllOf.


        :param account_name: The account_name of this HybridTransactionAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_name is None:  # noqa: E501
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def payee_name(self):
        """Gets the payee_name of this HybridTransactionAllOf.  # noqa: E501


        :return: The payee_name of this HybridTransactionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._payee_name

    @payee_name.setter
    def payee_name(self, payee_name):
        """Sets the payee_name of this HybridTransactionAllOf.


        :param payee_name: The payee_name of this HybridTransactionAllOf.  # noqa: E501
        :type: str
        """

        self._payee_name = payee_name

    @property
    def category_name(self):
        """Gets the category_name of this HybridTransactionAllOf.  # noqa: E501


        :return: The category_name of this HybridTransactionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this HybridTransactionAllOf.


        :param category_name: The category_name of this HybridTransactionAllOf.  # noqa: E501
        :type: str
        """

        self._category_name = category_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HybridTransactionAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HybridTransactionAllOf):
            return True

        return self.to_dict() != other.to_dict()
