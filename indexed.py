import array
from asyncio.proactor_events import constants
from hashlib import new; import math; import inspect;
from math import nan
from math import *
from inspect import _void
from multiprocessing import connection
from multiprocessing.dummy import Array
from sqlite3 import dbapi2
from tokenize import String
from stringify import Stuff
from scuffed import encrypt

def down(nums: int, saved: list) -> list:
    if nums != nan:
        while True:
            nums += 1
            if nums == 51:
                break
    for i in range (nums):
        if i != 0:
            print(i)
            saved.append(i)
    return [ i, saved ] # this just show it's always at the end of a thread

def shapify(all_characters: list, x: int) -> _void:
    out_of_range: int = 10
    if len(all_characters[x]) != out_of_range:
        print("\t", all_characters[x])
        created_hash = encrypt.make_hash(all_characters, x)
        if created_hash:
            created_salt = encrypt.make_salt(created_hash)
            if created_salt:
                PATH = "/home/ifstatements/site/scripts/personal"
                print(created_hash,"\n")
                print(created_salt) 
                saved = dbapi2.connect(PATH)
                saved.execute("")
    else:
        return

def run() -> _void:
    increments = down(1, [])[0]
    for x in range (increments):
        characters = ["!", "@", "G", "h", "ten", "fifite", "yes", "nn", "^", "*"]
        x = x / 2
        res = floor(x)
        shapify(characters, res) 
            
run()