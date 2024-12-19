# ARP Spoofing Script

This Python script demonstrates ARP spoofing, a method to intercept network traffic by sending falsified ARP (Address Resolution Protocol) messages. The script sends ARP packets to a target device and a gateway, enabling traffic redirection.

## Disclaimer

This script is provided for **educational purposes only**. Unauthorized use of ARP spoofing to intercept or disrupt network traffic is illegal and unethical. Ensure you have explicit permission to test and demonstrate this script in a controlled and authorized environment.

**Use responsibly and at your own risk.**

---

## Requirements

This script requires the following:

- Python 3
- `scapy` library (can be installed via `pip install scapy`)
- Administrator/root privileges

---

## How It Works

1. **Get MAC Address:** The `getMAC` function sends an ARP request to retrieve the MAC address of a given IP address.
2. **Spoof:** The `spoof` function sends falsified ARP packets to the target device and the gateway, associating the attacker's machine with the gateway.
3. **Restore:** The `restore` function resets the ARP tables of the target and gateway to their original state after the attack.

---

## Usage

1. Clone or download this repository.
2. Replace `yourtargetip` and `yourgatewayip` in the script with the appropriate IP addresses.
   ```python
   target_IP = "yourtargetip"
   gateway_IP = "yourgatewayip"
   ```
3. Run the script with administrator/root privileges:
   ```bash
   sudo python3 arp_spoof.py
   ```
4. Stop the script with `CTRL + C`. The script will reset ARP tables automatically.

---

## Example

If your target device IP is `192.168.1.100` and your gateway IP is `192.168.1.1`, update the script as follows:

```python
# Replace placeholders with actual IP addresses
target_IP = "192.168.1.100"
gateway_IP = "192.168.1.1"
```

Then, execute the script:

```bash
sudo python3 arp_spoof.py
```

---

## Important Notes

- This script sends ARP packets continuously until interrupted.
- Ensure you run the script in a testing environment where you have permission.
- Intercepted data is **not** handled or displayed by this script. It only demonstrates ARP spoofing.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

