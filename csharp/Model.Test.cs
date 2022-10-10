using System.Collections.Generic;   // List
using System;                       // Console
using NUnit.Framework;

[TestFixture]
public class ModelTests: TestsBase
{
    Model SimpleBM () {
        var model = new Model();
        model.TimeStart = 0;
        model.TimeSteps = 100;
        model.NumPaths = 10000;
        model.updaters.Add(new Updater(
            "IndependentGaussian"
        ));
        model.updaters.Add(new Updater(
            "SimpleBrownianMotion",
            _start:new Parameter("",1),
            _args:new List<Parameter>{new Parameter("",1),new Parameter("",0.1)}
        ));
        model.evaluations.Add(new EvaluationPoint(0,1.1));
        return model;
    }

    Model TwoSimpleBMs () {
        var model = new Model();
        model.TimeStart = 0;
        model.TimeSteps = 100;
        model.NumPaths = 10000;
        model.updaters.Add(new Updater(
            "IndependentGaussian"
        ));
        model.updaters.Add(new Updater(
            "SimpleBrownianMotion",
            _start:new Parameter("",0),
            _args:new List<Parameter>{new Parameter("",1),new Parameter("",0.1)}
        ));
        model.updaters.Add(new Updater(
            "SimpleBrownianMotion",
            _start:new Parameter("",0),
            _args:new List<Parameter>{new Parameter("",-2),new Parameter("",0.2)}
        ));
        model.evaluations.Add(new EvaluationPoint(0,1.1));
        model.evaluations.Add(new EvaluationPoint(0,2.2));
        model.evaluations.Add(new EvaluationPoint(0,3.3));
        return model;
    }

    Model BadModelWithoutEvaluationPoints () {
        var model = new Model();
        model.TimeStart = 0;
        model.TimeSteps = 100;
        model.NumPaths = 10000;
        model.updaters.Add(new Updater(
            "IndependentGaussian"
        ));
        model.updaters.Add(new Updater(
            "SimpleBrownianMotion",
            _start:new Parameter("",1),
            _args:new List<Parameter>{new Parameter("",1),new Parameter("",0.1)}
        ));
        return model;
    }

    Model BadModelWithWrongArguments () {
        var model = new Model();
        model.TimeStart = 0;
        model.TimeSteps = 100;
        model.NumPaths = 10000;
        model.updaters.Add(new Updater(
            "IndependentGaussian"
        ));
        model.updaters.Add(new Updater(
            "SimpleBrownianMotion",
            _start:new Parameter("",1),
            _args:new List<Parameter>{new Parameter("",1)}
        ));
        model.evaluations.Add(new EvaluationPoint(0,1.1));
        return model;
    }

    // Model GbmDigitalDoubleBarrierOption (
    //     double spot = 100,
    //     double drift = 0.2,
    //     double diffusion = 0.4,
    //     double barrier_lower = 120,
    //     double barrier_upper = 180,
    //     int timeSteps=1000,
    //     int numPaths=100000
    // ) {
    //     var model = new Model();

    //     model.TimeStart = 0;
    //     model.TimeSteps = timeSteps;
    //     model.NumPaths = numPaths;

    //     // We don't number functions which have no state
    //     model.equations.Add(new Model.Function(
    //         "IndependentGaussian"
    //     ));

    //     // Equation 0 (the first equation with a state)
    //     int gbm_eq = 0;
    //     model.equations.Add(new Model.Function(
    //         "GeometricalBrownianMotion",
    //         _start:spot,
    //         _args:new List<double>{
    //             drift,
    //             diffusion
    //         }
    //     ));
        
    //     // Up-And-In
    //     int barrier_lower_eq=1;
    //     model.equations.Add(new Model.Function(
    //         "Barrier",
    //         _start: 0,          // start value: inactive
    //         _args: new List<double>{
    //             barrier_lower,  // level
    //             1,              // value when we cross the barrier: set to active (0->1)
    //             1,              // direction:up
    //             0,              // action:set
    //             0               // number of windows
    //         },
    //         _refs: new List<int>{
    //             gbm_eq
    //         }
    //     ));

