## Steps to generate Access Token

1. Log In to your Signal Fx account
1. Click on My Profile under the settings tab at the top right corner
1. Click on Access Tokens
1. Click on New Token
1. Provide a name for the token and select both 'Ingest Token' and 'Api Token' options
1. Click on OK
1. A new entry with the Name you provided appears on the page. Expand it and click on 'Show Token'
   to get the token
1. Copy the generated token and use it in 'Access Token' asset configuration parameter

## Event Dimensions

- When crafting your Event Dimensions keep in mind:

  1. Must be valid JSON
  1. When running the action using datapaths in modern playbook, curly bracket characters that
     are not datapath references must be escaped with an additional curly bracket. E.G. { becomes
     {{\
     Example Dimensions Input: {{\\"description\\":\\"{0}\\",\\"tag\\":\\"{1}\\"}}\
     where {0} and {1} represent datapaths.

- Dimension key criteria:

  1. Maximum length can be 128 characters
  1. Must start with an uppercase or lowercase letter
  1. After the first character, the name can contain letters, numbers, underscores (\_), and
     hyphens (-)
  1. Spaces in dimension keys are not allowed
  1. If the dimension key does not match the criteria then the action may pass but event will not
     be created on SignalFx portal
