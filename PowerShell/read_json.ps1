# Define the path to the JSON file
$jsonFilePath = "D:\AI\PowerShell\1.json"


# Read the JSON file content
$jsonContent = Get-Content -Path $jsonFilePath -Raw
write-host($jsonContent)

# Convert the JSON content to a PowerShell object
$jsonObject = $jsonContent | ConvertFrom-Json

# Output the PowerShell object
$jsonObject

# read dict value
$jsonObject.Address.City

#read list vale
$jsonObject.PhoneNumbers[0]
