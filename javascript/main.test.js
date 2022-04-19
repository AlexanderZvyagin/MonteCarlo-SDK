const supertest = require('supertest');
const expect = require('expect');

const serverAddress = process.env.MCSERVER || 'http://192.168.1.82:8080';
const server = supertest.agent(serverAddress);

function Parameter (name,value=NaN,step=NaN,min=NaN,max=NaN) {
    return {name,value,step,min,max};
}

function EvaluationPoint (state=-1,time=NaN,value=NaN,error=NaN) {
    return {state,time,value,error};
}

function Model () {
    return {
        TimeStart:0,
        TimeSteps:1,
        NumPaths:1,
        updaters:[],
        evaluations:[]
    };
}

function AddStatelessUpdater(model,name,args=[],refs=[]){
    model.updaters.push({name,args,refs});
}

function AddStatefulUpdater(model,name,start,args=[],refs=[]){
    model.updaters.push({name,start,args,refs});
    // return model.updaters.length-1; // this is buggy!
}

function BuildModel_Simple () {
    const model = Model();
    model.TimeStart = 0;
    model.TimeSteps = 10;
    model.NumPaths = 10000;
    AddStatelessUpdater(model,"IndependentBrownianMotion");
    AddStatefulUpdater (
        model,
        "SimpleBrownianMotion",
        {name:"MC_r0",value:0.1},
        [
            {name:"MC_drift",value:0.2},
            {name:"MC_sigma",value:2}
        ]
    );

    AddStatefulUpdater (
        model,
        "DiscountFactor",
        {value:1}, // Discount factor at initial time is equal to 1:  P(t0,t0)=1
        [],
        [0] // discount factor calculation refers to the previously defined equation
    );

    model.evaluations.push({state:0,time:3});

    return model;
}

const ResponseOK = 200;

function check_functions_response(res){
    expect(res.status).toBe(ResponseOK);
    expect(res.body).not.toBeNull();
    expect(res.body.length).toBeGreaterThan(0);
}

function check_model_reply(res){
    expect(res.status).toBe(ResponseOK);
    expect(res.body).not.toBeNull();
    console.log(res.body);
}

describe("API endpoints",function(){
    it("should access /version via GET",function(done){
        server
        .get("/version")
        .expect("Content-type",/json/)
        .expect(ResponseOK) // THis is HTTP response
        .end(function(err,res){
            expect(res.status).toBe(ResponseOK);
            done();
        });
    });

    it("should access /version via POST",function(done){
        server
        .post("/version")
        .expect("Content-type",/json/)
        .expect(ResponseOK) // THis is HTTP response
        .end(function(err,res){
            expect(res.status).toBe(ResponseOK);
            done();
        });
    });

    it("should access /functions via GET",function(done){
        server
        .get("/functions")
        .expect("Content-type",/json/)
        .expect(ResponseOK) // THis is HTTP response
        .end(function(err,res){
            check_functions_response(res);
            done();
        });
    });
    it("should access /functions via POST",function(done){
        server
        .post("/functions")
        .expect("Content-type",/json/)
        .expect(ResponseOK) // THis is HTTP response
        .end(function(err,res){
            check_functions_response(res);
            done();
        });
    });
});

describe("/model endpoint",function(){

    (server.ok ? it : it.skip)
    ("should send a model request",function(done){
        const model = BuildModel_Simple();

        server
        .post("/model")
        .send(model)
        .expect("Content-type",/json/)
        .expect(ResponseOK) // THis is HTTP response
        .end(function(err,res){
            check_model_reply(res);
            done();
        });
    });
});

describe("environment variables",function(){
    it("read USER",function(done){
        expect(process.env.USER).not.toBeNull();
        done();
    });
});
