# BudgetDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**last_modified_on** | **datetime** | The last time any changes were made to the budget from either a web or mobile client | [optional] 
**first_month** | **date** | The earliest budget month | [optional] 
**last_month** | **date** | The latest budget month | [optional] 
**date_format** | [**DateFormat**](DateFormat.md) |  | [optional] 
**currency_format** | [**CurrencyFormat**](CurrencyFormat.md) |  | [optional] 
**accounts** | [**list[Account]**](Account.md) |  | [optional] 
**payees** | [**list[Payee]**](Payee.md) |  | [optional] 
**payee_locations** | [**list[PayeeLocation]**](PayeeLocation.md) |  | [optional] 
**category_groups** | [**list[CategoryGroup]**](CategoryGroup.md) |  | [optional] 
**categories** | [**list[Category]**](Category.md) |  | [optional] 
**months** | [**list[MonthDetail]**](MonthDetail.md) |  | [optional] 
**transactions** | [**list[TransactionSummary]**](TransactionSummary.md) |  | [optional] 
**subtransactions** | [**list[SubTransaction]**](SubTransaction.md) |  | [optional] 
**scheduled_transactions** | [**list[ScheduledTransactionSummary]**](ScheduledTransactionSummary.md) |  | [optional] 
**scheduled_subtransactions** | [**list[ScheduledSubTransaction]**](ScheduledSubTransaction.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


