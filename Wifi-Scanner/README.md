# WIFI Scanner

Note: Works only on Mac OS

---

## Description

This is a simple wifi scanner that uses the `airport` command line tool to scan for wifi networks and displays them in a table view. Airport is a command line tool that comes with Mac OS X and is located in `/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport`

---

## Inspiration

The idea behind this project is inspired from [Charalampos](https://github.com/CharalamposMoutsios/wifi_scanner)

---

## Usage

'python wifi_networks.py'

---

## Requirements

- It uses the `airport` command line tool, which is only available on Mac OS
- Python of course
- No external libraries are required

---

## Output

Available Wi-Fi Networks:
| Network Name | BSSID | RSSI | Channel | Security |
| --- | --- | --- | --- | --- |
| Zulu | 3c:7c:3f:e7:59:28 | -57 | 11 | WPA2(PSK/AES/AES) |
| Pesto | 70:8b:cd:e6:94:28 | -60 | 12 | WPA2(PSK/AES/AES) |
| Omni_7E1728 | 34:21:09:7e:17:31 | -60 | 11 | WPA2(PSK,FT-PSK/AES/AES) |

---
