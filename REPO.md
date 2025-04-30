# Software Quality Assurance Activities Report

## Activities Performed
- Uploaded project to GitHub
- Created Git Hooks for Bandit static analysis
- Created fuzz.py to fuzz 5 functions
- Added forensic logging in 5 methods
- Used the same 5 methods for the fuzzing and the forensics
from scanner  isValidUserName, isValidPasswordName
from parser getValuesRecursively, checkIfValidHelm
from graphtaint getYAMLFiles
- Set up GitHub Actions to run fuzz.py automatically
- Made a test script for the forensics
## Lessons Learned
- How Git hooks can enforce automatic security checks
- How to use more of githubs features
- How fuzz testing helps find random bugs and edge cases
- Importance of forensic logging for incident response
- How to automate testing pipelines with GitHub Actions
