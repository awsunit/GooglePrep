const express = require('express');
const morgan = require('morgan');
const { createProxyMiddleware } = require('http-proxy-middleware');


const app = express();

const PORT = 4200;
const HOST = 'localhost';
const URL_TO_MONITOR = 'https://www.yahoo.com/';

app.use(morgan('dev'));

app.get('/info', (req, res, next) => {
    console.log(req.headers);
    res.send('proxy magic baby');
});

// app.use('', (req, res, next) => {
//     res.sendStatus(403);
// })

app.use('/sports', createProxyMiddleware({
    target: URL_TO_MONITOR,
    changeOrigin: true,
    pathRewrite: {
        [`^/sports`]: '',
    },
}));

app.listen(PORT, HOST, () => {
    console.log('Starting proxy at: ', {HOST}, {PORT});
});