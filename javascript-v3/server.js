const
    server = process.env.SERVER_ADDRESS || 'naz.hopto.org',
    port   = process.env.SERVER_PORT || 8001;

module.exports = `http://${server}:${port}`;
