@echo off
start npm start
start docker start mongodb
start "" "http://localhost:3000"