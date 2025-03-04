$First = "Add-MpPreference -ThreatIDDefaultAction_Ids "
$Third = " -ThreatIDDefaultAction_Actions Allow -Force"
$ListID =   2147685180, `
            2147735507, `
            2147736914, `
            2147743522, `
            2147734094, `
            2147743421, `
            251873, `
            213927, `
            2147722906
$ListID | % { Invoke-Expression ($First + $_ + $Third) }
$ListPath = "C:\Windows\KMSAutoS", `
            "C:\Windows\System32\SppExtComObjHook.dll", `
            "C:\Windows\System32\SppExtComObjPatcher.exe", `
            "C:\Windows\AAct_Tools", "C:\Windows\AAct_Tools\AAct_x64.exe", `
            "C:\Windows\AAct_Tools\AAct_files\KMSSS.exe", `
            "C:\Windows\AAct_Tools\AAct_files", `
            "C:\Windows\KMS"
$First = "Add-MpPreference -ExclusionPath "
$Third = "-Force"
$ListPath | % { Invoke-Expression ($First + $_ + $Third) }
