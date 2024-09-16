import subprocess

def modify_apache_port(port):
    apache_conf = '/usr/local/etc/httpd/httpd.conf'  # Path for Homebrew-installed Apache
    try:
        # Replace the "Listen 80" line with the new port
        with open(apache_conf, 'r') as file:
            data = file.read()
        data = data.replace('Listen 80', f'Listen {port}')
        
        # Write the modified data back to the file
        with open(apache_conf, 'w') as file:
            file.write(data)
        print(f"Apache configuration updated to listen on port {port}.")
    except Exception as e:
        print(f"Failed to update Apache configuration: {e}")

def modify_nginx_port(port):
    nginx_conf = '/usr/local/etc/nginx/nginx.conf'  # Path for Homebrew-installed Nginx
    try:
        # Replace the "listen 80;" line with the new port
        with open(nginx_conf, 'r') as file:
            data = file.read()
        data = data.replace('listen 80;', f'listen {port};')
        
        # Write the modified data back to the file
        with open(nginx_conf, 'w') as file:
            file.write(data)
        print(f"Nginx configuration updated to listen on port {port}.")
    except Exception as e:
        print(f"Failed to update Nginx configuration: {e}")

def start_apache(port=80):
    modify_apache_port(port)  # Modify the port in the Apache config
    try:
        subprocess.run(['sudo', 'apachectl', 'start'], check=True)
        print(f"Apache server started on port {port}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Apache: {e}")

def start_nginx(port=80):
    modify_nginx_port(port)  # Modify the port in the Nginx config
    try:
        subprocess.run(['sudo', 'nginx'], check=True)
        print(f"Nginx server started on port {port}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Nginx: {e}")

# Example: Call the function to bind and start the server on a custom port
#start_apache(port=8080)  # Apache on port 8080
#start_nginx(port=8080)  # Nginx on port 8080
