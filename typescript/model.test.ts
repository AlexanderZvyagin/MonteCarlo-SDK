import { expect, expectTypeOf, test } from 'vitest'
import {server} from './server.js'
import * as sdk from './mcsdk'

const HttpStatus = {OK:200, BadRequest:400};

const failure = error => {
    expect(error).toBe(undefined);
}

test('SimpleModel with 0 time steps', async function () {

    const model = new sdk.Model(0,0,10000);
    model.Add(new sdk.IndependentGaussian());
    model.Add(new sdk.BrownianMotion(0.1,0.2,2));
    model.evaluations.push(new sdk.EvaluationPoint(0,1));

    await sdk.run(model, server())
        .then(result => {
            const error = new sdk.Error(result.message,result.details,result.code,result.errors);
            expect(error.code).toBe(HttpStatus.BadRequest);
//            expect(error.message).toContain('Error');
            expect(error.details).toContain('The number of time steps must be positive');
        });
})

test('SimpleModel with 0 paths', async function () {

    const model = new sdk.Model(0,10,0);
    model.RandomSeed = 0;
    model.Add(new sdk.IndependentGaussian());
    model.Add(new sdk.BrownianMotion(0.1,0.2,2));
    model.evaluations.push(new sdk.EvaluationPoint(0,1));

    await sdk.run(model,server())
        .then(result => {
            const error = new sdk.Error(result.message,result.details,result.code,result.errors);
            expect(error.code).toBe(HttpStatus.BadRequest);
//            expect(error.message).toContain('Error');
            expect(error.details).toContain('Bad number of paths');
        });
})

test('SimpleModel', async function () {

    const pars = {
        start     : 0.1,
        drift     : 0.2,
        diffusion : 0.3,
        T         : 2 // Time horizon
    };

    const expected = {
        mean     : pars.start+pars.drift*pars.T,
        stddev   : Math.sqrt(pars.T) * pars.diffusion,
        skewness : 0
    };


    const model = new sdk.Model(0,10,20000);
    model.RandomSeed = 0;
    model.Add(new sdk.IndependentGaussian());
    model.Add(new sdk.BrownianMotion(pars.start,pars.drift,pars.diffusion));
    model.evaluations.push(new sdk.EvaluationPoint(0,pars.T));

    await sdk.run(model, server())
        .then(result => {
            console.log(result);
            expect(result.mean[1]).toBeCloseTo(expected.mean,1);
            expect(result.stddev[1]).toBeCloseTo(expected.stddev,1);
            expect(result.skewness[1]).toBeCloseTo(expected.skewness,1);
            expect(result.names).toEqual(['IndependentGaussian','BrownianMotion' ]);
            expect(result.npaths).toEqual([0,model.NumPaths]);
            expect(result.time_points).toEqual([model.evaluations[0].time]);
            expect(result.time_steps).toEqual([model.TimeSteps-1]);
        })
        .catch(failure);
})
