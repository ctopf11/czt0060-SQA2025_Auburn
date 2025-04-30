import random
import sys
import os

# Force Python to look in the current folder
sys.path.append(os.path.dirname(__file__))

from scanner import isValidUserName, isValidPasswordName
from parser import getValuesRecursively, checkIfValidHelm
from graphtaint import getYAMLFiles


def fuzz(func):
    for _ in range(50):
        try:
            arg = random.choice([
                "",
                "admin",
                "user123",
                "a" * 500,
                None,
                123,
                True,
                False,
                [],
                {},
                "!@#$%",
                "\n\t",
                "username with spaces",
                lambda x: x,     
                set([1,2,3]) 
            ])
            result = func(arg)
            print(f"[OK] {func.__name__}({arg}) => {result}")
        except Exception as e:
            print(f"[BUG] {func.__name__}({arg}) => {e}")

if __name__ == "__main__":
    fuzz(isValidUserName)
    fuzz(isValidPasswordName)
    fuzz(getValuesRecursively)
    fuzz(getYAMLFiles)
    fuzz(checkIfValidHelm)
    



