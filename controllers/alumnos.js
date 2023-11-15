const Alumno = require('../models/alumno');

async function create(req, res) {
  const { matricula, genre } = req.body;

  const date = new Date();

  const alumno = new Alumno({
    matricula: matricula,
    genre: genre,
    date: date,
  });

  try {
    await alumno.save();
    res.redirect('/');
  } catch (error) {
    res.status(500).send('Error al guardar datos en la base de datos: ' + error.message);
  }
}

module.exports = { create };