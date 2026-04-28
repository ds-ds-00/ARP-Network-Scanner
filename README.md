#  ARP Network Scanner

A fast and lightweight Python-based network scanner that discovers devices on your local network using ARP requests.

---

##  Features

* 📡 Scan local network using ARP
* 🖥️ Discover live hosts (IP + MAC)
* 🏢 Vendor detection (MAC → Company)
* 📊 Clean tabulated output (CLI + file)
* 💾 Save results to file
* ⚙️ Simple CLI interface

---

## 🛠️ Tech Stack

* Python 3
* Scapy
* Tabulate
* Requests

---

## 📦 Installation

```bash
git clone https://github.com/ds-ds-00/ARP-Network-Scanner.git
cd ARP-Network-Scanner
pip install -r requirements.txt
```

---

## ⚠️ Windows Users

You must install **Npcap**:

👉 https://npcap.com/#download

During installation:

*  Enable WinPcap compatibility mode
*  Run the script with Administrator privileges
*  Recommend os is linux 

---

## ▶️ Usage

```bash
python network-scanner.py -i 192.168.1.0/24
```

### With output file:

```bash
python network-scanner.py -i 192.168.1.0/24 -o results.txt
```

---

## 📊 Example Output

```
+----------------+-------------------+---------------------------+
| IP             | MAC               | Vendor                    |
+================+===================+===========================+
| 192.168.29.1   | 04:xx:56:f9:xx:xx | Arcadyan Corporation      |
+----------------+-------------------+---------------------------+
| 192.168.29.14  | 48:xx:48:d2:xx:xx | Earda Technologies co Ltd |
+----------------+-------------------+---------------------------+
| 192.168.29.127 | 9a:xx:46:a2:xx:xx | Unknown                   |
+----------------+-------------------+---------------------------+
| 192.168.29.205 | 9c:xx:d3:c3:xx:xx | AzureWave Technology Inc. |
+----------------+-------------------+---------------------------+
| 192.168.29.198 | 1a:xx:be:b5:xx:xx | Unknown                   |
+----------------+-------------------+---------------------------+
```

---

## 📂 Project Structure

```
network-scanner/
│── network_scanner.py
│── requirements.txt
│── README.md
```

---

## ⚠️ Disclaimer

This tool is created for **educational and ethical purposes only**.
Do not use it on networks without permission.

---

## ⭐ Support

If you like this project:

* Star ⭐ the repo
* Fork 🍴 it
* Contribute 🚀

---
