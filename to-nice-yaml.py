#!/usr/bin/python3

import sys
import yaml
import ansible.plugins.filter.core

INFILE = sys.argv[1]
OUTFILE = sys.argv[2]
with open(INFILE) as infh:
    inyaml = yaml.safe_load(infh)
with open(OUTFILE, "w") as outfh:
    outfh.write(ansible.plugins.filter.core.to_nice_yaml(inyaml))
