
// This file was automatically generated!
// - by <software> <version>
// - from <DTO-s spec>

import * as fs from 'fs'

import * as dto from './dto'
import {
    Error,
    UpdaterDoc,
    UpdaterDto,
    Updater,
    IndependentGaussian,
    CorrelatedGaussian,
    BrownianMotion,
    BrownianMotionRef,
    GeometricalBrownianMotion,
    GeometricalBrownianMotionRef,
    ZeroCouponBond,
    Option,
    Barrier,
    Polynom,
    Multiplication,
    Division,
    HistogramAxis,
    Histogram,
    EvaluationPoint,
    Model,
    Result,
    EvaluationResults,
    Sum,
    SumOfFutureValues,
} from './dto'

function random_int(min:number = -1000, max:number = 1000) : number {
    return Math.floor (min + Math.random()*(max-min+1));
}

function yes_no () : boolean {
    return random_int(0,1)==1;
}

function random_optional_int() : number|undefined {
    return yes_no() ? random_int() : undefined;
}

function random_float(min:number = -1e6, max:number = 1e6) : number {
    return random_int();
}

function random_optional_float() : number|undefined {
    return yes_no() ? random_float() : undefined;
}

function random_string(min:number = 0, max:number = 3) : string {
    let out: string = '';
    const input: string = 'abcdefghijklmnopqrstuvwxyz0123456789';
    for (let i = 0; i < 32; i++)
        out += input.charAt(random_int(0,input.length));
    return out;
}

function random_optional_string() : string|undefined {
    return yes_no() ? random_string() : undefined;
}

function random_list_int (min:number = 0, max:number = 3) : number[] {
    const size = random_int(min,max);
    let list:number[] = [];
    for(let i=0; i<size; i++)
        list.push(random_int());
    return list;
}

function random_optional_list_int() : number[]|undefined {
    return yes_no() ? random_list_int() : undefined;
}

function random_list_float (min:number = 0, max:number = 3) : number[] {
    const size = random_int(min,max);
    let list:number[] = [];
    for(let i=0; i<size; i++)
        list.push(random_float());
    return list;
}

function random_optional_list_float() : number[]|undefined {
    return yes_no() ? random_list_float() : undefined;
}

function random_list_string (min:number = 0, max:number = 3) : string[] {
    const size = random_int(min,max);
    let list:string[] = [];
    for(let i=0; i<size; i++)
        list.push(random_string());
    return list;
}

function random_optional_list_string() : string[]|undefined {
    return yes_no() ? random_list_string() : undefined;
}


function random_Error () : Error {
    return new Error (
        random_optional_string(),
        random_optional_string(),
        random_optional_int(),
        random_optional_list_Error()

    );
}


function random_optional_Error () : Error|undefined {
    if(yes_no())
        return undefined;
    return random_Error ();
}


function random_list_Error (min:number = 0, max:number = 3) : Error[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Error[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Error());
    return list;
}


function random_optional_list_Error () : Error[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_Error ();
}


function random_UpdaterDoc () : UpdaterDoc {
    return new UpdaterDoc (
        random_string(),
        random_string(),
        random_string(),
        random_string(),
        random_int(),
        random_int()

    );
}


function random_optional_UpdaterDoc () : UpdaterDoc|undefined {
    if(yes_no())
        return undefined;
    return random_UpdaterDoc ();
}


function random_list_UpdaterDoc (min:number = 0, max:number = 3) : UpdaterDoc[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:UpdaterDoc[] = [];
    for(let i=0; i<size; i++)
        list.push(random_UpdaterDoc());
    return list;
}


function random_optional_list_UpdaterDoc () : UpdaterDoc[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_UpdaterDoc ();
}


function random_UpdaterDto () : UpdaterDto {
    return new UpdaterDto (
        random_string(),
        random_optional_list_int(),
        random_optional_list_float(),
        random_optional_list_float()

    );
}


function random_optional_UpdaterDto () : UpdaterDto|undefined {
    if(yes_no())
        return undefined;
    return random_UpdaterDto ();
}


