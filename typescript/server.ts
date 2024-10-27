export function server (): string {
    if(process.env.SERVER_ADDRESS===undefined)
        throw new Error('Please, set SERVER_ADDRESS environment variable, e.g. SERVER_ADDRESS=http://my.host:port/addr');
    return `${process.env.SERVER_ADDRESS}`;
}
