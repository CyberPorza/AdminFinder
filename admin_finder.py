import requests
import sys

def admin_finder():
    green = "\033[1;32m"
    red = "\033[1;31m"
    reset = "\033[0m"
    blue = "\033[1;34m"

    banner = r"""
    ______________________________________________________________
    
       ______      __             ____                      
      / ____/_  __/ /_  ___  ____/ __ \____  _____________ _
     / /   / / / / __ \/ _ \/ __/ /_/ / __ \/ ___/_  / __ `/
    / /___/ /_/ / /_/ /  __/ / / ____/ /_/ / /    / /_/ /_/ 
    \____/\__, /_.___/\___/_/ /_/    \____/_/    /___/\__,_/  
         /____/          [ Admin Page Finder v1.1 ] 🛡️
    ______________________________________________________________
    """
    print(green + banner + reset)
    print(f"{blue}             Developed by CyberPorza{reset}")
    
    if len(sys.argv) < 2:
        print(red + " [!] Usage: python3 admin_finder.py <url>" + reset)
        print(blue + " Example: python3 admin_finder.py https://example.com" + reset)
        sys.exit()

    target_url = sys.argv[1]
    if not target_url.startswith("http"):
        target_url = "http://" + target_url

    admin_list = [
        "admin/", "login/", "admin_panel/", "wp-admin/", "administrator/",
        "user/", "login.php", "admin.php", "cpanel/", "panel/", "manage/",
        "yonetim/", "yonetici/", "wp-login.php"
    ]

    print(f"{blue} [*] Searching for admin panels on: {target_url} ...{reset}")
    print("-" * 62)

    found_count = 0
    try:
        for path in admin_list:
            url = f"{target_url.strip('/')}/{path}"
            try:
                response = requests.get(url, timeout=2)
                if response.status_code == 200:
                    print(f"{green} [+] SUCCESS: Admin Panel Found! -> {url} (Status: 200){reset}")
                    found_count += 1
                elif response.status_code == 403:
                    print(f" [-] Access Forbidden: {path} (Status: 403)")
            except requests.ConnectionError:
                pass
            
    except KeyboardInterrupt:
        print(red + "\n [!] Search interrupted by user." + reset)
        sys.exit()

    print("-" * 62)
    print(f"{blue} [*] Search complete. Found {found_count} potential admin panels.{reset}")
    print("=" * 62)

if __name__ == "__main__":
    admin_finder()