function random_list_UpdaterDto (min:number = 0, max:number = 3) : UpdaterDto[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:UpdaterDto[] = [];
    for(let i=0; i<size; i++)
        list.push(random_UpdaterDto());
    return list;
}


function random_optional_list_UpdaterDto () : UpdaterDto[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_UpdaterDto ();
}


function random_Updater () : Updater {
    return new Updater (
        random_string(),
        random_list_int(),
        random_list_float(),
        random_list_float(),
        random_int(),
        random_string()

    );
}


function random_optional_Updater () : Updater|undefined {
    if(yes_no())
        return undefined;
    return random_Updater ();
}


function random_list_Updater (min:number = 0, max:number = 3) : Updater[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Updater[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Updater());
    return list;
}


function random_optional_list_Updater () : Updater[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_Updater ();
}


function random_IndependentGaussian () : IndependentGaussian {
    return new IndependentGaussian (
        random_list_int(),
        random_string()

    );
}


function random_optional_IndependentGaussian () : IndependentGaussian|undefined {
    if(yes_no())
        return undefined;
    return random_IndependentGaussian ();
}


function random_list_IndependentGaussian (min:number = 0, max:number = 3) : IndependentGaussian[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:IndependentGaussian[] = [];
    for(let i=0; i<size; i++)
        list.push(random_IndependentGaussian());
    return list;
}


function random_optional_list_IndependentGaussian () : IndependentGaussian[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_IndependentGaussian ();
}


function random_CorrelatedGaussian () : CorrelatedGaussian {
    return new CorrelatedGaussian (
        random_float(),
        random_int(),
        random_int(),
        random_string()

    );
}


function random_optional_CorrelatedGaussian () : CorrelatedGaussian|undefined {
    if(yes_no())
        return undefined;
    return random_CorrelatedGaussian ();
}


function random_list_CorrelatedGaussian (min:number = 0, max:number = 3) : CorrelatedGaussian[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:CorrelatedGaussian[] = [];
    for(let i=0; i<size; i++)
        list.push(random_CorrelatedGaussian());
    return list;
}


function random_optional_list_CorrelatedGaussian () : CorrelatedGaussian[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_CorrelatedGaussian ();
}


function random_BrownianMotion () : BrownianMotion {
    return new BrownianMotion (
        random_float(),
        random_float(),
        random_float(),
        random_string()

    );
}


function random_optional_BrownianMotion () : BrownianMotion|undefined {
    if(yes_no())
        return undefined;
    return random_BrownianMotion ();
}


function random_list_BrownianMotion (min:number = 0, max:number = 3) : BrownianMotion[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:BrownianMotion[] = [];
    for(let i=0; i<size; i++)
        list.push(random_BrownianMotion());
    return list;
}


function random_optional_list_BrownianMotion () : BrownianMotion[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_BrownianMotion ();
}


function random_BrownianMotionRef () : BrownianMotionRef {
    return new BrownianMotionRef (
        random_float(),
        random_int(),
        random_int(),
        random_string()

    );
}


function random_optional_BrownianMotionRef () : BrownianMotionRef|undefined {
    if(yes_no())
        return undefined;
    return random_BrownianMotionRef ();
}


function random_list_BrownianMotionRef (min:number = 0, max:number = 3) : BrownianMotionRef[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:BrownianMotionRef[] = [];
    for(let i=0; i<size; i++)
        list.push(random_BrownianMotionRef());
    return list;
}


function random_optional_list_BrownianMotionRef () : BrownianMotionRef[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_BrownianMotionRef ();
}


function random_GeometricalBrownianMotion () : GeometricalBrownianMotion {
    return new GeometricalBrownianMotion (
        random_float(),
        random_float(),
        random_float(),
        random_string()

    );
}


function random_optional_GeometricalBrownianMotion () : GeometricalBrownianMotion|undefined {
    if(yes_no())
        return undefined;
    return random_GeometricalBrownianMotion ();
}


