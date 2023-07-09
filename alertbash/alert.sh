#!/bin/bash

almost_full=85
recipient="anton.bosenko109@gmail.com"

disk_info=$(df -h /)
used_percent=$(echo "$disk_info" | awk 'NR==2{print $5}' | tr -d '%')

if ((used_percent >= almost_full)); then

    subject="Disk Space Alert: ${used_percent}% used"
    body="The disk is ${used_percent}% full."

    echo -e "Subject:${subject}\n${body}" | ssmtp "${recipient}"
fi
