#!/usr/bin/env python
import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_base import Base

from flask import Flask, jsonify
from flask.ext.restful import Api, Resource, reqparse
from rdns import rdns
from json_encoder import CustomJSONEncoder
import flask.ext.restful.representations.json

engine = create_engine('sqlite:///sqlite.db')
Base.metadata.create_all(engine, checkfirst=True)
DBSession = sessionmaker(bind=engine)
db = DBSession()

app = Flask(__name__)
api = Api(app)

flask.ext.restful.representations.json.settings["cls"] = CustomJSONEncoder

class rdnsList(Resource):
  def get(self):
    entries = db.query(rdns).all()
    if entries:
      return entries
    else:
      return "NOT_FOUND", 404

class rdnsAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('rdns', type = rdns, required = True, location = 'json')
    super(rdnsAPI, self).__init__()

  def get(self, ip):
    try:
      return db.query(rdns).filter(rdns.ip == ip).one()
    except:
      return "IP_NOT_FOUND", 404

  def post(self, ip):
    request = self.reqparse.parse_args().rdns

    if ( ip != request.ip ):
      return "pls use the same ip in url and request", 400

    try:
      entry = db.query(rdns).filter(rdns.ip == request.ip).one()
    except:
      entry = False

    if entry:
      print "updating"
      entry.ptr = request.ptr
      db.commit()
      return entry

    else:
      print "adding"
      db.add(request)
      db.commit()
      return "", 201

  def put(self, ip):
    self.post(ip)

  def delete(self, ip):
    try:
      entry = db.query(rdns).filter(rdns.ip == ip).one()
    except:
      return "IP_NOT_FOUND", 404

    db.delete(entry)
    db.commit()

api.add_resource(rdnsList, '/rdns')
api.add_resource(rdnsAPI, '/rdns/<string:ip>')

if __name__ == '__main__':
  app.run(debug=True)
