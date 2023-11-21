const mongoose = require('mongoose');

const schema = mongoose.Schema({
    _matricula: Number,
    _date: String
});

class Alumno{
    constructor(matricula, genre, date){
        this._matricula = matricula;
        this._date = date;
    }

    get matricula(){
        return this._matricula;
    }

    set matricula(v){
        this._matricula = v;
    }

    get date(){
        return this._date;
    }

    set date(v){
        this._date = v;
    }
}

schema.loadClass(Alumno);

module.exports = mongoose.model('Alumno',schema);