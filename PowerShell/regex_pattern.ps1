# Define the string
$text = "Contact us at support@example.com for more information."

# Define the regex pattern for an email address
$pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Use the -match operator to check if the pattern exists in the string
if ($text -match $pattern) {
    # The matched value is stored in the $matches automatic variable
    $email = $matches[0]
    Write-Output "Found email address: $email"
} else {
    Write-Output "No email address found."
}


# Define the string containing multiple IP addresses
$text = "Servers are located at 192.168.1.1, 10.0.0.5, and 172.16.0.3."

# Define the regex pattern for an IPv4 address
$pattern = "\b(?:(?:2[0-4][0-9]|25[0-5]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:2[0-4][0-9]|25[0-5]|1[0-9][0-9]|[1-9]?[0-9])\b"

# Use Select-String to find all matches
$matches = Select-String -InputObject $text -Pattern $pattern -AllMatches

# Output all found IP addresses
foreach ($match in $matches.Matches) {
    Write-Output "Found IP address: $($match.Value)"
}
