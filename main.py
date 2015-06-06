#!/usr/bin/python

#Title: Main.py
#Description: Program that recognizes face attributes from a given portrait in url form
#Author: Paul Ryan Olivar
#Created: June 6, 2015

import unirest

print "Welcome to the SmartLock program";


userURLInput = raw_input("Please enter url from which attributes will be analyzed \n");

print "You inputted " , userURLInput, type(userURLInput);

requestURL = "https://faceplusplus-faceplusplus.p.mashape.com/detection/detect?attribute=glass%2Cpose%2Cgender%2Cage%2Crace%2Csmiling&url=" + userURLInput;

print "The URL to be requested is " , requestURL;


#initiate API request
response = unirest.get(requestURL,
  headers={
    "X-Mashape-Key": "MW1pvu2ke2mshRfxItYbk92BVighp13BQ7pjsn65m55euuE04K",
    "Accept": "application/json"
  }
)

print "The response code is " , response.code;


if response.code == 200:

#Print response body
#print "Response is " ,response.body['face'][0];


#Print facial attributes
	print "The gender is " , response.body['face'][0]['attribute']['gender']['value'] , "with confidence", response.body['face'][0]['attribute']['gender']['confidence'];

	print "The age is " , response.body['face'][0]['attribute']['age']['value'], "with range +-", response.body['face'][0]['attribute']['age']['range'];

	print "The race is " , response.body['face'][0]['attribute']['race']['value'] , "with confidence " , response.body['face'][0]['attribute']['gender']['confidence'];

	print "Smiling: " ,  response.body['face'][0]['attribute']['smiling']['value'];

	print "Pose attributes: "

	print "Yaw angle: " , response.body['face'][0]['attribute']['pose']['yaw_angle']['value'];

	print "Pitch angle: " , response.body['face'][0]['attribute']['pose']['pitch_angle']['value'];

	print " Row angle: " , response.body['face'][0]['attribute']['pose']['roll_angle']['value'];

else:
	print "Picture cannot be processed";