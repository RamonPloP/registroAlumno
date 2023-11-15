const express = require('express');
const router = express.Router();
const { create } = require('../controllers/alumnos');

router.post('/create', create);

module.exports = router;
