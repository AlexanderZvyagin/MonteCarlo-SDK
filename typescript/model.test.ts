import fetch from "node-fetch"
import { expect, expectTypeOf, test } from 'vitest'
import {server} from './server.js'
import * as sdk from './mcsdk'

const failure = error => {
    expect(error).toBe(undefined);
}

async function runModel (model:sdk.Model) {
    return fetch(
        `${server()}/model`,
        {
            method: 'post',
            body: JSON.stringify(model)
        }
    ).then(async result => {
        const json = await result.json();
        if(result.status!==200){
            let error_multiline = "";
            for(let e of json.error){
                error_multiline += '\n' + e;
            }
            return Promise.reject(error_multiline);
        }
        return json;
    })
}

test('SimpleModel with 0 time steps', async function () {

    const model = new sdk.Model(0,0,10000);
    model.Add(new sdk.IndependentGaussian());
    model.Add(new sdk.BrownianMotion(0.1,0.2,2));
    model.evaluations.push(new sdk.EvaluationPoint(0,1));

    await runModel(model).catch(error => {
        expect(error).toContain('The number of time steps must be positive');
    });
})

test('SimpleModel with 0 paths', async function () {

    const model = new sdk.Model(0,10,0);
    model.RandomSeed = 0;
    model.Add(new sdk.IndependentGaussian());
    model.Add(new sdk.BrownianMotion(0.1,0.2,2));
    model.evaluations.push(new sdk.EvaluationPoint(0,1));

    await runModel(model).catch(error => {
        expect(error).toContain('Bad number of paths');
    });
})

test('SimpleModel', async function () {

    const model = new sdk.Model(0,10,10000);
    model.Add(new sdk.IndependentGaussian());
    model.Add(new sdk.BrownianMotion(0.1,0.2,2));
    model.evaluations.push(new sdk.EvaluationPoint(0,1));

    await runModel(model)
        .then(result => {
            console.log(result);
            expect(result.mean[0]).toBeCloseTo(0.3,1);
            expect(result.stddev[0]).toBeCloseTo(2.0,1);
            expect(result.skewness[0]).toBeCloseTo(0,1);
            expect(result.names).toEqual(['BrownianMotion' ]);
            expect(result.npaths).toEqual([model.NumPaths]);
            expect(result.time_points).toEqual([model.evaluations[0].time]);
            expect(result.time_steps).toEqual([model.TimeSteps]);
        })
        .catch(failure);    
})
