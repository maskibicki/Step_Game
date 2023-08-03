# netsh wlan show profile
#netsh wlan show profile <SSID> key=Clear

li = ["ssid1", "ssid2", "ssid3"]



wlan = input("netsh> ")

if wlan == "netsh wlan show profile":
    print("")
    print("Profiles on inteface Wi-Fi:")
    print("")
    print("Group policy profiles (read omly)")
    print("---------------------------------")
    print("    <None>")
    print("")
    print("User profiles")
    print("-------------")
    print(f"     All User Profile     : {li[0]}")
    print(f"     All User Profile     : {li[1]}")
    print(f"     All User Profile     : {li[2]}")
    key = input("netsh> ")
    if key == f"netsh wlan show profile {li[0]} key=Clear":
        print("122233242")
    