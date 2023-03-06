export function server (): string {
    if(process.env.SERVER_ADDRESS===undefined || process.env.SERVER_PORT===undefined)
        throw new Error(`Missing environment variable(s): SERVER_ADDRESS="${process.env.SERVER_ADDRESS}" SERVER_PORT="${process.env.SERVER_PORT}"`);
    return `http://${process.env.SERVER_ADDRESS}:${process.env.SERVER_PORT}`;
}
