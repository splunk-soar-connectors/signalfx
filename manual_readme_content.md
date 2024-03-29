[comment]: # " File: README.md"
[comment]: # "  Copyright (c) 2021-2023 Splunk Inc."
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

## Event Dimensions

-   When crafting your Event Dimensions keep in mind:

      

    1.  Must be valid JSON
    2.  When running the action using datapaths in modern playbook, curly bracket characters that
        are not datapath references must be escaped with an additional curly bracket. E.G. { becomes
        {{  
        Example Dimensions Input: {{\\"description\\":\\"{0}\\",\\"tag\\":\\"{1}\\"}}  
        where {0} and {1} represent datapaths.

-   Dimension key criteria:

      

    1.  Maximum length can be 128 characters
    2.  Must start with an uppercase or lowercase letter
    3.  After the first character, the name can contain letters, numbers, underscores (\_), and
        hyphens (-)
    4.  Spaces in dimension keys are not allowed
    5.  If the dimension key does not match the criteria then the action may pass but event will not
        be created on SignalFx portal
