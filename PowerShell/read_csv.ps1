#Get-ExecutionPolicy -List

#Import-Module ActiveDirectory
#New-ADUser -Name "John Doe" -GivenName "John" -Surname "Doe" -UserPrincipalName "johndoe@example.com" -SamAccountName "jdoe" -Path "OU=Users,DC=example,DC=com" -AccountPassword (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force) -Enabled $true


$a = Get-CimInstance -ClassName Win32_OperatingSystem
$b = New-Object PSObject -Property @{ version = $a.version; BuildNumber = $a.BuildNumber }
Write-Output "Version details: $($b.version)"

#Get-EventLog -LogName Application -EntryType Error -After (Get-Date).AddDays(-1)

hash_table = @{}

Get-Content -Path "D:\AI\PowerShell\test_input.txt"
Add-Content -Value "\n Welcome" -Path "D:\AI\PowerShell\test_input.txt"


$value = Import-Csv -path "D:\AI\PowerShell\csv_input_1.csv"
# Get the column headers
$columnHeaders = $value[0].PSObject.Properties.Name

# Display the column headers
$columnHeaders[1]




