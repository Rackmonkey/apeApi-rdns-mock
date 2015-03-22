import socket
import re
from sqlalchemy import *
from db_base import Base

class rdns(Base):
  __tablename__ = 'rdns'

  ip = Column(String(45), primary_key=True)
  ptr = Column(String(254), nullable=False)

  def __init__(self, values):
    self.ip = values['ip']
    self.ptr = values['ptr']
    if ( not self.is_valid() ):
      raise ValueError('INVALID_INPUT ')

  def is_valid(self):
    return self.is_valid_ip() and self.is_valid_ptr()

  def is_valid_ip(self):
    try:
      socket.inet_aton(self.ip)
    except socket.error:
      return False
    return True

  def is_valid_ptr(self):
    if self.ptr == "":
      return True

    hostname = self.ptr
    if len(hostname) > 255:
      return False
    if hostname[-1] == ".":
      hostname = hostname[:-1]
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))

  def __dict__(self):
    return {'rdns': {'ip': self.ip, 'ptr': self.ptr}}
