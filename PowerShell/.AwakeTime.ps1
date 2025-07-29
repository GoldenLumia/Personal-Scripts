# Elevation Block
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))  
{  
  $arguments = "& '" +$myinvocation.mycommand.definition + "'"
  Start-Process powershell -Verb runAs -ArgumentList $arguments
  Break
}
# Core Program Block
Import-Module "C:\PLACEHOLDER\Switch-NightLight.psm1"
Disable-NightLight
& "C:\PLACEHOLDER\Bluetooth.ps1" -BluetoothStatus Off
Import-Module "C:\PLACEHOLDER\VolumeControl.psm1"
[audio]::Volume = 1.00
Start-Process -FilePath "C:\PLACEHOLDER\.stop_rustdesk.bat" -Wait -NoNewWindow