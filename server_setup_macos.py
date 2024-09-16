# Automate Server Setup on MacOs
# The script will automate the process of setting up an Nginx web server server,
# Configuring firewall rules and Securing SSH

import subprocess

def run_command(command):
    """Run a shell command and check for errors"""
    try:
        print(f"Running: {command}")
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as error:
        print(f"Error: {error.stderr}")
        raise

def update_system():
    #Update Homebrew and upgrade system packages
    print("Updating Homebrew packages...")
    run_command("brew update && brew upgrade")

def install_nginx():
    #Install Nginx web server
    print("Installing Nginx web server via Homebrew...")
    
    # Install Nginx
    run_command("brew install nginx")
    
    # Create and start Nginx as a service
    run_command("sudo brew services start nginx")

def configure_firewall():
    #Configure macOS firewall to allow Nginx traffic
    print("Configuring macOS firewall for Nginx...")
    
    # Allow Nginx HTTP (port 80) and HTTPS (port 443) traffic through macOS firewall
    run_command('sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/local/opt/nginx/bin/nginx')
    run_command('sudo /usr/libexec/ApplicationFirewall/socketfilterfw --unblockapp /usr/local/opt/nginx/bin/nginx')

def configure_ssh():
    """Secure SSH on macOS"""
    print("Securing SSH...")
    
    # Disable root login
    run_command("sudo sed -i '' 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config")
    
    # Disable password authentication
    run_command("sudo sed -i '' 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config")
    
    # Restart SSH service
    run_command("sudo launchctl unload /System/Library/LaunchDaemons/ssh.plist && sudo launchctl load /System/Library/LaunchDaemons/ssh.plist")

def show_status():
    # Show the status of Nginx and firewall
    print("Checking Nginx status...")
    run_command("sudo brew services list | grep nginx")

def main():
    # Main function to automate the server setup on macOS
    try:
        update_system()
        install_nginx()
        configure_firewall()
        configure_ssh()
        show_status()
        print("Server setup complete on macOS!")
    except Exception as e:
        print(f"Server setup failed: {e}")

if __name__ == "__main__":
    main()
