# Check User Specified Website is UP
# Martin Thorpe 21.04.2016
#
# If specified website is DOWN, lets check
# google to verify because google is never down
import requests
import sys

# Query the site presented at command line
try:
        r = requests.get(sys.argv[1], timeout=3)
        webstat = r.status_code
except:
        # Issue here, lets log it as a 404
        webstat = 404

# If the site is down lets do some verification before we
# raise the alarm

if webstat != 200:

# Lets try and reach google.co.uk
        try:
                r = requests.get('http://www.google.co.uk', timeout=3)
                webstat = r.status_code
        except:
                webstat = 404

        if webstat != 404:
                print ("CRITICAL: There is a problem with %s.") % sys.argv[1]
                sys.exit(2)
        else:
                print ("WARNING: The outside world is not reachable from this host")
                sys.exit(1)
else:
        print ("OK: The website %s is UP") % sys.argv[1]
        sys.exit(0)
