##################################################################################
#      This file is part of mindwave-python.                                     #
#                                                                                #
#      mindwave-python is free software: you can redistribute it and/or modify   #
#      it under the terms of the GNU General Public License as published by      #
#      the Free Software Foundation, either version 3 of the License, or         #
#      (at your option) any later version.                                       #
#                                                                                #
#      mindwave-python is distributed in the hope that it will be useful,        #
#      but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#      GNU General Public License for more details.                              #
#                                                                                #
#      You should have received a copy of the GNU General Public License         #
#      along with mindwave-python.  If not, see <http://www.gnu.org/licenses/>.  #
##################################################################################

import os.path
import sys

def getInstallPath():
    thePath = os.path.dirname(sys.argv[0])
    if thePath:
        thePath += os.sep
    else:
        thePath = "./"
    return os.path.abspath(thePath)

if __name__ == "__main__":
    print "INSTALLATION PATH: getInstallPath()"
    print "{0}/synthconfig/linuxsampler.lscp".format(getInstallPath())

    with open("{0}/synthconfig/linuxsampler.lscp.template".format(getInstallPath()), "r") as f:
      lines = f.readlines()

    with open("{0}/synthconfig/linuxsampler.lscp".format(getInstallPath()), "w") as f:
      for l in lines:
        l = l.replace("#####", getInstallPath()+"/sonatina")
        f.write(l)