function random_list_GeometricalBrownianMotion (min:number = 0, max:number = 3) : GeometricalBrownianMotion[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:GeometricalBrownianMotion[] = [];
    for(let i=0; i<size; i++)
        list.push(random_GeometricalBrownianMotion());
    return list;
}


function random_optional_list_GeometricalBrownianMotion () : GeometricalBrownianMotion[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_GeometricalBrownianMotion ();
}


function random_GeometricalBrownianMotionRef () : GeometricalBrownianMotionRef {
    return new GeometricalBrownianMotionRef (
        random_float(),
        random_int(),
        random_int(),
        random_string()

    );
}


function random_optional_GeometricalBrownianMotionRef () : GeometricalBrownianMotionRef|undefined {
    if(yes_no())
        return undefined;
    return random_GeometricalBrownianMotionRef ();
}


function random_list_GeometricalBrownianMotionRef (min:number = 0, max:number = 3) : GeometricalBrownianMotionRef[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:GeometricalBrownianMotionRef[] = [];
    for(let i=0; i<size; i++)
        list.push(random_GeometricalBrownianMotionRef());
    return list;
}


function random_optional_list_GeometricalBrownianMotionRef () : GeometricalBrownianMotionRef[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_GeometricalBrownianMotionRef ();
}


function random_ZeroCouponBond () : ZeroCouponBond {
    return new ZeroCouponBond (
        random_int(),
        random_float(),
        random_string()

    );
}


function random_optional_ZeroCouponBond () : ZeroCouponBond|undefined {
    if(yes_no())
        return undefined;
    return random_ZeroCouponBond ();
}


function random_list_ZeroCouponBond (min:number = 0, max:number = 3) : ZeroCouponBond[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:ZeroCouponBond[] = [];
    for(let i=0; i<size; i++)
        list.push(random_ZeroCouponBond());
    return list;
}


function random_optional_list_ZeroCouponBond () : ZeroCouponBond[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_ZeroCouponBond ();
}


function random_Option () : Option {
    return new Option (
        random_int(),
        random_float(),
        random_int(),
        random_string()

    );
}


function random_optional_Option () : Option|undefined {
    if(yes_no())
        return undefined;
    return random_Option ();
}


function random_list_Option (min:number = 0, max:number = 3) : Option[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Option[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Option());
    return list;
}


function random_optional_list_Option () : Option[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_Option ();
}


function random_Barrier () : Barrier {
    return new Barrier (
        random_int(),
        random_float(),
        random_float(),
        random_int(),
        random_int(),
        random_float(),
        random_string()

    );
}


function random_optional_Barrier () : Barrier|undefined {
    if(yes_no())
        return undefined;
    return random_Barrier ();
}


function random_list_Barrier (min:number = 0, max:number = 3) : Barrier[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Barrier[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Barrier());
    return list;
}


function random_optional_list_Barrier () : Barrier[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_Barrier ();
}


function random_Polynom () : Polynom {
    return new Polynom (
        random_int(),
        random_list_float(),
        random_string()

    );
}


function random_optional_Polynom () : Polynom|undefined {
    if(yes_no())
        return undefined;
    return random_Polynom ();
}


function random_list_Polynom (min:number = 0, max:number = 3) : Polynom[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Polynom[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Polynom());
    return list;
}


function random_optional_list_Polynom () : Polynom[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_Polynom ();
}


function random_Multiplication () : Multiplication {
    return new Multiplication (
        random_list_int(),
        random_float(),
        random_string()

    );
}


function random_optional_Multiplication () : Multiplication|undefined {
    if(yes_no())
        return undefined;
    return random_Multiplication ();
}


function random_list_Multiplication (min:number = 0, max:number = 3) : Multiplication[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Multiplication[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Multiplication());
    return list;
}


function random_optional_list_Multiplication () : Multiplication[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_Multiplication ();
}


function random_Division () : Division {
    return new Division (
        random_int(),
        random_int(),
        random_float(),
        random_string()

    );
}


function random_optional_Division () : Division|undefined {
    if(yes_no())
        return undefined;
    return random_Division ();
}


function random_list_Division (min:number = 0, max:number = 3) : Division[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Division[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Division());
    return list;
}


