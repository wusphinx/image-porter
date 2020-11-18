#!/usr/bin/python3

import sys 
import os 
import subprocess 

class ImagePorter:
    def __init__(self, filepath: str) -> None:
        self.s2d = dict()
        with open(filepath) as fp:
            for line in fp:
                if not line.startswith("#"):
                    src, dst = line.split(",")
                    self.s2d[src.strip()]= dst.strip()
    
    def handle(self):
        for src, dst in self.s2d.items():
            subprocess.run(["docker", "pull", src]) 
            subprocess.run(["docker", "tag", src, dst]) 
            subprocess.run(["docker", "push", dst]) 
            
def main():
    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit() 

    ImagePorter(filepath=filepath).handle()
    

if __name__ == '__main__':
    main()