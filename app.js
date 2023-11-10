const express = require('express');
const mongoose = require('mongoose');
const app = express();
const port = 3000;
const bodyParser = require('body-parser');
const router = require('./routes/alumnos')


const url = "mongodb://localhost:27017/alumnos";
mongoose.connect(url);

const db = mongoose.connection;

db.on('open',()=>{
    console.log('Conexion Ok');
});

db.on('error', ()=>{
    console.log('No se pudo conectar a la db');
});  

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static('public'));


app.use('/', router);

app.listen(port, () => {
  console.log(`Servidor Express en ejecución en el puerto ${port}`);
});

module.exports = app;
