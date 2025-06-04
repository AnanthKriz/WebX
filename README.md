**webX** is a lightweight web vulnerability reconnaissance tool developed in Python for ethical hackers and penetration testers.  
It helps detect **open ports**, check **HTTP headers**, and perform **basic directory brute-forcing** on a target web server.

> ✨ Developed by **AnanthKriz**

---

## 📌 Features

- Port scanning of common service ports
- HTTP header information grabber
- Simple directory brute-force with default wordlist
- ASCII logo and easy-to-use command-line interface

---

## 🧠 Purpose of the Tool

webX is designed to assist in **early-stage information gathering** and **vulnerability detection** during web application assessments.

It is a useful script for:

- Bug bounty hunters
- CTF players
- Students learning ethical hacking
- System administrators testing their own infrastructure

---

## ⚙️ Supported Platforms

You can install and run `webX` on:

- ✅ **Termux (Android CLI)**
- ✅ **Kali Linux**
- ✅ **Parrot OS**
- ✅ **Windows (using Python)**

---

## 💾 Installation

### 🐧 On **Termux**:

```bash
pkg update && pkg install python git -y
pip install requests
git clone https://github.com/AnanthKriz/webX.git
cd webX
python webX.py example.com
🐍 On Kali Linux / Parrot OS:
bash
Copy code
sudo apt update && sudo apt install python3 git -y
pip3 install requests
git clone https://github.com/AnanthKriz/webX.git
cd webX
python3 webX.py example.com
🪟 On Windows:
Install Python from https://www.python.org

Open Command Prompt or PowerShell:

bash
Copy code
pip install requests
git clone https://github.com/AnanthKriz/webX.git
cd webX
python webX.py example.com
🚀 Usage
bash
Copy code
python webX.py <target>
📌 Example:

bash
Copy code
python webX.py testphp.vulnweb.com
📂 Example Output
csharp
Copy code
__        __   _     __  __
\ \      / /__| |__ |  \/  | ___ _ __  _   _
 \ \ /\ / / _ \ '_ \| |\/| |/ _ \ '_ \| | | |
  \ V  V /  __/ |_) | |  | |  __/ | | | |_| |
   \_/\_/ \___|_.__/|_|  |_|\___|_| |_|\__,_|

        webX - Web Vuln Scanner
        Developed by AnanthKriz

[*] Scanning ports on testphp.vulnweb.com...
[+] Port 80 is OPEN

[*] Checking HTTP headers for http://testphp.vulnweb.com...
Server: Apache
X-Powered-By: PHP/5.6.40

[*] Starting directory brute force on http://testphp.vulnweb.com...
[+] Found directory: http://testphp.vulnweb.com/admin
👤 Author
AnanthKriz
📫 GitHub: github.com/AnanthKriz

⚠️ Disclaimer
This tool is created for educational and authorized testing only.
Do not use against systems you do not own or have permission to test.
You are responsible for your actions.

yaml
Copy code

---

### ✅ What to Do Next:

1. Save this as `README.md` in the `webx` folder.
2. Add and push it to GitHub:

```bash
cd webx
git add README.md
git commit -m "Added README file with usage and install instructions"
git push origin main
Would you like me to help you add a license (like MIT or GPL), or make a .sh installer for Termux or Linux?


You said:
Yes

ChatGPT said:
Awesome! Let's add the following to your webX project:

📄 1. LICENSE File (MIT Recommended for Tools)
MIT is a permissive open-source license. Anyone can use, modify, and distribute your tool, with credit.

📜 LICENSE (MIT)
text
Copy code
MIT License

Copyright (c) 2025 AnanthKriz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND...
➕ Add it to your repo:
bash
Copy code
cd webx
nano LICENSE   # Paste the above license
git add LICENSE
git commit -m "Added MIT License"
git push origin main
🛠️ 2. Termux/Linux Installer Script (install.sh)
This script installs dependencies, clones the repo, and sets it up for quick use.

🐚 install.sh (inside webx/)
bash
Copy code
#!/bin/bash

echo "Installing webX..."
sleep 1

# Install dependencies
if [ -x "$(command -v pkg)" ]; then
    pkg update && pkg install python git -y
elif [ -x "$(command -v apt)" ]; then
    sudo apt update && sudo apt install python3 git -y
fi

# Clone and set up
git clone https://github.com/AnanthKriz/webX.git
cd webX
pip install requests || pip3 install requests

echo "✅ webX installed successfully!"
echo "📌 Run it using: python3 webX.py <target>"
➕ Make executable and push:
bash
Copy code
chmod +x install.sh
git add install.sh
git commit -m "Added install script for Termux and Linux"
git push origin main
✅ Optional: Make it a Global Command (webx)
If you'd like to run it like this:

bash
Copy code
webx example.com
You can create a symlink:

bash
Copy code
cd webx
chmod +x webX.py
ln -s $(pwd)/webX.py $PREFIX/bin/webx
Now you can run from anywhere:

bash
Copy code
webx example.com
✅ Summary of What's Now in Your Repo
webX.py → Your main tool

README.md → Description, usage, install guide

LICENSE → MIT license

install.sh → One-line installer for Termux/Linux

Would you like help making a banner, uploading the repo icon, or submitting it to GitHub Topics or tool lists?



