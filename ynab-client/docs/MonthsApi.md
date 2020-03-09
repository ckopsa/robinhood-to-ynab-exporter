# openapi_client.MonthsApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_budget_month**](MonthsApi.md#get_budget_month) | **GET** /budgets/{budget_id}/months/{month} | Single budget month
[**get_budget_months**](MonthsApi.md#get_budget_months) | **GET** /budgets/{budget_id}/months | List budget months


# **get_budget_month**
> MonthDetailResponse get_budget_month(budget_id, month)

Single budget month

Returns a single budget month

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
    api_instance = openapi_client.MonthsApi(api_client)
    budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
month = '2013-10-20' # date | The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))

    try:
        # Single budget month
        api_response = api_instance.get_budget_month(budget_id, month)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonthsApi->get_budget_month: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) | 
 **month** | **date**| The budget month in ISO format (e.g. 2016-12-01) (\&quot;current\&quot; can also be used to specify the current calendar month (UTC)) | 

### Return type

[**MonthDetailResponse**](MonthDetailResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The budget month detail |  -  |
**404** | The budget month was not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_months**
> MonthSummariesResponse get_budget_months(budget_id, last_knowledge_of_server=last_knowledge_of_server)

List budget months

Returns all budget months

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
    api_instance = openapi_client.MonthsApi(api_client)
    budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
last_knowledge_of_server = 56 # int | The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. (optional)

    try:
        # List budget months
        api_response = api_instance.get_budget_months(budget_id, last_knowledge_of_server=last_knowledge_of_server)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonthsApi->get_budget_months: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) | 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. | [optional] 

### Return type

[**MonthSummariesResponse**](MonthSummariesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of budget months |  -  |
**404** | No budget months were found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

