# Automate Server Setup on linux
# The script will automate the process of setting up an Nginx web server server,
# Configuring firewall rules and Securing SSH

import subprocess

def run_command(command):
    # Run a shell command and check for errors
    try:
        print(f"Running: {command}")
        result = subprocess.run(command, shell=True, check= True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as error:
        print(f"Error: {error.stderr}")
        raise


def update_system():
    #Update and upgrade system packages
    print("Updating system packages...")
    run_command("sudo apt update -y && sudo apt upgrade -y")


def install_nginx():
    # Install nginx web server
    print("Installing nginx web server...")
    run_command("sudo apt install nginx -y")
    run_command("sudo systemctl enable nginx")
    run_command("sudo systemctl start nginx")


def configure_firewall():
    # Configure firewall rules
    print("Configuring firewall...")
    run_command("sudo ufw allow OpenSSH")
    run_command("sudo ufw allow 'Nginx full'") 
    run_command("sudo ufw --force enable")


def configure_ssh():
    # Secure SSH by disabling root login and password authentication
    print("Securing SSH...")
    # Disable root Login
    run_command("sudo sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config")
    # Disable password authentication
    run_command("sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config")
    # Restart SSH service
    run_command("sudo service restart sshd")

def show_status():
    # Show status of Nginx and UFW
    print("Checking status of Nginx")
    run_command("sudo system status nginx")
    print("Checking status of UFW")
    run_command("sudo ufw status")

def main():
    # Main function to automate the server setup
    try:
        update_system()
        install_nginx()
        configure_firewall()
        configure_ssh()
        show_status()
    except Exception as e:
        print(f"Server setup failed: {e}")
    

if __name__ == "__main__":
    main()