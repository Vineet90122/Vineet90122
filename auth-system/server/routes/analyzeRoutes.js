const express = require('express');
const router = express.Router();
const { analyzeAudio } = require('../controller/analyzeController');

router.post('/analyze', analyzeAudio);

module.exports = router;
