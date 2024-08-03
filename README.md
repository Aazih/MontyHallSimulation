
# Monty Hall Simulation

This is a quick and dirty python program to simulate multiple runs of the Monty hall program. It has been tested on the online Python interpreter as of August 2024 at the site [Online-Python](https://www.online-python.com/)

## Monty Hall Problem

An explanation of the Monty Hall Problem can be found, as of August 2024, at [Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem)

## Features

* Interactive entry of number of doors in the simulation
* Interactive entry of number of times to simulate
* Automatically pseudo-randomly pick door for initial guess, door with prize, and door to eliminate.
* Automatically pseudo-randomly pick swapped door, as well as a new door guessed after a door has been eliminated.
* Publish statistics on how many times the first picked door, the swapped picked door, and the second randomly picked door from a smaller pool of doors won. This compares three strategies for after a door is eliminated, retain original choice, swap choice, and randomly pick from remaining doors after door is eliminated.

## Instructions

* Copy/paste code from montyhall_simulation.py into an online python interpreter such as [Online-Python](https://www.online-python.com/)
* Run program and follow prompts

## TODO

* ~~Extend program to provide option on how many doors to eliminate when running for more than 3 doors~~
* Error checking on interactive prompts.

## ChangeLog

* 2024-Aug-03_1: Initial version
* 2024-Aug-03_2: Add code comments and minor updates to print statements
* 2024-Aug-03_3: Added feature to eliminate more than one door.
