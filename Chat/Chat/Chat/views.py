#-*- coding: utf-8 -*-
"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, Flask, jsonify
from flask import request as flask_request
import requests

from Chat import app

@app.route('/')
def home():
    """Renders chat page.
    Note that the original chat style is from https://www.bypeople.com/minimal-css-chat-ui/#
    """
    bot = {
                'name'     : 'Chatbot',
                'nickname' : 'Puppy',
                'photo'    : 'https://apis.xogrp.com/media-api/images/280a5361-2cfb-4157-86ed-d2871807945a~rs_768.h?quality=75',
            }


    return render_template(
        'chat.html',
        bot=bot
    )

