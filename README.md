# thoughtful_technical

## Description

a robotic sorting function for dispatching packages based on volume and mass.

## Python Version
Requires version 3.10 or higher because of the match statement in sort function.

## To Run Function and Test
`python sort.py`

## The Problem

each package must be dispatched to one of three categories:

- **STANDARD**: not bulky and not heavy  
- **SPECIAL**: bulky or heavy (but not both)  
- **REJECTED**: both bulky and heavy



### Definitions

- a package is **bulky** if:
  - its volume (width × height × length) is ≥ 1,000,000 cm³  
  - or any single dimension is ≥ 150 cm  
- a package is **heavy** if its mass is ≥ 20 kg



## Solution
```
sort(width: float, height: float, length: float, mass: float) -> DispatchCategory

where DispatchCategory is an enum with values Standard, Special, Rejected
```