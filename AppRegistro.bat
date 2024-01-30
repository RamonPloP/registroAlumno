@echo off
start /WAIT npm start
start /WAIT docker start mongodb
start "" "http://localhost:3000"
