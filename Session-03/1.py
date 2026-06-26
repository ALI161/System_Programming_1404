import winreg

p = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"

try:
    k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, p)

    v, t = winreg.QueryValueEx(k, "AppsUseLightTheme")

    if v == 0:
        print("Dark Mode is ON")
    else:
        print("Dark Mode is OFF")

    winreg.CloseKey(k)

except:
    print("Error")