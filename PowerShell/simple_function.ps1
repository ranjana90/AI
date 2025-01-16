function Add-Numbers {
    param (
        [int]$a,
        [int]$b
    )
    $sum = $a + $b
    Write-Host "The sum is $sum"
    Write-Output $sum
}

$aa = Add-Numbers -a 5 -b 3
# $result will be $null because Write-Host does not send output to the pipeline
