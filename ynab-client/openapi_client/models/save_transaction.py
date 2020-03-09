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


class SaveTransaction(object):
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
        'account_id': 'str',
        'date': 'date',
        'amount': 'int',
        'payee_id': 'str',
        'payee_name': 'str',
        'category_id': 'str',
        'memo': 'str',
        'cleared': 'str',
        'approved': 'bool',
        'flag_color': 'str',
        'import_id': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'date': 'date',
        'amount': 'amount',
        'payee_id': 'payee_id',
        'payee_name': 'payee_name',
        'category_id': 'category_id',
        'memo': 'memo',
        'cleared': 'cleared',
        'approved': 'approved',
        'flag_color': 'flag_color',
        'import_id': 'import_id'
    }

    def __init__(self, account_id=None, date=None, amount=None, payee_id=None, payee_name=None, category_id=None, memo=None, cleared=None, approved=None, flag_color=None, import_id=None, local_vars_configuration=None):  # noqa: E501
        """SaveTransaction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._date = None
        self._amount = None
        self._payee_id = None
        self._payee_name = None
        self._category_id = None
        self._memo = None
        self._cleared = None
        self._approved = None
        self._flag_color = None
        self._import_id = None
        self.discriminator = None

        self.account_id = account_id
        self.date = date
        self.amount = amount
        if payee_id is not None:
            self.payee_id = payee_id
        if payee_name is not None:
            self.payee_name = payee_name
        if category_id is not None:
            self.category_id = category_id
        if memo is not None:
            self.memo = memo
        if cleared is not None:
            self.cleared = cleared
        if approved is not None:
            self.approved = approved
        if flag_color is not None:
            self.flag_color = flag_color
        if import_id is not None:
            self.import_id = import_id

    @property
    def account_id(self):
        """Gets the account_id of this SaveTransaction.  # noqa: E501


        :return: The account_id of this SaveTransaction.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this SaveTransaction.


        :param account_id: The account_id of this SaveTransaction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def date(self):
        """Gets the date of this SaveTransaction.  # noqa: E501

        The transaction date in ISO format (e.g. 2016-12-01).  Future dates (scheduled transactions) are not permitted.  Split transaction dates cannot be changed and if a different date is supplied it will be ignored.  # noqa: E501

        :return: The date of this SaveTransaction.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this SaveTransaction.

        The transaction date in ISO format (e.g. 2016-12-01).  Future dates (scheduled transactions) are not permitted.  Split transaction dates cannot be changed and if a different date is supplied it will be ignored.  # noqa: E501

        :param date: The date of this SaveTransaction.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def amount(self):
        """Gets the amount of this SaveTransaction.  # noqa: E501

        The transaction amount in milliunits format.  Split transaction amounts cannot be changed and if a different amount is supplied it will be ignored.  # noqa: E501

        :return: The amount of this SaveTransaction.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SaveTransaction.

        The transaction amount in milliunits format.  Split transaction amounts cannot be changed and if a different amount is supplied it will be ignored.  # noqa: E501

        :param amount: The amount of this SaveTransaction.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def payee_id(self):
        """Gets the payee_id of this SaveTransaction.  # noqa: E501

        The payee for the transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as tranfer_payee_id on the account resource.  # noqa: E501

        :return: The payee_id of this SaveTransaction.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this SaveTransaction.

        The payee for the transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as tranfer_payee_id on the account resource.  # noqa: E501

        :param payee_id: The payee_id of this SaveTransaction.  # noqa: E501
        :type: str
        """

        self._payee_id = payee_id

    @property
    def payee_name(self):
        """Gets the payee_name of this SaveTransaction.  # noqa: E501

        The payee name.  If a payee_name value is provided and payee_id has a null value, the payee_name value will be used to resolve the payee by either (1) a matching payee rename rule (only if import_id is also specified) or (2) a payee with the same name or (3) creation of a new payee.  # noqa: E501

        :return: The payee_name of this SaveTransaction.  # noqa: E501
        :rtype: str
        """
        return self._payee_name

    @payee_name.setter
    def payee_name(self, payee_name):
        """Sets the payee_name of this SaveTransaction.

        The payee name.  If a payee_name value is provided and payee_id has a null value, the payee_name value will be used to resolve the payee by either (1) a matching payee rename rule (only if import_id is also specified) or (2) a payee with the same name or (3) creation of a new payee.  # noqa: E501

        :param payee_name: The payee_name of this SaveTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                payee_name is not None and len(payee_name) > 50):
            raise ValueError("Invalid value for `payee_name`, length must be less than or equal to `50`")  # noqa: E501

        self._payee_name = payee_name

    @property
    def category_id(self):
        """Gets the category_id of this SaveTransaction.  # noqa: E501

        The category for the transaction.  Split and Credit Card Payment categories are not permitted and will be ignored if supplied.  If an existing transaction has a Split category it cannot be changed.  # noqa: E501

        :return: The category_id of this SaveTransaction.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this SaveTransaction.

        The category for the transaction.  Split and Credit Card Payment categories are not permitted and will be ignored if supplied.  If an existing transaction has a Split category it cannot be changed.  # noqa: E501

        :param category_id: The category_id of this SaveTransaction.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def memo(self):
        """Gets the memo of this SaveTransaction.  # noqa: E501


        :return: The memo of this SaveTransaction.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this SaveTransaction.


        :param memo: The memo of this SaveTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                memo is not None and len(memo) > 200):
            raise ValueError("Invalid value for `memo`, length must be less than or equal to `200`")  # noqa: E501

        self._memo = memo

    @property
    def cleared(self):
        """Gets the cleared of this SaveTransaction.  # noqa: E501

        The cleared status of the transaction  # noqa: E501

        :return: The cleared of this SaveTransaction.  # noqa: E501
        :rtype: str
        """
        return self._cleared

    @cleared.setter
    def cleared(self, cleared):
        """Sets the cleared of this SaveTransaction.

        The cleared status of the transaction  # noqa: E501

        :param cleared: The cleared of this SaveTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["cleared", "uncleared", "reconciled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cleared not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cleared` ({0}), must be one of {1}"  # noqa: E501
                .format(cleared, allowed_values)
            )

        self._cleared = cleared

    @property
    def approved(self):
        """Gets the approved of this SaveTransaction.  # noqa: E501

        Whether or not the transaction is approved.  If not supplied, transaction will be unapproved by default.  # noqa: E501

        :return: The approved of this SaveTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this SaveTransaction.

        Whether or not the transaction is approved.  If not supplied, transaction will be unapproved by default.  # noqa: E501

        :param approved: The approved of this SaveTransaction.  # noqa: E501
        :type: bool
        """

        self._approved = approved

    @property
    def flag_color(self):
        """Gets the flag_color of this SaveTransaction.  # noqa: E501

        The transaction flag  # noqa: E501

        :return: The flag_color of this SaveTransaction.  # noqa: E501
        :rtype: str
        """
        return self._flag_color

    @flag_color.setter
    def flag_color(self, flag_color):
        """Sets the flag_color of this SaveTransaction.

        The transaction flag  # noqa: E501

        :param flag_color: The flag_color of this SaveTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["red", "orange", "yellow", "green", "blue", "purple"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and flag_color not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `flag_color` ({0}), must be one of {1}"  # noqa: E501
                .format(flag_color, allowed_values)
            )

        self._flag_color = flag_color

    @property
    def import_id(self):
        """Gets the import_id of this SaveTransaction.  # noqa: E501

        If specified, the new transaction will be assigned this import_id and considered \"imported\".  We will also attempt to match this imported transaction to an existing \"user-entered\" transation on the same account, with the same amount, and with a date +/-10 days from the imported transaction date.<br><br>Transactions imported through File Based Import or Direct Import (not through the API) are assigned an import_id in the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'. For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.  Using a consistent format will prevent duplicates through Direct Import and File Based Import.<br><br>If import_id is omitted or specified as null, the transaction will be treated as a \"user-entered\" transaction. As such, it will be eligible to be matched against transactions later being imported (via DI, FBI, or API).  # noqa: E501

        :return: The import_id of this SaveTransaction.  # noqa: E501
        :rtype: str
        """
        return self._import_id

    @import_id.setter
    def import_id(self, import_id):
        """Sets the import_id of this SaveTransaction.

        If specified, the new transaction will be assigned this import_id and considered \"imported\".  We will also attempt to match this imported transaction to an existing \"user-entered\" transation on the same account, with the same amount, and with a date +/-10 days from the imported transaction date.<br><br>Transactions imported through File Based Import or Direct Import (not through the API) are assigned an import_id in the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'. For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.  Using a consistent format will prevent duplicates through Direct Import and File Based Import.<br><br>If import_id is omitted or specified as null, the transaction will be treated as a \"user-entered\" transaction. As such, it will be eligible to be matched against transactions later being imported (via DI, FBI, or API).  # noqa: E501

        :param import_id: The import_id of this SaveTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                import_id is not None and len(import_id) > 36):
            raise ValueError("Invalid value for `import_id`, length must be less than or equal to `36`")  # noqa: E501

        self._import_id = import_id

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
        if not isinstance(other, SaveTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SaveTransaction):
            return True

        return self.to_dict() != other.to_dict()
