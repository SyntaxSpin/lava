import sys
import subprocess
import requests
import os

AUR_RPC = "https://aur.archlinux.org/rpc/?v=5"
AUR_GIT = "https://aur.archlinux.org/"

def search(pkg):
    resp = requests.get(f"{AUR_RPC}&type=search&arg={pkg}")
    results = resp.json()["results"]
    for r in results:
        print(f"{r['Name']}: {r['Description']}")
    if not results:
        print("No results found.")

def download(pkg):
    print(f"Cloning {pkg} from AUR...")
    subprocess.run(["git", "clone", f"{AUR_GIT}{pkg}.git"])

def install(pkg):
    download(pkg)
    os.chdir(pkg)
    subprocess.run(["makepkg", "-si"])
    os.chdir("..")

def remove(pkg):
    print(f"Removing {pkg} with pacman...")
    subprocess.run(["sudo", "pacman", "-R", pkg])

def main():
    if len(sys.argv) < 3:
        print("Usage: lava -S <pkgname> | -R <pkgname>")
        return
    flag, pkg = sys.argv[1], sys.argv[2]
    if flag == "-S":
        install(pkg)
    elif flag == "-R":
        remove(pkg)
    else:
        print(f"Unknown flag: {flag}")

if __name__ == "__main__":
    main()