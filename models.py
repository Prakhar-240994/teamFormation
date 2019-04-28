# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:55:24 2019

@author: Prakhar
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

class Member(db.Model):
    __tablename__ = 'member'
    pid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    occupation = db.Column(db.String(30))
    prev_projects  = db.Column(db.Boolean)
    experience = db.Column(db.Integer)
    time_commitment = db.Column(db.String(10))

    def __init__(self, name, email, occupation, prev_projects, experience, time_commitment):
        self.name = name
        self.email = email
        self.occupation = occupation
        self.prev_projects = prev_projects
        self.experience = experience
        self.time_commitment = time_commitment

class Interests(db.Model):
    __tablename__ = 'interests'
    pid = db.Column(db.Integer, primary_key = True)
    aoi = db.Column(db.String(100))

    def __init__(self, pid, aoi):
        self.pid = pid
        self.aoi = aoi

    def splitInterests(pid, interests):
        interestList = list()
        tempList = interests.split(';')
        for interest in tempList:
            interestList.append(Interests(int(pid), interest))
        return interestList

class WorkedOn(db.Model):
    __tablename__ = 'workedon'
    pid = db.Column(db.Integer, primary_key = True)
    worked = db.Column(db.String(100))

    def __init__(self, pid, worked):
        self.pid = pid
        self.worked = worked

    def splitWorks(pid, works):
        workedList = list()
        tempList = works.split(';')
        for work in tempList:
            workedList.append(WorkedOn(int(pid), work))
        return workedList

class Teams(db.Model):
    __tablename__ = 'teams'
    tid = db.Column(db.Integer, primary_key = True)
    pid = db.Column(db.Integer)

    def __init__(self, pid):
        self.pid = pid
