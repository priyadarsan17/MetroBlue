# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 15:15:33 2021

@author: Priyadarshan.Sathya
"""

from py5paisa import FivePaisaClient

client = FivePaisaClient(email="priyadarsan17@yahoo.com", passwd="67BJsvs84612", dob="19960604")

client.login()

req_list_=[{"Exch":"N","ExchType":"D","Symbol":"NIFTY 26 AUG 2021 CE 16000.00","Expiry":"20210826","StrikePrice":"16000","OptionType":"CE"},
            {"Exch":"N","ExchType":"D","Symbol":"NIFTY 26 AUG 2021 PE 16000.00","Expiry":"20210826","StrikePrice":"16000","OptionType":"PE"}]
            
client.fetch_market_feed(req_list_)

