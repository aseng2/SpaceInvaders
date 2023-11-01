# Anthony Seng
# CPSC 386-05
# 2023-04-20
# aseng6825@csu.fullerton.edu
# @aseng2
#
# Lab 05-00
#
# setup.py
#

""" Simple setup.py """

from setuptools import setup

setup_info = {
    "name": "videogame",
    "version": "0.1",
    "description": "A package to support writing games with PyGame",
    # "long_description": open("README.md").read(),
    # "author": "Tuffy Titan",
    # "author_email": "tuffy@csu.fullerton.edu",
    # "url": "https://some.url/somehwere/maybe/github",
}

setup(**setup_info)
