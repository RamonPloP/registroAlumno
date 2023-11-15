function validateMatricula(req, res, next) {
  const { matricula } = req.body;
  const matriculaRegex = /^\d{6}$/;

  if (!matriculaRegex.test(matricula)) {
    res.status(400).redirect('/');
    }else{
    next();
  }
 
}

module.exports = validateMatricula;
  