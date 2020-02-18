var server = require('http');

server.createServer( function(req, res) {
    res.writeHead(200, {'Content-Type' : 'text/html'});
    res.write('<p style="color:blue">Hello World!</p>');
    res.end();
}).listen(8080);