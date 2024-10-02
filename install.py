#!/bin/bash
# Installation script for autoTOR

echo "[+] Do you want to install Auto TOR IP changer? (y/n)"
read choice

if [[ $choice == "Y" || $choice == "y" ]]; then
    # Give execution permissions to the Python file
    chmod 777 autoTOR.py

    # Create the directory and move the Python file there
    mkdir -p /usr/share/aut/
    cp autoTOR.py /usr/share/aut/

    # Create a shell script in /usr/bin/ to allow running the Python file via 'aut' command
    echo "#!/bin/bash" > /usr/bin/aut
    echo "python3 /usr/share/aut/autoTOR.py" >> /usr/bin/aut

    # Set the necessary permissions
    chmod +x /usr/bin/aut
    chmod +x /usr/share/aut/autoTOR.py

    echo "[+] Auto TOR IP changer installed successfully. Run it using the command: aut"
else
    echo "[+] Installation aborted."
fi
