[comment]: # "Auto-generated SOAR connector documentation"
# SignalFx

Publisher: Splunk  
Connector Version: 1\.0\.9  
Product Vendor: Splunk  
Product Name: SignalFx  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.1\.0  

This App uses the Splunk Infrastructure Monitoring \(SignalFx\) API to retrieve and send data

[comment]: # " File: README.md"
[comment]: # "  Copyright (c) 2021-2022 Splunk Inc."
[comment]: # ""
[comment]: # "  Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)"
[comment]: # ""
## Steps to generate Access Token

1.  Log In to your Signal Fx account
2.  Click on My Profile under the settings tab at the top right corner
3.  Click on Access Tokens
4.  Click on New Token
5.  Provide a name for the token and select both 'Ingest Token' and 'Api Token' options
6.  Click on OK
7.  A new entry with the Name you provided appears on the page. Expand it and click on 'Show Token'
    to get the token
8.  Copy the generated token and use it in 'Access Token' asset configuration parameter


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a SignalFx asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base\_url** |  required  | string | Splunk Infrastructure Monitoring \(SignalFx\) URL
**token** |  required  | password | Go to SignalFx My Profile \-> Access Tokens

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[run query](#action-run-query) - Retrieves dimensions based on a query  
[clear incident](#action-clear-incident) - Clears a specified incident  
[get incident](#action-get-incident) - Get details of a specified incident  
[list incidents](#action-list-incidents) - List all incidents  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'run query'
Retrieves dimensions based on a query

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**query** |  required  | 'Dimension name' or 'name and value' to search for \(e\.g\: aws\_region\:region\_name\) | string |  `signalfx query` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.query | string |  `signalfx query` 
action\_result\.data | string |  `signalfx data` 
action\_result\.data\.\*\.count | numeric | 
action\_result\.data\.\*\.results\.\*\.key | string | 
action\_result\.data\.\*\.results\.\*\.value | string | 
action\_result\.data\.\*\.results\.\*\.created | numeric | 
action\_result\.data\.\*\.results\.\*\.creator | string | 
action\_result\.data\.\*\.results\.\*\.description | string | 
action\_result\.data\.\*\.results\.\*\.lastUpdated | numeric | 
action\_result\.data\.\*\.results\.\*\.lastUpdatedBy | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_arn | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_state | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_region | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_image\_id | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_tag\_Name | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_account\_id | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_hypervisor | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_instance\_id | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_launch\_time | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_architecture | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_state\_reason | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_instance\_type | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_reservation\_id | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_public\_dns\_name | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_private\_dns\_name | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_root\_device\_type | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_availability\_zone | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_public\_ip\_address | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_iops | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_size | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_encrypted | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_volume\_id | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_create\_time | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_snapshot\_id | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_volume\_type | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_attachment\_state | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_delete\_on\_termination | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_cluster\_name | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_service\_name | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_cluster\_status | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_queue\_arn | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_queue\_url | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_fifo\_queue | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_created\_timestamp | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_visibility\_timeout | string | 
action\_result\.data\.\*\.results\.\*\.customProperties\.aws\_maximum\_message\_size | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.total\_results | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'clear incident'
Clears a specified incident

Type: **generic**  
Read only: **False**

This action clears \(resolves\) a specific incident that is identified by the parameter incidentid\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**incidentid** |  required  | The ID of the incident to be cleared | string |  `signalfx incidentid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.incidentid | string |  `signalfx incidentid` 
action\_result\.data | string |  `signalfx data` 
action\_result\.data\.\*\.code | numeric | 
action\_result\.data\.\*\.message | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get incident'
Get details of a specified incident

Type: **investigate**  
Read only: **True**

This action pulls details of a specific incident that is identified by the parameter incidentid\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**incidentid** |  required  | The ID of the incident to get details about | string |  `signalfx incidentid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.incidentid | string |  `signalfx incidentid` 
action\_result\.data | string |  `signalfx data` 
action\_result\.data\.\*\.severity | string | 
action\_result\.data\.\*\.active | boolean | 
action\_result\.data\.\*\.anomalyState | string | 
action\_result\.data\.\*\.detectorId | string | 
action\_result\.data\.\*\.detectLabel | string | 
action\_result\.data\.\*\.detectorName | string | 
action\_result\.data\.\*\.displayBody | string | 
action\_result\.data\.\*\.isMuted | boolean | 
action\_result\.data\.\*\.triggeredWhileMuted | boolean | 
action\_result\.data\.\*\.triggeredNotificationSent | boolean | 
action\_result\.data\.\*\.duration | numeric | 
action\_result\.data\.\*\.incidentId | string |  `signalfx incidentid` 
action\_result\.data\.\*\.events\.\*\.id | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.state | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.sf\_metric | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_region | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_tenancy | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_platform | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_account\_id | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.cloud\_provider | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_instance\_type | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_instance\_family | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_availability\_zone | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_master\_account\_id | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.cloud\_provider\_service | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.value | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S2\.value | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S3\.value | string | 
action\_result\.data\.\*\.events\.\*\.severity | string | 
action\_result\.data\.\*\.events\.\*\.timestamp | numeric | 
action\_result\.data\.\*\.events\.\*\.detectorId | string | 
action\_result\.data\.\*\.events\.\*\.incidentId | string |  `signalfx incidentid` 
action\_result\.data\.\*\.events\.\*\.detectLabel | string | 
action\_result\.data\.\*\.events\.\*\.anomalyState | string | 
action\_result\.data\.\*\.events\.\*\.detectorName | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list incidents'
List all incidents

Type: **investigate**  
Read only: **True**

This action can return incidents up to index 10000\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**include\_resolved** |  optional  | Whether to fetch resolved incidents | boolean | 
**limit** |  optional  | Number of results to be returned | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.include\_resolved | boolean | 
action\_result\.parameter\.limit | numeric | 
action\_result\.data | string |  `signalfx data` 
action\_result\.data\.\*\.incidentId | string |  `signalfx incidentid` 
action\_result\.data\.\*\.severity | string | 
action\_result\.data\.\*\.active | boolean | 
action\_result\.data\.\*\.anomalyState | string | 
action\_result\.data\.\*\.detectorId | string | 
action\_result\.data\.\*\.detectLabel | string | 
action\_result\.data\.\*\.detectorName | string | 
action\_result\.data\.\*\.displayBody | string | 
action\_result\.data\.\*\.isMuted | boolean | 
action\_result\.data\.\*\.triggeredWhileMuted | boolean | 
action\_result\.data\.\*\.triggeredNotificationSent | boolean | 
action\_result\.data\.\*\.events\.\*\.id | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.state | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.sf\_metric | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_region | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_tenancy | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_platform | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_account\_id | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.cloud\_provider | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_instance\_type | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_instance\_family | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_availability\_zone | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.aws\_master\_account\_id | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.key\.cloud\_provider\_service | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S1\.value | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S2\.value | string | 
action\_result\.data\.\*\.events\.\*\.inputs\.\_S3\.value | string | 
action\_result\.data\.\*\.events\.\*\.severity | string | 
action\_result\.data\.\*\.events\.\*\.timestamp | numeric | 
action\_result\.data\.\*\.events\.\*\.detectorId | string | 
action\_result\.data\.\*\.events\.\*\.incidentId | string |  `signalfx incidentid` 
action\_result\.data\.\*\.events\.\*\.detectLabel | string | 
action\_result\.data\.\*\.events\.\*\.anomalyState | string | 
action\_result\.data\.\*\.events\.\*\.detectorName | string | 
action\_result\.data\.\*\.duration | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.total\_incidents | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 