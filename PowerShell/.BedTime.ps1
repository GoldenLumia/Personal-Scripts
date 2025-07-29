# Elevation Block (needed for rustdesk bat, called before anything else by PS anyways it seems so mind as well stick it up here)
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))  
{  
  $arguments = "& '" +$myinvocation.mycommand.definition + "'"
  Start-Process powershell -Verb runAs -ArgumentList $arguments
  Break
}
# Core Program Block
Import-Module "C:\PLACEHOLDER\Switch-NightLight.psm1"
Enable-NightLight
& "C:\PLACEHOLDER\Bluetooth.ps1" -BluetoothStatus On
Import-Module "C:\PLACEHOLDER\VolumeControl.psm1"
[audio]::Volume = 0.25
Start-Process -FilePath "C:\PLACEHOLDER\.start_rustdesk.bat" -Wait -NoNewWindow