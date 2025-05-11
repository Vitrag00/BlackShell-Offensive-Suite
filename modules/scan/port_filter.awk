# Filters only open ports from an Nmap output
/^([0-9]+\/tcp|udp)/ {
    if ($2 == "open") {
        print $0
    }
}
