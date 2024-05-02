# evtx2json
Hi! Have you ever dealt with a huge amount of Windows Event Logs that you needed to check for certain Indicators of Compromise (IOCs)?

**Say no more!** This Python program takes a Windows Event Log file (.evtx) and converts it into a JSON file, which you can then ingest into your own pipeline and work with.

**No complicated setup, no annoying fiddling required—it just works out of the box!**



# Prerequisites
1. `pip install python-evtx`
2. `pip install xmltodict`
3. `pip install argparse`

# Usage
    evtx2json.py [-h] [-o OUTPUT] evtx 
   
    evtx2json.py -o Security-converted.json Security.evtx
