const http = require('http');
const express = require('express');

const hostname = '127.0.0.1';
const port = 3000;

var app = express();

app.set(port, process.env.PORT || 3000);

app.use(function(req, res, next) {
	var fileName = req.query.fileName;
	res.send({fileName:fileName});
});

http.createServer(app).listen(app.get(port), function() {
	console.log('Express Start');
});