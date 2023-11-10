const Alumno = require('../models/alumno');

async function create (req, res){
  const { matricula, genre } = req.body;
  const dateObj = new Date();
  const date = `${dateObj.getDate()}-${dateObj.getMonth() + 1}-${dateObj.getFullYear()}`;

  const alumno = new Alumno({
      matricula: matricula,
      genre: genre,
      date: date
  });

  try {
      await alumno.save();
      res.redirect('/');
  } catch (error) {
      res.status(500).send('Error al guardar datos en la base de datos: ' + error.message);
  }
}

/*
function list(req, res){
    Alumno.find().then(objs => res.status(200).json({
        msg: "Lista de Alumnos",
        obj: objs
    })).catch();
}
*/

module.exports = {create};