from ipaddress import ip_address

try:
    ip = ip_address(input("Enter an IP address: ").strip())

    print(ip)

    if ip.is_global:
        print("Globally routable IP")
    else:
        print("Not globally routable IP")

except ValueError:
    print("Please enter a valid IP address")
