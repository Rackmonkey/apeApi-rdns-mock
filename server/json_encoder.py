from flask.json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
  def default(self, obj):
    op = getattr(obj, "__dict__", None)
    if callable(op):
      return obj.__dict__()
    return super(CustomJSONEncoder, self).default(obj)
