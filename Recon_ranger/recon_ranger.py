import os
import subprocess
import requests
import json
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init()

# Define the text
main_title = "AUTOMATED_RECON"
sub_title = "                Created By Pavan Kumar Tule"

# Use pyfiglet to create the large text
main_title_fig = pyfiglet.figlet_format(main_title)
sub_title_fig = pyfiglet.figlet_format(sub_title)

# Print the text with green color
print(f"{Fore.GREEN}{main_title_fig}{Style.RESET_ALL}")
print(f"{Fore.GREEN}{sub_title_fig}{Style.RESET_ALL}")

# Keep the script running so the text remains visible
#input("Press Enter to exit...")

class ReconRanger:
    def __init__(self, target):
        self.target = target
        self.output_dir = f"recon_results/{target}"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    #Subdomain Enumeration
    def subdomain_enum(self):
        print("Performing Subdomain Enumeration...")
        subprocess.run(f"subfinder -d {self.target} -o {self.output_dir}/subdomains.txt", shell=True)
        subprocess.run(f"assetfinder -d {self.target} -o {self.output_dir}/assetfinder.txt", shell=True)
        subprocess.run(f"findomain -t {self.target} -o {self.output_dir}/findomain.txt", shell=True)

    #Live Subdomains
    def live_subdomains(self):
        print("Identifying Live Subdomains...")
        subprocess.run(f"httpx -l -o {self.output_dir}/live_subdomains.txt {self.output_dir}/subdomains.txt", shell=True)

    #Subdomain Takeovers
    def subdomain_takeover(self):
        print("Checking for Subdomain Takeovers...")
        subprocess.run(f"subzy -d {self.target} -o {self.output_dir}/subdomain_takeover.txt", shell=True)

    #Finding Open Ports
    def open_ports(self):
        print("Finding Open Ports...")
        subprocess.run(f"naabu -host {self.target} -o {self.output_dir}/open_ports.txt", shell=True)

    #JSON Files Finding
    def json_files_discovery(self):
        print("Searching for JSON Files...")
        subprocess.run(f"waybackurls {self.target} -o {self.output_dir}/json_files.txt", shell=True)

    #Javascript Finding
    def js_vulnerabilities(self):
        print("Identifying JavaScript Vulnerabilities...")
        subprocess.run(f"katana -u {self.target} -o {self.output_dir}/js_vulnerabilities.txt", shell=True)
        subprocess.run(f"subjs -u {self.target} -o {self.output_dir}/subjs.txt", shell=True)
        subprocess.run(f"httpx -u {self.target} -o {self.output_dir}/httpx_js.txt", shell=True)
        subprocess.run(f"nuclei -u {self.target} -o {self.output_dir}/nuclei_js.txt", shell=True)

    #Hindden Directories Finding
    def directory_enumeration(self):
        print("Discovering Hidden Directories...")
        subprocess.run(f"dirsearch -u {self.target} -o {self.output_dir}/directories.txt", shell=True)
    
    #Finding Injection
    def injection_vulnerabilities(self):
        print("Finding Injection Vulnerabilities...")
        subprocess.run(f"gospider -u {self.target} -o {self.output_dir}/injection_vulnerabilities.txt", shell=True)
        subprocess.run(f"qsreplace -u {self.target} -o {self.output_dir}/qsreplace.txt", shell=True)
        subprocess.run(f"dalfox -u {self.target} -o {self.output_dir}/dalfox.txt", shell=True)
    
    #Finding XSS 
    def xss_vulnerabilities(self):
        print("Detecting XSS Vulnerabilities...")
        subprocess.run(f"gospider -u {self.target} -o {self.output_dir}/xss_vulnerabilities.txt", shell=True)
        subprocess.run(f"qsreplace -u {self.target} -o {self.output_dir}/qsreplace_xss.txt", shell=True)
        subprocess.run(f"dalfox -u {self.target} -o {self.output_dir}/dalfox_xss.txt", shell=True)

    #Open Redirections
    def open_redirection(self):
        print("Identifying Open Redirections...")
        subprocess.run(f"uro -u {self.target} -o {self.output_dir}/open_redirection.txt", shell=True)
    
    #Finding Comprehensive
    def comprehensive_vulnerability_scanning(self):
        print("Performing Comprehensive Vulnerability Scanning...")
        subprocess.run(f"nuclei -u {self.target} -o {self.output_dir}/nuclei_vulnerabilities.txt", shell=True)

    def run_recon(self):
        self.subdomain_enum()
        self.live_subdomains()
        self.subdomain_takeover()
        self.open_ports()
        self.json_files_discovery()
        self.js_vulnerabilities()
        self.directory_enumeration()
        self.injection_vulnerabilities()
        self.xss_vulnerabilities()
        self.open_redirection()
        self.comprehensive_vulnerability_scanning()

