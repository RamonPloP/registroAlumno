fetch('http://148.229.225.109/LogAleph/default.aspx?cmd=show&id=0%2C18&Biblioteca=FI&DeLaForma=true&btn=Ejecutar').then(obj =>{
    console.log(obj.body)
}).catch(err => {
    console.log(err)
});