from random import random as rand
from random import shuffle
import psycopg2
from qbutil import question
from configs import (postgresql_user, postgresql_password, postgresql_host, 
                     postgresql_port, postgresql_quizdb_name)
from numpy.random import binomial

#init postgresql connection
connection = psycopg2.connect(user = postgresql_user, 
                              password = postgresql_password,
                              host = postgresql_host,
                              port = postgresql_port,
                              database = postgresql_quizdb_name)
cursor = connection.cursor()

def get_random_tossup():
    cursor.execute('SELECT * FROM tossups ORDER BY random() LIMIT 1;')
    res = cursor.fetchone()
    return question(res[1], res[2])

def get_random_bonus():
    cursor.execute('SELECT * FROM bonus_parts ORDER BY random() LIMIT 1;')
    res = cursor.fetchone()
    return question(res[2], res[3])

def get_random_tossups(num):
    if num == 0: return []
    cmd = 'SELECT * FROM tossups ORDER BY random() LIMIT ' + str(num) + ';'
    cursor.execute(cmd)
    res = cursor.fetchall()
    return [question(quest[1], quest[2]) for quest in res]

def get_random_bonuses(num):
    if num == 0: return []
    cmd = 'SELECT * FROM bonus_parts ORDER BY random() LIMIT ' + str(num) + ';'
    cursor.execute(cmd)
    res = cursor.fetchall()
    return [question(quest[2], quest[3]) for quest in res]
    
def get_random_question(toss_freq = .25):
    return get_random_tossup() if rand() < toss_freq else get_random_bonus()

def get_random_questions(num, toss_freq = .25):
    num_tossup = binomial(num, toss_freq)
    num_bonus = num - num_tossup
    questions = get_random_tossups(num_tossup) + get_random_bonuses(num_bonus)
    shuffle(questions)
    return questions   