**webX** is a lightweight web vulnerability reconnaissance tool developed in Python for ethical hackers and penetration testers.  
It helps detect **open ports**, check **HTTP headers**, and perform **basic directory brute-forcing** on a target web server.

> ✨ Developed by **AnanthKriz**

---

## 📌 Features

- Port scanning of common service ports
- HTTP header information grabber
- Simple directory brute-force with default wordlist
- ASCII logo and easy-to-use command-line interface

---

## 🧠 Purpose of the Tool

webX is designed to assist in **early-stage information gathering** and **vulnerability detection** during web application assessments.

It is a useful script for:

- Bug bounty hunters
- CTF players
- Students learning ethical hacking
- System administrators testing their own infrastructure

---

## ⚙️ Supported Platforms

You can install and run `webX` on:

- ✅ **Termux (Android CLI)**
- ✅ **Kali Linux**
- ✅ **Parrot OS**
- ✅ **Windows (using Python)**

---

## 💾 Installation

### 🐧 On **Termux**:

```bash
pkg update && pkg install python git -y
pip install requests
git clone https://github.com/AnanthKriz/webX.git
cd webX
python webX.py example.com
🐍 On Kali Linux / Parrot OS:
bash
Copy code
sudo apt update && sudo apt install python3 git -y
pip3 install requests
git clone https://github.com/AnanthKriz/webX.git
cd webX
python3 webX.py example.com
🪟 On Windows:
Install Python from https://www.python.org

Open Command Prompt or PowerShell:

bash
Copy code
pip install requests
git clone https://github.com/AnanthKriz/webX.git
cd webX
python webX.py example.com
🚀 Usage
bash
Copy code
python webX.py <target>
📌 Example:

bash
Copy code
python webX.py testphp.vulnweb.com
📂 Example Output
csharp
Copy code
__        __   _     __  __
\ \      / /__| |__ |  \/  | ___ _ __  _   _
 \ \ /\ / / _ \ '_ \| |\/| |/ _ \ '_ \| | | |
  \ V  V /  __/ |_) | |  | |  __/ | | | |_| |
   \_/\_/ \___|_.__/|_|  |_|\___|_| |_|\__,_|

        webX - Web Vuln Scanner
        Developed by AnanthKriz

[*] Scanning ports on testphp.vulnweb.com...
[+] Port 80 is OPEN

[*] Checking HTTP headers for http://testphp.vulnweb.com...
Server: Apache
X-Powered-By: PHP/5.6.40

[*] Starting directory brute force on http://testphp.vulnweb.com...
[+] Found directory: http://testphp.vulnweb.com/admin
👤 Author
AnanthKriz
📫 GitHub: github.com/AnanthKriz

⚠️ Disclaimer
This tool is created for educational and authorized testing only.
Do not use against systems you do not own or have permission to test.
You are responsible for your actions.

yaml
Copy code

---

### ✅ What to Do Next:

1. Save this as `README.md` in the `webx` folder.
2. Add and push it to GitHub:

```bash
cd webx
git add README.md
git commit -m "Added README file with usage and install instructions"
git push origin main
Would you like me to help you add a license (like MIT or GPL), or make a .sh installer for Termux or Linux?


You said:
Yes

ChatGPT said:
Awesome! Let's add the following to your webX project:

📄 1. LICENSE File (MIT Recommended for Tools)
MIT is a permissive open-source license. Anyone can use, modify, and distribute your tool, with credit.

📜 LICENSE (MIT)
text
Copy code
MIT License

Copyright (c) 2025 AnanthKriz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND...
➕ Add it to your repo:
bash
Copy code
cd webx
nano LICENSE   # Paste the above license
git add LICENSE
git commit -m "Added MIT License"
git push origin main
🛠️ 2. Termux/Linux Installer Script (install.sh)
This script installs dependencies, clones the repo, and sets it up for quick use.

🐚 install.sh (inside webx/)
bash
Copy code
#!/bin/bash

echo "Installing webX..."
sleep 1

# Install dependencies
if [ -x "$(command -v pkg)" ]; then
    pkg update && pkg install python git -y
elif [ -x "$(command -v apt)" ]; then
    sudo apt update && sudo apt install python3 git -y
fi

# Clone and set up
git clone https://github.com/AnanthKriz/webX.git
cd webX
pip install requests || pip3 install requests

echo "✅ webX installed successfully!"
echo "📌 Run it using: python3 webX.py <target>"
➕ Make executable and push:
bash
Copy code
chmod +x install.sh
git add install.sh
git commit -m "Added install script for Termux and Linux"
git push origin main
✅ Optional: Make it a Global Command (webx)
If you'd like to run it like this:

bash
Copy code
webx example.com
You can create a symlink:

bash
Copy code
cd webx
chmod +x webX.py
ln -s $(pwd)/webX.py $PREFIX/bin/webx
Now you can run from anywhere:

bash
Copy code
webx example.com
✅ Summary of What's Now in Your Repo
webX.py → Your main tool

README.md → Description, usage, install guide

LICENSE → MIT license

install.sh → One-line installer for Termux/Linux

Would you like help making a banner, uploading the repo icon, or submitting it to GitHub Topics or tool lists?



