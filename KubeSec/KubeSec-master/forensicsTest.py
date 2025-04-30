import logging
from scanner import isValidUserName, isValidPasswordName
from parser import getValuesRecursively, checkIfValidHelm
from graphtaint import getYAMLFiles

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Test isValidUserName
isValidUserName("admin")
isValidUserName(None)
isValidUserName("!@#$%")

# Test isValidPasswordName
isValidPasswordName("user123")
isValidPasswordName(None)
isValidPasswordName("!@#$%")

# Test getValuesRecursively
list(getValuesRecursively({"key": ["val1", {"nested": "val2"}]}))
list(getValuesRecursively([]))
list(getValuesRecursively("simple_value"))

# Test checkIfValidHelm
checkIfValidHelm("helm chart values")
checkIfValidHelm("random text")
checkIfValidHelm(None)

#testing to get yaml files 
getYAMLFiles("TEST_ARTIFACTS")