function random_optional_list_Division () : Division[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_Division ();
}


function random_HistogramAxis () : HistogramAxis {
    return new HistogramAxis (
        random_int(),
        random_int(),
        random_float(),
        random_float()

    );
}


function random_optional_HistogramAxis () : HistogramAxis|undefined {
    if(yes_no())
        return undefined;
    return random_HistogramAxis ();
}


function random_list_HistogramAxis (min:number = 0, max:number = 3) : HistogramAxis[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:HistogramAxis[] = [];
    for(let i=0; i<size; i++)
        list.push(random_HistogramAxis());
    return list;
}


function random_optional_list_HistogramAxis () : HistogramAxis[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_HistogramAxis ();
}


function random_Histogram () : Histogram {
    return new Histogram (
        random_HistogramAxis(),
        random_optional_HistogramAxis(),
        random_optional_int(),
        random_optional_list_float()

    );
}


function random_optional_Histogram () : Histogram|undefined {
    if(yes_no())
        return undefined;
    return random_Histogram ();
}


function random_list_Histogram (min:number = 0, max:number = 3) : Histogram[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Histogram[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Histogram());
    return list;
}


function random_optional_list_Histogram () : Histogram[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_Histogram ();
}


function random_EvaluationPoint () : EvaluationPoint {
    return new EvaluationPoint (
        random_float(),
        random_optional_list_Histogram()

    );
}


function random_optional_EvaluationPoint () : EvaluationPoint|undefined {
    if(yes_no())
        return undefined;
    return random_EvaluationPoint ();
}


function random_list_EvaluationPoint (min:number = 0, max:number = 3) : EvaluationPoint[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:EvaluationPoint[] = [];
    for(let i=0; i<size; i++)
        list.push(random_EvaluationPoint());
    return list;
}


function random_optional_list_EvaluationPoint () : EvaluationPoint[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_EvaluationPoint ();
}


function random_Model () : Model {
    return new Model (
        random_float(),
        random_int(),
        random_int(),
        random_list_Updater(),
        random_list_EvaluationPoint(),
        random_optional_int(),
        random_optional_float(),
        random_optional_int(),
        random_int()

    );
}


function random_optional_Model () : Model|undefined {
    if(yes_no())
        return undefined;
    return random_Model ();
}


function random_list_Model (min:number = 0, max:number = 3) : Model[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Model[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Model());
    return list;
}


function random_optional_list_Model () : Model[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_Model ();
}


function random_Result () : Result {
    return new Result (
        random_int(),
        random_float(),
        random_float(),
        random_float()

    );
}


function random_optional_Result () : Result|undefined {
    if(yes_no())
        return undefined;
    return random_Result ();
}


function random_list_Result (min:number = 0, max:number = 3) : Result[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Result[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Result());
    return list;
}


function random_optional_list_Result () : Result[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_Result ();
}


function random_EvaluationResults () : EvaluationResults {
    return new EvaluationResults (
        random_list_string(),
        random_list_int(),
        random_list_float(),
        random_list_float(),
        random_list_float(),
        random_list_float(),
        random_list_int(),
        random_list_Histogram(),
        random_optional_Model()

    );
}


function random_optional_EvaluationResults () : EvaluationResults|undefined {
    if(yes_no())
        return undefined;
    return random_EvaluationResults ();
}


function random_list_EvaluationResults (min:number = 0, max:number = 3) : EvaluationResults[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:EvaluationResults[] = [];
    for(let i=0; i<size; i++)
        list.push(random_EvaluationResults());
    return list;
}


function random_optional_list_EvaluationResults () : EvaluationResults[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_EvaluationResults ();
}


function random_Sum () : Sum {
    return new Sum (
        random_list_float(),
        random_list_int(),
        random_string()

    );
}


function random_optional_Sum () : Sum|undefined {
    if(yes_no())
        return undefined;
    return random_Sum ();
}


function random_list_Sum (min:number = 0, max:number = 3) : Sum[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Sum[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Sum());
    return list;
}


function random_optional_list_Sum () : Sum[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_Sum ();
}


