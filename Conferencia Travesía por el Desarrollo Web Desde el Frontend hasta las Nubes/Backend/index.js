const express = require('express');
const morgan = require('morgan');
const cors = require('cors');
const app = express();
const http = require('http');

app.use(morgan('dev'));
app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.json({ limit:'50mb'}));
app.use(express.urlencoded({ limit:'50mb' }));
app.use(cors());

const server = http.createServer(app);

app.post('/sumar', (req, res) => {
    try{
        console.log("Api llamada, numeros enviados por el cliente: ", req.body);
        const {num1, num2} = req.body;
        if(num1 === undefined || num2 === undefined){
            throw new Error('Error: Parametros no definidos');
        }
        const resultado = parseInt(num1) + parseInt(num2);
        res.status(200).json({resultado:resultado});
    }catch(error){
        res.status(500).json({error: error.message});        
    }

});

server.listen(3000, () => {
    console.log('Server on port 3000');
})



module.exports = {server};