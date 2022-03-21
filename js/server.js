// import RegularJSON from '../json/prep.json';


// console.log({RegularJSON});

var http = require('http');
var fs = require('fs');
var path = require('path');

http.createServer((request, response) => {
    console.log(`Request url: ${request.url}`);

    var mimeTypes = {
        '.html': 'text/html',
        '.css': 'text/css',
        '.js': 'text/javascript',
    }
    var relativePaths = {
        '.html': `./html${request.url}`,
        '.css': `./css${request.url}`,
        '.js': `./js${request.url}`,
    }

    // could spend time building up mimi types, assume single page
    var filePath = `.${request.url}`;

    var extension = String(path.extname(filePath)).toLowerCase();
    console.log({extension});


    var contentType = mimeTypes[extension];

    filePath = relativePaths[extension];
    console.log(`new filePath: ${filePath}`);

    fs.readFile(filePath, function(error, content){
        if (error) {
            console.log({error});
            response.writeHead(500);
            response.end('error occurred boss');
        } else {
            console.log('success`');
            response.writeHead(200, {'Content-Type': contentType});
            response.end(content, 'utf-8');
        }
    })
}).listen(8080);
console.log('server running'); 