    //     // Up-And-Out
    //     int barrier_upper_eq=2;
    //     model.equations.Add(new Model.Function(
    //         "Barrier",
    //         _start: 1,          // start value: active
    //         _args: new List<double>{
    //             barrier_upper,  // level
    //             0,              // value when we cross the barrier: set inactive (1->0)
    //             1,              // direction:up
    //             0,              // action:set
    //             0               // number of windows
    //         },
    //         _refs: new List<int>{
    //             gbm_eq
    //         }
    //     ));

    //     // DigitalDoubleBarrier: the product of two barriers
    //     int digital_eq=3;
    //     model.equations.Add(new Model.Function(
    //         "Multiplication",
    //         _start: 0,          // start value: not important
    //         _args: new List<double>{
    //         },
    //         _refs: new List<int>{
    //             barrier_lower_eq, barrier_upper_eq
    //         }
    //     ));

    //     model.evaluations.Add(new Model.EvaluationPoint(4));
    //     return model;
    // }


    public Model CreateModel(string name){
        if(name=="SimpleBM")
            return SimpleBM();
        if(name=="TwoSimpleBMs")
            return TwoSimpleBMs();
        if(name=="EuropeanOptionModel")
            return Example1_EuropeanOption_Test.EuropeanOptionModel();
        if(name=="BadModelWithoutEvaluationPoints")
            return BadModelWithoutEvaluationPoints();
        if(name=="BadModelWithWrongArguments")
            return BadModelWithWrongArguments();
        throw new ArgumentException($"Unknown name {name}");
    }

    [TestCase("SimpleBM")]
    [TestCase("TwoSimpleBMs")]
    [TestCase("EuropeanOptionModel")]
    // [TestCase("GbmDigitalDoubleBarrierOption")]
    public void RunModel(string name){
        var result = Helper.Run(CreateModel(name),server);
        result.Print();
        Assert.That(true,Is.EqualTo(result.Good));
    }

    [TestCase("BadModelWithoutEvaluationPoints")]
    // [TestCase("BadModelWithWrongArguments")]
    public void RunModelShowError(string name){
        var result = Helper.Run(CreateModel(name),server);
        result.Print();
        Assert.That(false,Is.EqualTo(result.Good));
    }

    // [Test]
    // public async Task CheckSingleBarrier() {
    //     // create:
    //     //   1. vanilla option
    //     //   2. single barrier KnockIn option
    //     //   3. single barrier KnockOut option
    //     // and verify that:
    //     //   vanilla = KnockIn + KnockOut

    //     // --------------------------------------
    //     // --- Input arguments
    //     // --------------------------------------
    //     int
    //         timeSteps           = 1000,
    //         numPaths            = 10000;
    //     double
    //         underlyingStart     = 100,
    //         underlyingDrift     = 0,
    //         underlyingDiffusion = 0.1,
    //         strike              = 110,
    //         timeStart           = 0,
    //         timeEnd             = 2;
    //     // --------------------------------------

    //     var model = new Model();
    //     model.TimeStart = timeStart;
    //     model.TimeSteps = timeSteps;
    //     model.NumPaths = numPaths;

    //     int? bmEq =
    //         model.Add(new Model.Function("IndependentGaussian"));
    //     Assert.That(bmEq,Is.Null);
    //     int underlyingEq = 
    //         model.Add(new Model.Function(
    //             "GeometricalBrownianMotion",
    //             _start:underlyingStart,
    //             _args:new List<double>{underlyingDrift,underlyingDiffusion}
    //         )).Value;
    //     Assert.That(underlyingEq,Is.EqualTo(0));

    //     int barrierUpAndIn =
    //         model.Add(new Model.Function(
    //             "Barrier",
    //             _start: 0,          // start value: inactive
    //             _args: new List<double>{
    //                 strike,         // level
    //                 1,              // value when we cross the barrier: set to active (0->1)
    //                 1,              // direction:up
    //                 0,              // action:set
    //                 0               // number of windows
    //             },
    //             _refs: new List<int>{
    //                 underlyingEq
    //             }
    //         )).Value;

