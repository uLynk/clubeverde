const express = require('express');
const swaggerUi = require('swagger-ui-express');
const swaggerJsdoc = require('swagger-jsdoc');

const app = express();

const swaggerOptions = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'API de Teste',
      version: '1.0.0',
      description: 'Documentação de uma API',
    },
  },
  apis: ['./app.js'],
};

const swaggerDocs = swaggerJsdoc(swaggerOptions);

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocs));

app.get('/teste', (req, res) => {
  res.send('Servidor funcionando!');
});

app.listen(3000, () => {
  console.log('Servidor rodando em http://localhost:3000');
  console.log('Documentação em http://localhost:3000/api-docs');
});
