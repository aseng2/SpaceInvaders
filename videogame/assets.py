# Anthony Seng
# CPSC 386-05
# 2023-04-20
# aseng6825@csu.fullerton.edu
# @aseng2
#
# Lab 05-00
#
# assets.py
#

"""Assets for making games with PyGame."""

import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

asset_dict = {
    'soundtrack' : 'Main Theme - Super Smash Bros Brawl.mp3',
    'explosion' : 'explosion1.gif',
    'alien' : 'alien2_1_25.png',
    'spaceship' : 'spaceship2_2_100x100.png',
    'soundfx' : 'esm_8bit_explosion_bomb_boom_blast_cannon_retro_old_school_classic_cartoon.mp3'
}

def get(key):
    """Get the data"""
    value = asset_dict.get(key, None)
    assert value
    if value:
        value = os.path.join(data_dir, value)
    return value
