const
    server = process.env.SERVER_ADDRESS || 'localhost',
    port   = process.env.SERVER_PORT || 8001;

module.exports = `http://${server}:${port}`;
