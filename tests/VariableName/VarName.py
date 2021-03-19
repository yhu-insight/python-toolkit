# -*- coding: utf-8 -*-

# Python __name__ module Test
# Author - yucheng.hu@insight.com

import ImportVarName

print("Main VarName __name__ = %s" % __name__)

if __name__ == "__main__":
    print("VarName is being run directly")
else:
    print("VarName is being imported")
