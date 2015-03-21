from flask.json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
  def default(self, obj):
    op = getattr(obj, "__json__", None)
    if callable(op):
      return obj.__json__()
    return super(MyJSONEncoder, self).default(obj)
