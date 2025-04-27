Python DDoS Attack Script

A basic Python script to simulate a DDoS attack. You can use this to test the Golang DDoS protection server.

Installation

1. Install Python:
If you don't have Python installed, download it from the official Python website: https://www.python.org/downloads/.


2. Clone the repository:

git clone https://github.com/ryyyawh/ddos-attack.git
cd ddos-simple


3. Install required dependencies:

pip install requests


How To Usage?

1. To simulate an attack, run the ddos_attack.py script by specifying the target server URL (in this case, your Golang server running locally on port 8080):

python ddos_attack.py http://localhost:8080


2. The script will begin sending HTTP GET requests to the target URL to simulate an HTTP flood.



How It Works

The script uses requests to send HTTP GET requests continuously to the target server.

The target server will have protection mechanisms like rate limiting and CAPTCHA to mitigate the attack.



---

Conclusion

This repository provides two essential components for handling DDoS attacks:

A DDoS Protection Server built using Golang that includes multiple techniques such as rate limiting, IP blocking, and CAPTCHA to protect against attacks.

A DDoS Attack Script written in Python to simulate attacks for testing the server's defenses.


To further enhance the protection, consider integrating cloud-based DDoS protection services such as Cloudflare or AWS Shield.

Let me know if you have any questions or need further modifications!


---

©® Xylays Developer
