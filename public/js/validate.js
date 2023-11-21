function validarFormulario() {
    const matriculaValida = validarMatricula();

    return matriculaValida;
  }

  function validarMatricula() {
    const matriculaInput = document.getElementById("input");
    const matricula = matriculaInput.value;
    const regexMatricula = /^\d+$/;

    if (!regexMatricula.test(matricula)) {
      document.getElementById("error").innerText = "La matrícula debe ser solo los numeros.";
      return false;
    }

    return true;
  }