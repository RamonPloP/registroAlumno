const express = require('express');
const router = express();
const controller = require('../controllers/alumnos');

router.post('/create',controller.create);

module.exports = router;