    //     int barrierUpAndOut =
    //         model.Add(new Model.Function(
    //             "Barrier",
    //             _start: 1,          // start value: active
    //             _args: new List<double>{
    //                 strike,         // level
    //                 0,              // value when we cross the barrier: set to inactive (1->0)
    //                 1,              // direction:up
    //                 0,              // action:set
    //                 0               // number of windows
    //             },
    //             _refs: new List<int>{
    //                 underlyingEq
    //             }
    //         )).Value;

    //     int point0 = model.Add(new Model.EvaluationPoint(timeEnd/2));
    //     int point1 = model.Add(new Model.EvaluationPoint(timeEnd));

    //     var results = await Run(model);
    //     Print(results);
    //     var resultUpAndIn  = Model.GetResultStatistics(results,barrierUpAndIn ,point1);
    //     var resultUpAndOut = Model.GetResultStatistics(results,barrierUpAndOut,point1);
    //     // resultUpAndIn and resultUpAndIn are NOT independent
    //     // (with the same process generation)
    //     // They should sum up to 1 _independently_ from  numPaths
    //     // within the float number calcuation precision around 1, which is ~10^-7
    //     Assert.That(resultUpAndIn.mean+resultUpAndOut.mean,Is.EqualTo(1).Within(1e-7));
    // }

    // [Test]
    // public async Task DoubleNotTouch() {
    //     // Do not hit any of the two barriers

    //     // --------------------------------------
    //     // --- Input arguments
    //     // --------------------------------------
    //     int
    //         timeSteps           = 1000,
    //         numPaths            = 10000;
    //     double
    //         underlyingStart     = 1,
    //         underlyingDrift     = 0,
    //         underlyingDiffusion = 0.1,
    //         lowerBarrier        = 0.9,
    //         upperBarrier        = 1.1,
    //         timeStart           = 0,
    //         timeEnd             = 2;
    //     // --------------------------------------

    //     var model = new Model();
    //     model.TimeStart = timeStart;
    //     model.TimeSteps = timeSteps;
    //     model.NumPaths = numPaths;

    //     int? bmEq =
    //         model.Add(new Model.Function("IndependentGaussian"));
    //     Assert.That(bmEq,Is.Null);
    //     int underlyingEq = 
    //         model.Add(new Model.Function(
    //             "GeometricalBrownianMotion",
    //             _start:underlyingStart,
    //             _args:new List<double>{underlyingDrift,underlyingDiffusion}
    //         )).Value;
    //     Assert.That(underlyingEq,Is.EqualTo(0));

    //     int lowerBarrierEq =
    //         model.Add(new Model.Function(
    //             "Barrier",
    //             _start: 1,          // start value: active
    //             _args: new List<double>{
    //                 lowerBarrier,   // level
    //                 0,              // value when we cross the barrier: set to inactive (1->0)
    //                -1,              // direction:down
    //                 0,              // action:set
    //                 0               // number of windows
    //             },
    //             _refs: new List<int>{
    //                 underlyingEq
    //             }
    //         )).Value;

    //     int upperBarrierEq =
    //         model.Add(new Model.Function(
    //             "Barrier",
    //             _start: 1,          // start value: active
    //             _args: new List<double>{
    //                 upperBarrier,   // level
    //                 0,              // value when we cross the barrier: set to inactive (1->0)
    //                 1,              // direction:up
    //                 0,              // action:set
    //                 0               // number of windows
    //             },
    //             _refs: new List<int>{
    //                 underlyingEq
    //             }
    //         )).Value;

    //     int doubleNotTouchEq =
    //         model.Add(new Model.Function(
    //             "Multiplication",
    //             _start: 0,          // start value: not important
    //             _args: new List<double>{
    //             },
    //             _refs: new List<int>{
    //                 lowerBarrierEq, upperBarrierEq
    //             }
    //         )).Value;

    //     int point0 = model.Add(new Model.EvaluationPoint(timeEnd/2));
    //     int point1 = model.Add(new Model.EvaluationPoint(timeEnd));

    //     var results = await Run(model);
    //     Print(results);
    // }
}
