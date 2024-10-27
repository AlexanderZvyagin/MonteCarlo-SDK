import fetch from "node-fetch"
import { expect, expectTypeOf, test } from 'vitest'
import {server} from './server.js'
import * as sdk from './mcsdk'

test('modules are loaded', () => {
    expect(fetch).not.toBeUndefined()
    expect(server()).not.toBeUndefined()
    expect(sdk).not.toBeUndefined()
    expectTypeOf(sdk.Model).not.toBeUndefined()
})

test('server endpoints are accessible', async function () {
    console.log(`The server is ${server()}`);
    for(let endpoint of ['/','/metrics','/functions']){
        await fetch(`${server()}${endpoint}`,{
        })
        .then(result => {
            expect(result.status).toBe(200);
            expect(result.error).toBe(undefined);
        })
    }
})
