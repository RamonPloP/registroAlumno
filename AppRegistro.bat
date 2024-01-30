@echo off
start /WAIT docker start mongodb
start npm start
start "" "http://localhost:3000"
