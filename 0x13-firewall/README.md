# 🚀 Web Server Firewall Setup with UFW 🚀

Welcome to the **Web Server Firewall Setup** guide! This guide will help you secure your web server (`web-01`) using the **UFW** firewall. 🛡️

## 📝 Requirements

- Install **UFW** (Uncomplicated Firewall).
- Block all incoming traffic, except for the following TCP ports:
  - **22 (SSH)** 🔑
  - **80 (HTTP)** 🌐
  - **443 (HTTPS)** 🔒

## 📋 Setup Instructions

Follow these steps to install and configure UFW on your server.

### 1. Update Package Lists 🔄

```bash
sudo apt-get update
2. Install UFW 🛠️sudo apt-get install ufw3. Allow SSH (Port 22) 🔑sudo ufw allow 22/tcp4. Allow HTTP (Port 80) 🌐sudo ufw allow 80/tcp5. Allow HTTPS (Port 443) 🔒sudo ufw allow 443/tcp6. Enable UFW ✅sudo ufw enable7. Check UFW Status 📊sudo ufw status🎉 Congratulations!Your web server is now secured with UFW, allowing only the necessary ports for SSH, HTTP, and HTTPS traffic. Enjoy your secure server! 🚀📧 SupportIf you need any help, feel free to reach out to us! We're here to assist you. 😊Made with ❤️ by YUSUF MM
