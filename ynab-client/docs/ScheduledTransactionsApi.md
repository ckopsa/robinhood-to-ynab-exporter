# openapi_client.ScheduledTransactionsApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_scheduled_transaction_by_id**](ScheduledTransactionsApi.md#get_scheduled_transaction_by_id) | **GET** /budgets/{budget_id}/scheduled_transactions/{scheduled_transaction_id} | Single scheduled transaction
[**get_scheduled_transactions**](ScheduledTransactionsApi.md#get_scheduled_transactions) | **GET** /budgets/{budget_id}/scheduled_transactions | List scheduled transactions


# **get_scheduled_transaction_by_id**
> ScheduledTransactionResponse get_scheduled_transaction_by_id(budget_id, scheduled_transaction_id)

Single scheduled transaction

Returns a single scheduled transaction

### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.youneedabudget.com/v1
configuration.host = "https://api.youneedabudget.com/v1"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ScheduledTransactionsApi(api_client)
    budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
scheduled_transaction_id = 'scheduled_transaction_id_example' # str | The id of the scheduled transaction

    try:
        # Single scheduled transaction
        api_response = api_instance.get_scheduled_transaction_by_id(budget_id, scheduled_transaction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScheduledTransactionsApi->get_scheduled_transaction_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) | 
 **scheduled_transaction_id** | **str**| The id of the scheduled transaction | 

### Return type

[**ScheduledTransactionResponse**](ScheduledTransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Scheduled Transaction |  -  |
**404** | The scheduled transaction was not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_transactions**
> ScheduledTransactionsResponse get_scheduled_transactions(budget_id, last_knowledge_of_server=last_knowledge_of_server)

List scheduled transactions

Returns all scheduled transactions

### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.youneedabudget.com/v1
configuration.host = "https://api.youneedabudget.com/v1"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ScheduledTransactionsApi(api_client)
    budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
last_knowledge_of_server = 56 # int | The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. (optional)

    try:
        # List scheduled transactions
        api_response = api_instance.get_scheduled_transactions(budget_id, last_knowledge_of_server=last_knowledge_of_server)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScheduledTransactionsApi->get_scheduled_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) | 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. | [optional] 

### Return type

[**ScheduledTransactionsResponse**](ScheduledTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested scheduled transactions |  -  |
**404** | No scheduled transactions were found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

