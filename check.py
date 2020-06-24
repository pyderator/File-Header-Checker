import lsb_release
import os

release_version = lsb_release.get_lsb_information().get('RELEASE')
if release_version <= '18.04':
    if os.system("dpkg-query -l | grep snapd") == 0:
        print('Snap is already installed')
        if os.system("snap list --all | grep hexyl") == 0:
            print('Hexyl is already installed')
        else:
            print('Installing hexyl')
            os.system("sudo snap install hexyl")
            print('Hexyl Installed Successfully')
        print('Extracting Header of Files')
        for f in os.listdir():
            print(f,end='/t')
            print(os.system(f'hexyl {f} -c 16'))
    else:
        print("Installing Snap")
        os.system('sudo apt-install snap')
        print("Installing Hexyl")
        os.system('sudo snap install hexyl')


