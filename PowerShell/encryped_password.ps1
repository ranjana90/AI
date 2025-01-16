# Create a secure string from the plaintext password
$secureString = ConvertTo-SecureString -String "MySecretPassword" -AsPlainText -Force


# Convert the secure string to an encrypted standard string representation
$encryptedString = $secureString | ConvertFrom-SecureString
write-host("Encrypted :",$encryptedString)

# Output the encrypted string to a file
$encryptedString | Out-File "password.txt" 