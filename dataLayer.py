# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:13:36 2019

@author: Prakhar
"""

from flask_mysqldb import MySQL

class Data():

    def insert(member, conn):
        cur = conn.cursor()
        query = '''INSERT INTO member(name, email, occupation, prev_projects, experience, time_commitment) VALUES (%s, %s, %s, %s, %s, %s)'''
        if member.prev_projects=='True':
            member.prev_projects = 1
        else:
            member.prev_projects= 0

        vals = (member.name,member.email,member.occupation,str(member.prev_projects),member.experience,member.time_commitment)
        cur.execute(query, vals)
        rows = cur.rowcount
        conn.commit()
        cur.close()
        return rows

    def getId(conn):
        cur = conn.cursor()
        query = '''SELECT pid FROM member ORDER BY pid DESC LIMIT 1'''
        cur.execute(query)
        pid = cur.fetchall()
        #print(pid[0][0])
        return pid[0][0]

    def insertInterests(listOfInterests, conn):
        cur = conn.cursor()
        query = '''INSERT INTO interests(pid, aoi) VALUES (%s, %s)'''
        for interest in listOfInterests:
            vals = (int(interest.pid), interest.aoi)
            cur.execute(query, vals)
        rows = cur.rowcount
        conn.commit()
        cur.close()
        return rows

    def insertWorkedOn(listOfWorks, conn):
        cur = conn.cursor()
        query = '''INSERT INTO workedon(pid, worked) VALUES (%s, %s)'''
        for work in listOfWorks:
            vals = (int(work.pid), work.worked)
            cur.execute(query, vals)
        rows = cur.rowcount
        conn.commit()
        cur.close()
        return rows

    def getMembers(conn):
        cur = conn.cursor()
        query = '''SELECT COUNT(*) FROM member'''
        cur.execute(query)
        noOfMembers = cur.fetchall()
        return int(noOfMembers[0][0])

    def getExperienced(conn):
        cur = conn.cursor()
        query = '''SELECT COUNT(*) FROM member WHERE experience >= 4'''
        cur.execute(query)
        noOfExperienced = cur.fetchall()
        return int(noOfExperienced[0][0])

    def getArchitects(conn):
        cur = conn.cursor()
        query = '''SELECT COUNT(*) FROM member WHERE prev_projects = true'''
        cur.execute(query)
        noOfArchitects = cur.fetchall()
        return int(noOfArchitects[0][0])
