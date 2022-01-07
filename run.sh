#!/bin/sh
python transmitter.py 16 1 firstSignal.txt
python transmitter.py 16 2 secondSignal.txt
python transmitter.py 16 3 thirdSignal.txt
python channel.py
python receiver.py
