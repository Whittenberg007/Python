import paramiko
import base64

def connect_to_sftp(host, port, username, private_key_path):
    # Create an SSH client instance
    ssh_client = paramiko.SSHClient()

    # Automatically add the server's host key (this is insecure and used for demonstration; see note below)
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #known_host_key = "AAAAB3NzaC1yc2EAAAADAQABAAABgQDOKIztoYZxEg7LLiRxZ1NwkSadtloIznqwjXoS++m2dMqZwcFNTfcIkPmgodL7woCRm3s7BeIVQLtEUaOw+0YaPNLFb4yYtDnUAbJqnkXYsCG7Wl7E9d/Xir5wopzUpSzCNagH39R9EiarseSKtNmh9CrE5aQdcBJRL0dOhTYFycAD6thjtcko3eCvG8GKUCL0x3S01/4cSPGw+Gt4phbvAuuUzb/idhq7FEbN2s73Gio4//nGeUKy+WKFpwo06h/eixKN33dpIl7w0UdkEq1aN1w9xbidHurWVZMTq3cVvuLyQKQQJTX6jve5/AQEdoJMc/n8yOBOh0p4WM1RNcKKo+rhNsE8kjrQgRVUIlM+y+9DbOXUPI0zn1IT9TSk4nPufehiR6rhX6cg3EIpBEZFAJCXYjZYrrprZ5/9Cg0klk0GXGSJFCV+uWqW+Y/HAS3peAgZsrTq0b1ecndZNaFioAdD8NIHnLIqI6jkI2ILPeprgQn2SGQJ4JhXYPdlD8U="
    #ssh_client.get_host_keys()#.add(host, 'ssh-rsa', paramiko.RSAKey(data=base64.decodebytes(known_host_key.encode())))


    # Load the private key
    mykey = paramiko.RSAKey(filename=private_key_path)

    # Connect to the server
    ssh_client.connect(host, port, username=username, pkey=mykey)

    # Open an SFTP session
    sftp = ssh_client.open_sftp()

    # Use the SFTP session (e.g., list the contents of the root directory)
    print(sftp.listdir('/'))
    
    # Download the file from the SFTP server
    remote_file_path = '/Test.txt'  # Path to the file on the SFTP server
    local_file_path = 'Test.txt'   # Path where you want to save the file on your local machine
    sftp.get(remote_file_path, local_file_path)
    remote_file_path = '/Second Test File.txt'  # Path to the file on the SFTP server
    local_file_path = 'Second Test File.txt'   # Path where you want to save the file on your local machine
    sftp.get(remote_file_path, local_file_path)
    print(f"Downloaded {remote_file_path} to {local_file_path}")

    # Close the SFTP session
    sftp.close()

    # Close the SSH client
    ssh_client.close()

# Example usage
connect_to_sftp('lazydogsecuritytestsftp.blob.core.windows.net', 22, 'lazydogsecuritytestsftp.test', 'C:\\Users\\whitt\\Downloads\\LazyPay_WF_KP.pem')
