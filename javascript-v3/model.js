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

const NumberOfStatefullUpdaters = model => model.updaters.filter(v=>v.start!==undefined).length;
const NumberOfStatelessUpdaters = model => model.updaters.filter(v=>v.start===undefined).length;

function AddStatelessUpdater({model,name,args=[],refs=[]}){
    model.updaters.push({name,args,refs});
}

function AddStatefulUpdater({model,name,start=NaN,args=[],refs=[]}){
    model.updaters.push({name,start,args,refs});
    return NumberOfStatefullUpdaters(model)-1;
}

function PrintEvaulationResult (result) {
    const
        numStates  = result.names.length,
        numEvals   = result.time_points.length,
	evalsTable = [];
    for(let i=0; i<numStates; i++){
        const stateResultLine = {name:result.names[i]};
        for(let j=0; j<numEvals; j++){
	    const
	        col = `time=${result.time_points[j]} step=${result.time_steps[j]}`,
	        index = numStates*j+i,
	        mean  = result.mean[index],
		error = result.stddev[index]/Math.sqrt(result.npaths[index]);
	    stateResultLine[col] = `${mean.toFixed(3)} +/- ${error.toFixed(3)}`;
	}
	evalsTable.push(stateResultLine);
    }

    console.table(evalsTable);
}

module.exports = {
    Model,
    Parameter,
    EvaluationPoint,
    AddStatelessUpdater,
    AddStatefulUpdater,
    NumberOfStatelessUpdaters,
    NumberOfStatelessUpdaters,
    PrintEvaulationResult
}
