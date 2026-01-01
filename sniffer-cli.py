import argparse 
import os 
from pathlib import Path 
import json
from datetime import datetime as dt 

valid_protocols = ("TCP", "UDP", "ARP")

def sniff(protocol='TCP', count=1): 
    packets = {
        'protocol':None,
        'source':None, 
        'destination':None,  
        'data':None
    }

    while len(packets) < int(count): 
        print("actively sniffing")
        # do work here 

    

    return packets

def save_results(path, data):
    timestamp = dt.now().isoformat()
    path = path / f'data_{timestamp}.json'
    path.write_text(json.dumps(data))

def display_results(packets):
    # TODO - need to fix the formatting of this with the expectation of a dictionary of many results 
    print("/=========================================\\")
    print("|================ RESULTS =================|")
    print("|==========================================|")
    print("| Protocol | Source | Destination | Data |")
    for k, v in packets.items(): 
        print(f"| {k} : {v} |")
    print("\\=========================================/")


def get_arguments():
    parser = argparse.ArgumentParser(prog='sniffer-cli',description='sniffs packets')
    parser.add_argument('-c', '--count')      
    parser.add_argument('-s', '--save-results', action='store_true')      
    parser.add_argument('-p', '--protocol', type=str, default="TCP")  
    return parser.parse_args()

def validate_args(args): 
    if isinstance(args.count, int):
        print(f"TypeError for value past for count: {args.count}")
        exit(1)
    if args.protocol not in valid_protocols:
        print(f"Protocol not valid: {args.protocol}")
        print(f"Valid Protocols: ")
        for p in valid_protocols:
            print(p)
        exit(1)

def main():
    args = get_arguments() 
    validate_args(args)
    try: 
        results = sniff(protocol=args.protocol, count=args.count)
    except Exception as e: 
        print(f"There was an exception: {str(e)}")
        exit(1)

    if args.save_results: 
        base = Path(__file__).parent
        save_path = base / "saves"
        if not save_path.exists():
            save_path.mkdir(parents=True, exist_ok=True)
        save_results(save_path, results)
    
    display_results(results)
    

if __name__ == "__main__":
    main() 