const Alumno = require('../models/alumno');

async function create(req, res) {
  const { matricula } = req.body;

  const date = new Date();

  dateM = `${date.getMonth()+1}-${date.getFullYear()}`

  const alumno = new Alumno({
    matricula: matricula,
    date: dateM
  });

  try {
    await alumno.save();
    res.redirect('/');
  } catch (error) {
    res.status(500).send('Error al guardar datos en la base de datos: ' + error.message);
  }
}

module.exports = { create };