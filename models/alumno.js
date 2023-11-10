const mongoose = require('mongoose');

const schema = mongoose.Schema({
    _matricula: String,
    _genre: String,
    _date: String
});

class Alumno{
    constructor(matricula, genre, date){
        this._matricula = matricula;
        this._genre = genre;
        this._date = date;
    }

    get matricula(){
        return this._matricula;
    }

    set matricula(v){
        this._matricula = v;
    }

    get genre(){
        return this._genre;
    }

    set genre(v){
        this._genre = v;
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