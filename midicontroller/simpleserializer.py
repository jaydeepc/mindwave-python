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

  def model_to_ui(self):
    """
    update ui from internal model
    """
    for name in self.objs:
      control, getvalue, setvalue = self.objs[name]
      setvalue(control, self.model[name])

  def to_string(self):
    import json
    return json.dumps(self.model, sort_keys=True,
                      indent=4, separators=(',', ': '))

  def from_string(self, string):
    import json
    self.model = json.loads(string)

