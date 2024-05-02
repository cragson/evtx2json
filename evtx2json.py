#!/usr/bin/env python3

import Evtx.Evtx as evtx

import os
import xmltodict
import json

def json_to_file( json_file_name, json_data ):

    if (os.path.splitext( json_file_name )[1] == ".json"):
        json_file=json_file_name
    else:
        json_file=json_file_name +".json"

    with open(json_file,"w") as outfile:
        outfile.write(json_data)

    outfile.close()

def convert_evtx_to_json( EVTX_PATH ):

    with evtx.Evtx( EVTX_PATH ) as log:

        final_dict=[]

        # Loop through each record in the evtx log
        for record in log.records():

            # Convert the record to a dictionary for ease of parsing
            data_dict=xmltodict.parse(record.xml())
            if data_dict.get('Event', {}).get('EventData') is not None:
                event_combined = {
                    "System": data_dict['Event']['System'],
                    "EventData": data_dict['Event']['EventData']
                }
               
            else:
                event_combined = {
                    "System": data_dict['Event']['System'],
                }

            final_dict.append(event_combined)
           
    return json.dumps(final_dict, indent=4, default=str)
        
def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Converts an windows event log file (evtx) to an json file.")
    parser.add_argument("evtx", type=str,action='store',
                        help="Path to the Windows EVTX event log file")
    parser.add_argument("-o","--output",type=str, action='store',
                        help="Path of output JSON file")
    args = parser.parse_args()
    
    evtx_json = convert_evtx_to_json( args.evtx )

    json_to_file( args.output )
   
if __name__ == "__main__":
    main()