Follow instructions here: https://kc.mcafee.com/corporate/index?page=content&id=KB70253&_ga=2.244946821.1433165505.1575395540-1615106853.1572638627

Get current EPOCH from here: https://www.epochconverter.com/

```
sudo sudo defaults write /Library/Preferences/com.mcafee.ssm.antimalware.plist Update_DAT_Time -string <current epoch>
sudo sudo defaults write /Library/Preferences/com.mcafee.ssm.antimalware.plist Update_Last_Update_Time -string <current epoch>

sudo launchctl unload /Library/LaunchDaemons/com.mcafee.ssm.ScanManager.plist
sudo launchctl load /Library/LaunchDaemons/com.mcafee.ssm.ScanManager.plist
sudo launchctl unload /Library/LaunchDaemons/com.mcafee.ssm.ScanFactory.plist
sudo launchctl load /Library/LaunchDaemons/com.mcafee.ssm.ScanFactory.plist
```