function random_SumOfFutureValues () : SumOfFutureValues {
    return new SumOfFutureValues (
        random_int(),
        random_list_float(),
        random_string()

    );
}


function random_optional_SumOfFutureValues () : SumOfFutureValues|undefined {
    if(yes_no())
        return undefined;
    return random_SumOfFutureValues ();
}


function random_list_SumOfFutureValues (min:number = 0, max:number = 3) : SumOfFutureValues[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:SumOfFutureValues[] = [];
    for(let i=0; i<size; i++)
        list.push(random_SumOfFutureValues());
    return list;
}


function random_optional_list_SumOfFutureValues () : SumOfFutureValues[]|undefined {
    if(yes_no())
        return undefined;
    return random_list_SumOfFutureValues ();
}


function create (struct_name:string, file_name:string){
    if(false){

    } else if (struct_name === 'Error') {
        const obj1: Error = random_Error();
        const j: object = {};
        dto.Error_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: Error = new Error();
        dto.Error_from_json(j,obj2);
        if(!dto.Error_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'UpdaterDoc') {
        const obj1: UpdaterDoc = random_UpdaterDoc();
        const j: object = {};
        dto.UpdaterDoc_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: UpdaterDoc = new UpdaterDoc();
        dto.UpdaterDoc_from_json(j,obj2);
        if(!dto.UpdaterDoc_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'UpdaterDto') {
        const obj1: UpdaterDto = random_UpdaterDto();
        const j: object = {};
        dto.UpdaterDto_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: UpdaterDto = new UpdaterDto();
        dto.UpdaterDto_from_json(j,obj2);
        if(!dto.UpdaterDto_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Updater') {
        const obj1: Updater = random_Updater();
        const j: object = {};
        dto.Updater_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: Updater = new Updater();
        dto.Updater_from_json(j,obj2);
        if(!dto.Updater_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'IndependentGaussian') {
        const obj1: IndependentGaussian = random_IndependentGaussian();
        const j: object = {};
        dto.IndependentGaussian_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: IndependentGaussian = new IndependentGaussian();
        dto.IndependentGaussian_from_json(j,obj2);
        if(!dto.IndependentGaussian_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'CorrelatedGaussian') {
        const obj1: CorrelatedGaussian = random_CorrelatedGaussian();
        const j: object = {};
        dto.CorrelatedGaussian_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: CorrelatedGaussian = new CorrelatedGaussian();
        dto.CorrelatedGaussian_from_json(j,obj2);
        if(!dto.CorrelatedGaussian_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'BrownianMotion') {
        const obj1: BrownianMotion = random_BrownianMotion();
        const j: object = {};
        dto.BrownianMotion_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: BrownianMotion = new BrownianMotion();
        dto.BrownianMotion_from_json(j,obj2);
        if(!dto.BrownianMotion_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'BrownianMotionRef') {
        const obj1: BrownianMotionRef = random_BrownianMotionRef();
        const j: object = {};
        dto.BrownianMotionRef_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: BrownianMotionRef = new BrownianMotionRef();
        dto.BrownianMotionRef_from_json(j,obj2);
        if(!dto.BrownianMotionRef_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'GeometricalBrownianMotion') {
        const obj1: GeometricalBrownianMotion = random_GeometricalBrownianMotion();
        const j: object = {};
        dto.GeometricalBrownianMotion_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: GeometricalBrownianMotion = new GeometricalBrownianMotion();
        dto.GeometricalBrownianMotion_from_json(j,obj2);
        if(!dto.GeometricalBrownianMotion_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'GeometricalBrownianMotionRef') {
        const obj1: GeometricalBrownianMotionRef = random_GeometricalBrownianMotionRef();
        const j: object = {};
        dto.GeometricalBrownianMotionRef_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: GeometricalBrownianMotionRef = new GeometricalBrownianMotionRef();
        dto.GeometricalBrownianMotionRef_from_json(j,obj2);
        if(!dto.GeometricalBrownianMotionRef_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'ZeroCouponBond') {
        const obj1: ZeroCouponBond = random_ZeroCouponBond();
        const j: object = {};
        dto.ZeroCouponBond_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: ZeroCouponBond = new ZeroCouponBond();
        dto.ZeroCouponBond_from_json(j,obj2);
        if(!dto.ZeroCouponBond_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Option') {
        const obj1: Option = random_Option();
        const j: object = {};
        dto.Option_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: Option = new Option();
        dto.Option_from_json(j,obj2);
        if(!dto.Option_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Barrier') {
        const obj1: Barrier = random_Barrier();
        const j: object = {};
        dto.Barrier_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: Barrier = new Barrier();
        dto.Barrier_from_json(j,obj2);
        if(!dto.Barrier_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Polynom') {
        const obj1: Polynom = random_Polynom();
        const j: object = {};
        dto.Polynom_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: Polynom = new Polynom();
        dto.Polynom_from_json(j,obj2);
        if(!dto.Polynom_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Multiplication') {
        const obj1: Multiplication = random_Multiplication();
        const j: object = {};
        dto.Multiplication_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: Multiplication = new Multiplication();
        dto.Multiplication_from_json(j,obj2);
        if(!dto.Multiplication_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Division') {
        const obj1: Division = random_Division();
        const j: object = {};
        dto.Division_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: Division = new Division();
        dto.Division_from_json(j,obj2);
        if(!dto.Division_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'HistogramAxis') {
        const obj1: HistogramAxis = random_HistogramAxis();
        const j: object = {};
        dto.HistogramAxis_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: HistogramAxis = new HistogramAxis();
        dto.HistogramAxis_from_json(j,obj2);
        if(!dto.HistogramAxis_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Histogram') {
        const obj1: Histogram = random_Histogram();
        const j: object = {};
        dto.Histogram_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: Histogram = new Histogram();
        dto.Histogram_from_json(j,obj2);
        if(!dto.Histogram_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'EvaluationPoint') {
        const obj1: EvaluationPoint = random_EvaluationPoint();
        const j: object = {};
        dto.EvaluationPoint_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: EvaluationPoint = new EvaluationPoint();
        dto.EvaluationPoint_from_json(j,obj2);
        if(!dto.EvaluationPoint_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Model') {
        const obj1: Model = random_Model();
        const j: object = {};
        dto.Model_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: Model = new Model();
        dto.Model_from_json(j,obj2);
        if(!dto.Model_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Result') {
        const obj1: Result = random_Result();
        const j: object = {};
        dto.Result_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: Result = new Result();
        dto.Result_from_json(j,obj2);
        if(!dto.Result_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'EvaluationResults') {
        const obj1: EvaluationResults = random_EvaluationResults();
        const j: object = {};
        dto.EvaluationResults_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: EvaluationResults = new EvaluationResults();
        dto.EvaluationResults_from_json(j,obj2);
        if(!dto.EvaluationResults_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Sum') {
        const obj1: Sum = random_Sum();
        const j: object = {};
        dto.Sum_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: Sum = new Sum();
        dto.Sum_from_json(j,obj2);
        if(!dto.Sum_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'SumOfFutureValues') {
        const obj1: SumOfFutureValues = random_SumOfFutureValues();
        const j: object = {};
        dto.SumOfFutureValues_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: SumOfFutureValues = new SumOfFutureValues();
        dto.SumOfFutureValues_from_json(j,obj2);
        if(!dto.SumOfFutureValues_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);

    } else
        throw new Error(`Cannot create an object of the structure ${struct_name}.`);
}

function convert (struct_name:string, file1_name:string, file2_name:string){
    if(false){

    } else if (struct_name === 'Error') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Error = dto.Error_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'UpdaterDoc') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: UpdaterDoc = dto.UpdaterDoc_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'UpdaterDto') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: UpdaterDto = dto.UpdaterDto_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Updater') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Updater = dto.Updater_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'IndependentGaussian') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: IndependentGaussian = dto.IndependentGaussian_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'CorrelatedGaussian') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: CorrelatedGaussian = dto.CorrelatedGaussian_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'BrownianMotion') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: BrownianMotion = dto.BrownianMotion_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'BrownianMotionRef') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: BrownianMotionRef = dto.BrownianMotionRef_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'GeometricalBrownianMotion') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: GeometricalBrownianMotion = dto.GeometricalBrownianMotion_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'GeometricalBrownianMotionRef') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: GeometricalBrownianMotionRef = dto.GeometricalBrownianMotionRef_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'ZeroCouponBond') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: ZeroCouponBond = dto.ZeroCouponBond_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Option') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Option = dto.Option_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Barrier') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Barrier = dto.Barrier_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Polynom') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Polynom = dto.Polynom_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Multiplication') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Multiplication = dto.Multiplication_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Division') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Division = dto.Division_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'HistogramAxis') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: HistogramAxis = dto.HistogramAxis_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Histogram') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Histogram = dto.Histogram_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'EvaluationPoint') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: EvaluationPoint = dto.EvaluationPoint_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Model') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Model = dto.Model_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Result') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Result = dto.Result_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'EvaluationResults') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: EvaluationResults = dto.EvaluationResults_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Sum') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Sum = dto.Sum_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'SumOfFutureValues') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: SumOfFutureValues = dto.SumOfFutureValues_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));

    } else
        throw new Error(`Cannot convert an object of the structure ${struct_name}.`);
}

function compare (struct_name:string, file1_name:string, file2_name:string){
    if(false){

    } else if (struct_name === 'Error') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Error = dto.Error_fromJSON_string(jstr1);
        const obj2: Error = dto.Error_fromJSON_string(jstr2);
        if(!dto.Error_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'UpdaterDoc') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: UpdaterDoc = dto.UpdaterDoc_fromJSON_string(jstr1);
        const obj2: UpdaterDoc = dto.UpdaterDoc_fromJSON_string(jstr2);
        if(!dto.UpdaterDoc_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'UpdaterDto') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: UpdaterDto = dto.UpdaterDto_fromJSON_string(jstr1);
        const obj2: UpdaterDto = dto.UpdaterDto_fromJSON_string(jstr2);
        if(!dto.UpdaterDto_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Updater') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Updater = dto.Updater_fromJSON_string(jstr1);
        const obj2: Updater = dto.Updater_fromJSON_string(jstr2);
        if(!dto.Updater_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'IndependentGaussian') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: IndependentGaussian = dto.IndependentGaussian_fromJSON_string(jstr1);
        const obj2: IndependentGaussian = dto.IndependentGaussian_fromJSON_string(jstr2);
        if(!dto.IndependentGaussian_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'CorrelatedGaussian') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: CorrelatedGaussian = dto.CorrelatedGaussian_fromJSON_string(jstr1);
        const obj2: CorrelatedGaussian = dto.CorrelatedGaussian_fromJSON_string(jstr2);
        if(!dto.CorrelatedGaussian_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'BrownianMotion') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: BrownianMotion = dto.BrownianMotion_fromJSON_string(jstr1);
        const obj2: BrownianMotion = dto.BrownianMotion_fromJSON_string(jstr2);
        if(!dto.BrownianMotion_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'BrownianMotionRef') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: BrownianMotionRef = dto.BrownianMotionRef_fromJSON_string(jstr1);
        const obj2: BrownianMotionRef = dto.BrownianMotionRef_fromJSON_string(jstr2);
        if(!dto.BrownianMotionRef_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'GeometricalBrownianMotion') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: GeometricalBrownianMotion = dto.GeometricalBrownianMotion_fromJSON_string(jstr1);
        const obj2: GeometricalBrownianMotion = dto.GeometricalBrownianMotion_fromJSON_string(jstr2);
        if(!dto.GeometricalBrownianMotion_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'GeometricalBrownianMotionRef') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: GeometricalBrownianMotionRef = dto.GeometricalBrownianMotionRef_fromJSON_string(jstr1);
        const obj2: GeometricalBrownianMotionRef = dto.GeometricalBrownianMotionRef_fromJSON_string(jstr2);
        if(!dto.GeometricalBrownianMotionRef_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'ZeroCouponBond') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: ZeroCouponBond = dto.ZeroCouponBond_fromJSON_string(jstr1);
        const obj2: ZeroCouponBond = dto.ZeroCouponBond_fromJSON_string(jstr2);
        if(!dto.ZeroCouponBond_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Option') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Option = dto.Option_fromJSON_string(jstr1);
        const obj2: Option = dto.Option_fromJSON_string(jstr2);
        if(!dto.Option_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Barrier') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Barrier = dto.Barrier_fromJSON_string(jstr1);
        const obj2: Barrier = dto.Barrier_fromJSON_string(jstr2);
        if(!dto.Barrier_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Polynom') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Polynom = dto.Polynom_fromJSON_string(jstr1);
        const obj2: Polynom = dto.Polynom_fromJSON_string(jstr2);
        if(!dto.Polynom_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Multiplication') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Multiplication = dto.Multiplication_fromJSON_string(jstr1);
        const obj2: Multiplication = dto.Multiplication_fromJSON_string(jstr2);
        if(!dto.Multiplication_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Division') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Division = dto.Division_fromJSON_string(jstr1);
        const obj2: Division = dto.Division_fromJSON_string(jstr2);
        if(!dto.Division_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'HistogramAxis') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: HistogramAxis = dto.HistogramAxis_fromJSON_string(jstr1);
        const obj2: HistogramAxis = dto.HistogramAxis_fromJSON_string(jstr2);
        if(!dto.HistogramAxis_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Histogram') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Histogram = dto.Histogram_fromJSON_string(jstr1);
        const obj2: Histogram = dto.Histogram_fromJSON_string(jstr2);
        if(!dto.Histogram_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'EvaluationPoint') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: EvaluationPoint = dto.EvaluationPoint_fromJSON_string(jstr1);
        const obj2: EvaluationPoint = dto.EvaluationPoint_fromJSON_string(jstr2);
        if(!dto.EvaluationPoint_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Model') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Model = dto.Model_fromJSON_string(jstr1);
        const obj2: Model = dto.Model_fromJSON_string(jstr2);
        if(!dto.Model_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Result') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Result = dto.Result_fromJSON_string(jstr1);
        const obj2: Result = dto.Result_fromJSON_string(jstr2);
        if(!dto.Result_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'EvaluationResults') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: EvaluationResults = dto.EvaluationResults_fromJSON_string(jstr1);
        const obj2: EvaluationResults = dto.EvaluationResults_fromJSON_string(jstr2);
        if(!dto.EvaluationResults_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Sum') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Sum = dto.Sum_fromJSON_string(jstr1);
        const obj2: Sum = dto.Sum_fromJSON_string(jstr2);
        if(!dto.Sum_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'SumOfFutureValues') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: SumOfFutureValues = dto.SumOfFutureValues_fromJSON_string(jstr1);
        const obj2: SumOfFutureValues = dto.SumOfFutureValues_fromJSON_string(jstr2);
        if(!dto.SumOfFutureValues_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);

    } else
        throw new Error(`Cannot compare an object of the structure ${struct_name}.`);
}

function main () {
    // expect at least 3 args
    if(process.argv.length<3)
        throw new Error(`Expect at least 3 args, found ${process.argv.length}`);

    var command = process.argv[2];

    if(command=='create'){
        if(process.argv.length<5)
            throw new Error(`Command "${command}" expects at least 5 args, found ${process.argv.length}`);
        create(process.argv[3],process.argv[4]);
    }
    else if(command=='convert'){
        if(process.argv.length<6)
            throw new Error(`Command "${command}" expects at least 6 args, found ${process.argv.length}`);
        convert(process.argv[3],process.argv[4],process.argv[5]);
    }
    else if(command=='compare'){
        if(process.argv.length<6)
            throw new Error(`Command "${command}" expects at least 6 args, found ${process.argv.length}`);
        compare(process.argv[3],process.argv[4],process.argv[5]);
    } else
        throw new Error(`Unknown command "${command}"`);
}

main();

