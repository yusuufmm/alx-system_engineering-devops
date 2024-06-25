# 🚀 Web Server Firewall Setup with UFW 🚀

Welcome to the **Web Server Firewall Setup** guide! This guide will help you secure your web server (`web-01`) using the **UFW** firewall and configure port forwarding. 🛡️

## 📝 Requirements

- Install **UFW** (Uncomplicated Firewall).
- Block all incoming traffic, except for the following TCP ports:
  - **22 (SSH)** 🔑
  - **80 (HTTP)** 🌐
  - **443 (HTTPS)** 🔒
- Redirect **port 8080/TCP** to **port 80/TCP**.

## 📋 Setup Instructions

Follow these steps to install and configure UFW on your server.

### 1. Update Package Lists 🔄

```bash
sudo apt-get update
```

### 2. Install UFW 🛠️

```bash
sudo apt-get install ufw
```

### 3. Allow Necessary Ports ✅

```bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 8080/tcp
```

### 4. Enable UFW 🛡️

```bash
sudo ufw enable
```

### 5. Enable IP Forwarding in the Kernel 🌐

Edit the `/etc/ufw/sysctl.conf` file:

```bash
sudo nano /etc/ufw/sysctl.conf
```

Uncomment or add the following line:

```bash
net/ipv4/ip_forward=1
```

### 6. Edit UFW Before Rules 📝

Edit the `/etc/ufw/before.rules` file:

```bash
sudo nano /etc/ufw/before.rules
```

Add the following lines at the top of the file, right after the header comments:

```bash
# Start redirecting port 8080 to 80
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
# End redirecting port 8080 to 80
```

### 7. Reload UFW ♻️

Reload UFW to apply the changes:

```bash
sudo ufw disable
sudo ufw enable
```

### 8. Check UFW Status 📊

Verify that UFW is active and the rules are in place:

```bash
sudo ufw status
```

## 🎉 Congratulations!

Your web server is now secured with UFW, allowing only the necessary ports for SSH, HTTP, and HTTPS traffic. Port 8080 is also successfully redirected to port 80. Enjoy your secure server! 🚀

## 📧 Support

If you need any help, feel free to reach out to us! We're here to assist you. 😊

---

Made with ❤️ by YUSUF MM (@yusuufmm.github)
