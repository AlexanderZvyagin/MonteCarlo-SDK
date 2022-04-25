using System.Collections.Generic;   // List
using System;                       // Console
using NUnit.Framework;

[TestFixture]
public class Example1_EuropeanOption_Test: TestsBase
{
    // https://www.johndcook.com/blog/cpp_erf/
    public double erf (double x)
    {
        // constants
        double a1 =  0.254829592;
        double a2 = -0.284496736;
        double a3 =  1.421413741;
        double a4 = -1.453152027;
        double a5 =  1.061405429;
        double p  =  0.3275911;

        // Save the sign of x
        int sign = 1;
        if (x < 0)
            sign = -1;
        x = Math.Abs(x);

        // A&S formula 7.1.26
        double t = 1.0/(1.0 + p*x);
        double y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t*Math.Exp(-x*x);

        return sign*y;
    }

    public double cndf (double x) {
        return (erf(x/Math.Sqrt(2))+1)/2;
    }

    public (double,double) Black76 (
        double spot,
        double strike,
        double sigma,
        double time,
        double discount
    ){
        double
            sigma_sqrt_time = sigma * Math.Sqrt(time),
            forward         = spot/discount,
            d               = Math.Log(forward/strike) / sigma_sqrt_time,
            dp              = d + sigma_sqrt_time/2,
            dm              = d - sigma_sqrt_time/2,
            cndf_pdp        = cndf(dp),
            cndf_pdm        = cndf(dm),
            cndf_ndp        = 1-cndf_pdp,
            cndf_ndm        = 1-cndf_pdm,
            price_call      = cndf_pdp * spot              - cndf_pdm * strike * discount,
            price_put       = cndf_ndm * strike * discount - cndf_ndp * spot;
        return (price_call, price_put);
    }

    static public Model EuropeanOptionModel (
        double spot = 100,
        double strike = 300,
        double drift = 0.2,
        double diffusion = 0.4,
        double timeStart = 0,
        double timeHorizon = 4,
        int numPaths=10000,
        int timeSteps=1000
    ) {
        var model = new Model();

        model.TimeStart = timeStart;
        model.TimeSteps = timeSteps;
        model.NumPaths = numPaths;

        // We don't number functions which have no state
        model.updaters.Add(new Updater(
            "IndependentBrownianMotion"
        ));

        // Equation 0 (the first equation with a state)
        int gbm_eq = 0;
        model.updaters.Add(new Updater(
            "GeometricalBrownianMotion",
            _start:new Parameter("",spot),
            _args:new List<Parameter>{
                new Parameter("",drift),
                new Parameter("",diffusion)
            }
        ));
        // Equation 1
        model.updaters.Add(new Updater(
            "Product_Option",
            _start: new Parameter("",double.NaN),                      // start value is not important
            _args: new List<Parameter>{
                new Parameter("",strike),                     // strike
                new Parameter("",0),                          // option type, 0:call, 1:put
            },
            _refs: new List<int>{
                gbm_eq
            }
        ));
        // Equation 2
        model.updaters.Add(new Updater(
            "Product_Option",
            _start: new Parameter("",double.NaN),                      // start value is not important
            _args: new List<Parameter>{
                new Parameter("",strike),                     // strike
                new Parameter("",1),                          // option type, 0:call, 1:put
            },
            _refs: new List<int>{
                gbm_eq
            }
        ));
        model.evaluations.Add(new EvaluationPoint(0,timeHorizon));
        return model;
    }


    [TestCase(100,300,0.4,4,0.2,10000,1000)]
    [TestCase(100,300,0.2,0.4,0)]
    [TestCase(100,300,0.2,0.4,0.2)]
    [TestCase(100,200,0.1,1,0)]
    [TestCase(150,200,0.1,10,0.02)]
    [TestCase(100,100,0.1,10,0.02)]
    [TestCase(100,200,1,1,0,100000,10000)]
    [TestCase(150,200,0.2,4,0.2,100000,10000)]
    public void EuropeanOptionCallPutPrices(
        double spot,
        double strike,
        double sigma,
        double time,
        double riskFreeRate,
        int numPaths = 10000,
        int timeSteps = 1000
    ){
        var model = EuropeanOptionModel(
            spot:spot,
            strike:strike,
            timeHorizon:time,
            drift:riskFreeRate,
            diffusion:sigma,
            numPaths:numPaths,
            timeSteps:timeSteps
        );
        var modelResults = Helper.Run(model,server);
        modelResults.Print();
        double
            discount = Math.Exp(-time*riskFreeRate);
        Statistics
            mc_call = modelResults.StatisticsOfStatePoint(1,0),
            mc_put  = modelResults.StatisticsOfStatePoint(2,0);
        var (bs_call,bs_put) = Black76(spot,strike,sigma,time,discount);

        // Console.WriteLine($"BS Call/Put prices:  {Black76(spot,strike,sigma,time,discount)}");
        Console.WriteLine($"Call: {mc_call.mean*discount}  {bs_call}");
        Console.WriteLine($"Put : {mc_put .mean*discount}  {bs_put }");

        double nsigma=3;
        Assert.That(bs_call/discount,Is.EqualTo(mc_call.mean).Within(abseps+nsigma*mc_call.meanError),"call price error");
        Assert.That(bs_put /discount,Is.EqualTo(mc_put .mean).Within(abseps+nsigma*mc_put .meanError),"put price error"); 
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
    //         model.Add(new Model.Function("IndependentBrownianMotion"));
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
    //         model.Add(new Model.Function("IndependentBrownianMotion"));
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

    // [TestCase(0)]
    // [TestCase(double.NaN)]
    // public void TestSerializationOfParameter(double value){
    //     var options = Helper.GetJsonSerializerOptions();
    //     var p1 = new Parameter("MyParameter",value,1,2,3);
    //     var p1_js = JsonSerializer.Serialize<Parameter>(p1,options);
    //     Console.WriteLine($"{p1_js}");
    //     var p2 = System.Text.Json.JsonSerializer.Deserialize<Parameter>(p1_js,options);
    // }


}
