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

class SimpleSerializer(object):
  def __init__(self):
    """
    objs = dictionary to map a control name to a control object
    model= dictionary to map a control name to a control value
    """
    self.objs = {}
    self.model= {}

  def register(self, name, control, getvalue_method, setvalue_method):
    """
    only controls that are explicitly registered are serialized
    """
    self.objs[name] = (control, getvalue_method, setvalue_method)

  def ui_to_model(self):
    """
    collect ui state into the internal model
    """
    for name in self.objs:
      control, getvalue, setvalue = self.objs[name]
      self.model[name] = getvalue(control)
    return self.model

  def model_to_ui(self, model):
    """
    update ui from internal model
    """
    for name in self.objs:
      control, getvalue, setvalue = self.objs[name]
      setvalue(control, model[name])

