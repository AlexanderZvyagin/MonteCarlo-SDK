import {assert, describe, expect, it, beforeEach, afterEach, test} from 'vitest'
import server from './server.js'
import model from './model'

const failure = error => {
    console.error(`Failure is called! with ${error}`);
    expect(error).toBe(undefined);
}

function BuildModel_Simple () {
    const m = model.Model();
    m.TimeStart = 0;
    m.TimeSteps = 10;
    m.NumPaths = 10000;
    model.AddStatelessUpdater({
        model: m,
        name:"IndependentBrownianMotion"
    });
    model.AddStatefulUpdater ({
        model: m,
        name: "SimpleBrownianMotion",
        start: {name:"MC_r0",value:0.1},
        args: [
            {name:"MC_drift",value:0.2},
            {name:"MC_sigma",value:2}
        ]
    });
    return m;
}

function FxOption_vanilla () {
    const m = model.Model();
    m.TimeStart = 0;
    m.TimeSteps = 1000;
    m.NumPaths = 10000;
    model.AddStatelessUpdater({
        model: m,
        name:"IndependentBrownianMotion"
    });

    const fxProcessNumber =
        model.AddStatefulUpdater ({
            model: m,
            name: "SimpleGeometricalBrownianMotion",
            start: {name:"GBPJPY",value:130},
            args: [
                {name:"MC_drift",value:0.01},
                {name:"MC_sigma",value:0.01}
            ]
        });
    expect(fxProcessNumber).toBe(0);

    const callOptionOnFxProcessNumber =
        model.AddStatefulUpdater ({
            model: m,
            name: "Product_Option",
            start: {name:"PV"}, // value is not important
            args: [
                {name:"myStrike",value:140},
                {name:"myType",value:0} // call:0 put:1
            ],
            refs: [fxProcessNumber]
        });
    expect(callOptionOnFxProcessNumber).toBe(1);

    return m;
}

function FxOption_SingleBarrierUpAndOut () {
    const m = model.Model();
    m.TimeStart = 0;
    m.TimeSteps = 1000;
    m.NumPaths = 10000;
    model.AddStatelessUpdater({
        model: m,
        name:"IndependentBrownianMotion"
    });

    const fxProcessNumber =
        model.AddStatefulUpdater ({
            model: m,
            name: "SimpleGeometricalBrownianMotion",
            start: {name:"GBPJPY",value:140},
            args: [
                {name:"MC_drift",value:0.01},
                {name:"MC_sigma",value:0.01}
            ]
        });
    expect(fxProcessNumber).toBe(0);

    const callOptionOnFxProcessNumber =
        model.AddStatefulUpdater ({
            model: m,
            name: "Product_Option",
            start: {name:"PV"}, // value is not important
            args: [
                {name:"myStrike",value:140},
                {name:"myType",value:0} // call:0 put:1
            ],
            refs: [fxProcessNumber]
        });
    expect(callOptionOnFxProcessNumber).toBe(1);

    const triggerLevel = 150;

    const barrierUpAndOutNumber =
        model.AddStatefulUpdater ({
            model: m,
            name: "Barrier",
            start: {name:"barrier1",value:1}, // start with an active barrier
            args: [
                {name:"triggerLevel",value:triggerLevel},
                {name:"valueOnCrossing",value:0},
                {name:"direction",value:1},
                {name:"action",value:0}, // set
                // {name:"numberOfWindows",value:0} // no special windows, check barrier condition every step
            ],
            refs: [fxProcessNumber]
        });
    expect(barrierUpAndOutNumber).toBe(2);

    const barrierCrossingCounterNumber =
        model.AddStatefulUpdater ({
            model: m,
            name: "Barrier",
            start: {name:"barrier1",value:0}, // start with 0 counter
            args: [
                {name:"triggerLevel",value:triggerLevel},
                {name:"valueOnCrossing",value:1}, // increment by 1
                {name:"direction",value:1},
                {name:"action",value:1}, // action:increment
            ],
            refs: [fxProcessNumber]
        });
    expect(barrierCrossingCounterNumber).toBe(3);

    const barrieroptionNumber =
        model.AddStatefulUpdater ({
            model: m,
            name: "Multiplication",
            start: {name:"barrierOption"},
            refs: [callOptionOnFxProcessNumber,barrierUpAndOutNumber]
        });
    expect(barrieroptionNumber).toBe(4);

    if(0)
        model.AddStatefulUpdater ({
            model: m,
            name: "Error"
        });
    
    return m;
}

