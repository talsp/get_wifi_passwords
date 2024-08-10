import subprocess
import pandas as pd

def get_wifi_passwords():
        
        data = []
 
        profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        
        for profile in profiles_data:
           if "All User Profile" in profile:
              profile_split = profile.split(":")
              ssid = profile_split[1]
              try:
                profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', ssid.strip(), 'key=clear']).decode('utf-8').split('\n')

                for info in profile_info:
                    if "Key Content" in info:
                        info_split = info.split(":")
                        pwd = info_split[1]
                        temp_data = {"Profile": ssid.strip(), "Password": pwd.strip()}
                        data.append(temp_data)
              except Exception as e:
                  print(f"[-] Error: {e}")
           
    
        return data

if __name__ == "__main__":
    print("[+] Fetching WIFI password...")
    data = get_wifi_passwords()
    data_df =  pd.DataFrame(data)
    print(data_df)
   