async function runModel (modelStructure) {
    return fetch(
        `${server}/model`,
        {
            method: 'post',
            body: JSON.stringify(modelStructure)
        }
    ).then(result => result.json())
}

describe("models", () => {

    test('Main endpoints are accessible', async function () {
        for(let endpoint of ['/','/version','/metrics','/functions']){
            await fetch(`${server}${endpoint}`,{
                // method: 'post',
                // body:JSON.stringify(null),
                // headers: { 'Content-Type': 'application/json'}
            })
            .then(result => {
                expect(result.status).toBe(200);
                expect(result.error).toBe(undefined);
            })
            .catch(failure);
        }
    })

    test('Single process model', async function () {
        const m = BuildModel_Simple();
        await runModel({...m,evaluations:[model.EvaluationPoint(0,1)]})
            .then(result => {
                expect(result).toStrictEqual({
                    mean: [ 0.31632035970687866 ],
                    names: [ 'SimpleBrownianMotion' ],
                    npaths: [ m.NumPaths ],
                    skewness: [ -0.015936529263854027 ],
                    stddev: [ 2.0176687240600586 ],
                    time_points: [ 1 ],
                    time_steps: [ m.TimeSteps ]
                });
            })
            .catch(failure);
    })

    test('Vanilla FxOption', async function () {
        const m = FxOption_vanilla();
        await runModel({
            ...m,
            evaluations: [model.EvaluationPoint(0,1),model.EvaluationPoint(0,2),model.EvaluationPoint(0,10)]
        })
            .then(result => {
                model.PrintEvaulationResult(result);
                // expect(result).toStrictEqual({
                //     mean: [
                //         131.2976837158203,                  0,
                //                         1,                  0,
                //                         0, 132.60549926757812,
                //                         0,                  1,
                //                         0,                  0,
                //        143.67669677734375,  4.193181991577148,
                //       0.16329999268054962,  3.318000078201294,
                //                         0
                //     ],
                //     names: [
                //       'SimpleGeometricalBrownianMotion',
                //       'Product_Option',
                //       'Barrier',
                //       'Barrier',
                //       'Multiplication'
                //     ],
                //     npaths: [
                //       10000, 10000, 10000,
                //       10000, 10000, 10000,
                //       10000, 10000, 10000,
                //       10000, 10000, 10000,
                //       10000, 10000, 10000
                //     ],
                //     skewness: [
                //       0.12002643197774887, null,
                //       null,                null,
                //       null,                0.002960249548777938,
                //       null,                null,
                //       null,                null,
                //       0.08844727277755737, 0.7804861664772034,
                //       1.8217766284942627,  1.7272361516952515,
                //       null
                //     ],
                //     stddev: [
                //        1.3058944940567017,                  0,
                //                         0,                  0,
                //                         0, 1.8599189519882202,
                //                         0,                  0,
                //                         0,                  0,
                //          4.52650260925293,  3.781205177307129,
                //       0.36963915824890137, 3.3134686946868896,
                //                         0
                //     ],
                //     time_points: [ 1, 2, 10 ],
                //     time_steps: [ 100, 200, 1000 ]
                // });
            })
            .catch(failure);
    })

    test('Single barrier UpAndOut FxOption', async function () {
        const m = FxOption_SingleBarrierUpAndOut();
        await runModel({
            ...m,
            evaluations: [model.EvaluationPoint(0,1),model.EvaluationPoint(0,2),model.EvaluationPoint(0,10)]
        })
            .then(result => {
                model.PrintEvaulationResult(result);
                // expect(result).toStrictEqual({
                //     mean: [
                //         131.30398559570312,
                //         0,
                //         132.6192626953125,
                //         0,
                //         143.6581268310547,
                //         4.190196990966797
                //     ],
                //     names: [ 'GeometricalBrownianMotion', 'Product_Option' ],
                //     npaths: [ 10000, 10000, 10000, 10000, 10000, 10000 ],
                //     skewness: [
                //         0.16844412684440613,
                //         null,
                //         0.06291159987449646,
                //         null,
                //         0.11779488623142242,
                //         0.79306560754776
                //     ],
                //     stddev: [
                //         1.311639428138733,
                //         0,
                //         1.8854682445526123,
                //         0,
                //         4.58415412902832,
                //         3.8257291316986084
                //     ],
                //     time_points: [ 1, 2, 10 ],
                //     time_steps: [ 100, 200, 1000 ]
                // });
            })
            .catch(failure);
    })

})
