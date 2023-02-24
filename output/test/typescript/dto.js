"use strict";
// This is an automatically generated file.
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
exports.__esModule = true;
exports.GeometricalBrownianMotion_equal = exports.BrownianMotionRef_from_json_string = exports.BrownianMotionRef_to_json_string = exports.BrownianMotionRef_from_json = exports.BrownianMotionRef_to_json = exports.BrownianMotionRef_fromJSON_string = exports.BrownianMotionRef_fromJSON = exports.BrownianMotionRef_equal = exports.BrownianMotion_from_json_string = exports.BrownianMotion_to_json_string = exports.BrownianMotion_from_json = exports.BrownianMotion_to_json = exports.BrownianMotion_fromJSON_string = exports.BrownianMotion_fromJSON = exports.BrownianMotion_equal = exports.CorrelatedGaussian_from_json_string = exports.CorrelatedGaussian_to_json_string = exports.CorrelatedGaussian_from_json = exports.CorrelatedGaussian_to_json = exports.CorrelatedGaussian_fromJSON_string = exports.CorrelatedGaussian_fromJSON = exports.CorrelatedGaussian_equal = exports.IndependentGaussian_from_json_string = exports.IndependentGaussian_to_json_string = exports.IndependentGaussian_from_json = exports.IndependentGaussian_to_json = exports.IndependentGaussian_fromJSON_string = exports.IndependentGaussian_fromJSON = exports.IndependentGaussian_equal = exports.Updater_from_json_string = exports.Updater_to_json_string = exports.Updater_from_json = exports.Updater_to_json = exports.Updater_fromJSON_string = exports.Updater_fromJSON = exports.Updater_equal = exports.UpdaterDto_from_json_string = exports.UpdaterDto_to_json_string = exports.UpdaterDto_from_json = exports.UpdaterDto_to_json = exports.UpdaterDto_fromJSON_string = exports.UpdaterDto_fromJSON = exports.UpdaterDto_equal = exports.UpdaterDoc_from_json_string = exports.UpdaterDoc_to_json_string = exports.UpdaterDoc_from_json = exports.UpdaterDoc_to_json = exports.UpdaterDoc_fromJSON_string = exports.UpdaterDoc_fromJSON = exports.UpdaterDoc_equal = void 0;
exports.HistogramAxis_fromJSON = exports.HistogramAxis_equal = exports.Multiplication_from_json_string = exports.Multiplication_to_json_string = exports.Multiplication_from_json = exports.Multiplication_to_json = exports.Multiplication_fromJSON_string = exports.Multiplication_fromJSON = exports.Multiplication_equal = exports.Linear1DInterpolation_from_json_string = exports.Linear1DInterpolation_to_json_string = exports.Linear1DInterpolation_from_json = exports.Linear1DInterpolation_to_json = exports.Linear1DInterpolation_fromJSON_string = exports.Linear1DInterpolation_fromJSON = exports.Linear1DInterpolation_equal = exports.Barrier_from_json_string = exports.Barrier_to_json_string = exports.Barrier_from_json = exports.Barrier_to_json = exports.Barrier_fromJSON_string = exports.Barrier_fromJSON = exports.Barrier_equal = exports.Option_from_json_string = exports.Option_to_json_string = exports.Option_from_json = exports.Option_to_json = exports.Option_fromJSON_string = exports.Option_fromJSON = exports.Option_equal = exports.ZeroCouponBond_from_json_string = exports.ZeroCouponBond_to_json_string = exports.ZeroCouponBond_from_json = exports.ZeroCouponBond_to_json = exports.ZeroCouponBond_fromJSON_string = exports.ZeroCouponBond_fromJSON = exports.ZeroCouponBond_equal = exports.GeometricalBrownianMotionRef_from_json_string = exports.GeometricalBrownianMotionRef_to_json_string = exports.GeometricalBrownianMotionRef_from_json = exports.GeometricalBrownianMotionRef_to_json = exports.GeometricalBrownianMotionRef_fromJSON_string = exports.GeometricalBrownianMotionRef_fromJSON = exports.GeometricalBrownianMotionRef_equal = exports.GeometricalBrownianMotion_from_json_string = exports.GeometricalBrownianMotion_to_json_string = exports.GeometricalBrownianMotion_from_json = exports.GeometricalBrownianMotion_to_json = exports.GeometricalBrownianMotion_fromJSON_string = exports.GeometricalBrownianMotion_fromJSON = void 0;
exports.Updater = exports.UpdaterDto = exports.UpdaterDoc = exports.EvaluationResults_from_json_string = exports.EvaluationResults_to_json_string = exports.EvaluationResults_from_json = exports.EvaluationResults_to_json = exports.EvaluationResults_fromJSON_string = exports.EvaluationResults_fromJSON = exports.EvaluationResults_equal = exports.Result_from_json_string = exports.Result_to_json_string = exports.Result_from_json = exports.Result_to_json = exports.Result_fromJSON_string = exports.Result_fromJSON = exports.Result_equal = exports.Model_from_json_string = exports.Model_to_json_string = exports.Model_from_json = exports.Model_to_json = exports.Model_fromJSON_string = exports.Model_fromJSON = exports.Model_equal = exports.Parameter_from_json_string = exports.Parameter_to_json_string = exports.Parameter_from_json = exports.Parameter_to_json = exports.Parameter_fromJSON_string = exports.Parameter_fromJSON = exports.Parameter_equal = exports.EvaluationPoint_from_json_string = exports.EvaluationPoint_to_json_string = exports.EvaluationPoint_from_json = exports.EvaluationPoint_to_json = exports.EvaluationPoint_fromJSON_string = exports.EvaluationPoint_fromJSON = exports.EvaluationPoint_equal = exports.Histogram_from_json_string = exports.Histogram_to_json_string = exports.Histogram_from_json = exports.Histogram_to_json = exports.Histogram_fromJSON_string = exports.Histogram_fromJSON = exports.Histogram_equal = exports.HistogramAxis_from_json_string = exports.HistogramAxis_to_json_string = exports.HistogramAxis_from_json = exports.HistogramAxis_to_json = exports.HistogramAxis_fromJSON_string = void 0;
exports.EvaluationResults = exports.Result = exports.Model = exports.Parameter = exports.EvaluationPoint = exports.Histogram = exports.HistogramAxis = exports.Multiplication = exports.Linear1DInterpolation = exports.Barrier = exports.Option = exports.ZeroCouponBond = exports.GeometricalBrownianMotionRef = exports.GeometricalBrownianMotion = exports.BrownianMotionRef = exports.BrownianMotion = exports.CorrelatedGaussian = exports.IndependentGaussian = void 0;
function list_equal(a, b, eq) {
    if (a.length !== b.length)
        return false;
    for (var i = 0; i < a.length; i++)
        if (!eq(a[i], b[i]))
            return false;
    return true;
}
function float_equal(a, b) {
    if (Number.isNaN(a) && Number.isNaN(b))
        return true;
    return a === b;
}
function int_equal(a, b) {
    return a === b;
}
function string_equal(a, b) {
    return a === b;
}
var UpdaterDoc = /** @class */ (function () {
    function UpdaterDoc(name, title, doc_md, start, nargs_min, nrefs_min) {
        if (name === void 0) { name = ""; }
        if (title === void 0) { title = ""; }
        if (doc_md === void 0) { doc_md = ""; }
        if (start === void 0) { start = ""; }
        if (nargs_min === void 0) { nargs_min = -88; }
        if (nrefs_min === void 0) { nrefs_min = -88; }
        this.name = name;
        this.title = title;
        this.doc_md = doc_md;
        this.start = start;
        this.nargs_min = nargs_min;
        this.nrefs_min = nrefs_min;
    }
    UpdaterDoc.prototype.json = function () {
        return UpdaterDoc_to_json_string(this);
    };
    return UpdaterDoc;
}());
exports.UpdaterDoc = UpdaterDoc;
function UpdaterDoc_equal(a, b) {
    if (!string_equal(a.name, b.name))
        return false;
    if (!string_equal(a.title, b.title))
        return false;
    if (!string_equal(a.doc_md, b.doc_md))
        return false;
    if (!string_equal(a.start, b.start))
        return false;
    if (!int_equal(a.nargs_min, b.nargs_min))
        return false;
    if (!int_equal(a.nrefs_min, b.nrefs_min))
        return false;
    return true;
}
exports.UpdaterDoc_equal = UpdaterDoc_equal;
function UpdaterDoc_fromJSON(j, obj) {
    obj.name = j["name"];
    obj.title = j["title"];
    obj.doc_md = j["doc_md"];
    obj.start = j["start"];
    obj.nargs_min = j["nargs_min"];
    obj.nrefs_min = j["nrefs_min"];
}
exports.UpdaterDoc_fromJSON = UpdaterDoc_fromJSON;
function UpdaterDoc_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new UpdaterDoc();
    UpdaterDoc_fromJSON(j, obj);
    return obj;
}
exports.UpdaterDoc_fromJSON_string = UpdaterDoc_fromJSON_string;
function UpdaterDoc_to_json(j, obj) {
    j["name"] = obj.name;
    j["title"] = obj.title;
    j["doc_md"] = obj.doc_md;
    j["start"] = obj.start;
    j["nargs_min"] = obj.nargs_min;
    j["nrefs_min"] = obj.nrefs_min;
}
exports.UpdaterDoc_to_json = UpdaterDoc_to_json;
function UpdaterDoc_from_json(j, obj) {
    obj.name = j["name"];
    obj.title = j["title"];
    obj.doc_md = j["doc_md"];
    obj.start = j["start"];
    obj.nargs_min = j["nargs_min"];
    obj.nrefs_min = j["nrefs_min"];
}
exports.UpdaterDoc_from_json = UpdaterDoc_from_json;
function UpdaterDoc_to_json_string(self) {
    var j = {};
    UpdaterDoc_to_json(j, self);
    return JSON.stringify(j);
}
exports.UpdaterDoc_to_json_string = UpdaterDoc_to_json_string;
function UpdaterDoc_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new UpdaterDoc();
    UpdaterDoc_from_json(j, obj);
    return obj;
}
exports.UpdaterDoc_from_json_string = UpdaterDoc_from_json_string;
var UpdaterDto = /** @class */ (function () {
    function UpdaterDto(name, refs, args, start) {
        if (name === void 0) { name = ""; }
        if (refs === void 0) { refs = undefined; }
        if (args === void 0) { args = undefined; }
        if (start === void 0) { start = undefined; }
        this.name = name;
        this.refs = refs;
        this.args = args;
        this.start = start;
    }
    UpdaterDto.prototype.json = function () {
        return UpdaterDto_to_json_string(this);
    };
    return UpdaterDto;
}());
exports.UpdaterDto = UpdaterDto;
function UpdaterDto_equal(a, b) {
    if (!string_equal(a.name, b.name))
        return false;
    if (a.refs === undefined && b.refs !== undefined)
        return false;
    if (a.refs !== undefined && b.refs === undefined)
        return false;
    if (a.refs !== undefined && b.refs !== undefined)
        if (!list_equal(a.refs, b.refs, int_equal))
            return false;
    if (a.args === undefined && b.args !== undefined)
        return false;
    if (a.args !== undefined && b.args === undefined)
        return false;
    if (a.args !== undefined && b.args !== undefined)
        if (!list_equal(a.args, b.args, float_equal))
            return false;
    if (a.start === undefined && b.start !== undefined)
        return false;
    if (a.start !== undefined && b.start === undefined)
        return false;
    if (a.start !== undefined && b.start !== undefined)
        if (!float_equal(a.start, b.start))
            return false;
    return true;
}
exports.UpdaterDto_equal = UpdaterDto_equal;
function UpdaterDto_fromJSON(j, obj) {
    obj.name = j["name"];
    if ("refs" in j)
        obj.refs = j["refs"];
    if ("args" in j)
        obj.args = j["args"];
    if ("start" in j)
        obj.start = j["start"];
}
exports.UpdaterDto_fromJSON = UpdaterDto_fromJSON;
function UpdaterDto_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new UpdaterDto();
    UpdaterDto_fromJSON(j, obj);
    return obj;
}
exports.UpdaterDto_fromJSON_string = UpdaterDto_fromJSON_string;
function UpdaterDto_to_json(j, obj) {
    j["name"] = obj.name;
    if (obj.refs !== undefined) {
        j["refs"] = obj.refs;
    }
    if (obj.args !== undefined) {
        j["args"] = obj.args;
    }
    if (obj.start !== undefined) {
        j["start"] = obj.start;
    }
}
exports.UpdaterDto_to_json = UpdaterDto_to_json;
function UpdaterDto_from_json(j, obj) {
    obj.name = j["name"];
    if ("refs" in j)
        obj.refs = j["refs"];
    else
        obj.refs = undefined;
    if ("args" in j)
        obj.args = j["args"];
    else
        obj.args = undefined;
    if ("start" in j)
        obj.start = j["start"];
    else
        obj.start = undefined;
}
exports.UpdaterDto_from_json = UpdaterDto_from_json;
function UpdaterDto_to_json_string(self) {
    var j = {};
    UpdaterDto_to_json(j, self);
    return JSON.stringify(j);
}
exports.UpdaterDto_to_json_string = UpdaterDto_to_json_string;
function UpdaterDto_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new UpdaterDto();
    UpdaterDto_from_json(j, obj);
    return obj;
}
exports.UpdaterDto_from_json_string = UpdaterDto_from_json_string;
var Updater = /** @class */ (function (_super) {
    __extends(Updater, _super);
    function Updater(name, refs, args, start, title) {
        if (name === void 0) { name = ""; }
        if (refs === void 0) { refs = []; }
        if (args === void 0) { args = []; }
        if (start === void 0) { start = undefined; }
        if (title === void 0) { title = ""; }
        var _this = _super.call(this, name, refs, args, start) || this;
        _this._equation = -88;
        _this._state = -88;
        _this.title = title;
        return _this;
    }
    Updater.prototype.GetStateNumber = function () {
        if (this._state < 0)
            throw new Error("Updater ".concat(this.name, " has no state."));
        return this._state;
    };
    Updater.prototype.GetEquationNumber = function () {
        if (this._equation < 0)
            throw new Error("Updater ".concat(this.name, " has no _equation."));
        return this._equation;
    };
    Updater.prototype.HasState = function () {
        return this.start !== undefined;
    };
    Updater.prototype.GetStart = function () {
        if (this.start === undefined)
            throw new Error("start");
        return this.start;
    };
    Updater.prototype.json = function () {
        return Updater_to_json_string(this);
    };
    return Updater;
}(UpdaterDto));
exports.Updater = Updater;
function Updater_equal(a, b) {
    if (!UpdaterDto_equal(a, b))
        return false;
    return true;
}
exports.Updater_equal = Updater_equal;
function Updater_fromJSON(j, obj) {
    UpdaterDto_fromJSON(j, obj);
}
exports.Updater_fromJSON = Updater_fromJSON;
function Updater_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Updater();
    Updater_fromJSON(j, obj);
    return obj;
}
exports.Updater_fromJSON_string = Updater_fromJSON_string;
function Updater_to_json(j, obj) {
    UpdaterDto_to_json(j, obj);
}
exports.Updater_to_json = Updater_to_json;
function Updater_from_json(j, obj) {
    UpdaterDto_from_json(j, obj);
}
exports.Updater_from_json = Updater_from_json;
function Updater_to_json_string(self) {
    var j = {};
    Updater_to_json(j, self);
    return JSON.stringify(j);
}
exports.Updater_to_json_string = Updater_to_json_string;
function Updater_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Updater();
    Updater_from_json(j, obj);
    return obj;
}
exports.Updater_from_json_string = Updater_from_json_string;
var IndependentGaussian = /** @class */ (function (_super) {
    __extends(IndependentGaussian, _super);
    function IndependentGaussian(refs, title) {
        if (refs === void 0) { refs = []; }
        if (title === void 0) { title = ""; }
        return _super.call(this, "IndependentGaussian", refs, [], undefined, title) || this;
    }
    IndependentGaussian.prototype.json = function () {
        return IndependentGaussian_to_json_string(this);
    };
    return IndependentGaussian;
}(Updater));
exports.IndependentGaussian = IndependentGaussian;
function IndependentGaussian_equal(a, b) {
    if (!Updater_equal(a, b))
        return false;
    return true;
}
exports.IndependentGaussian_equal = IndependentGaussian_equal;
function IndependentGaussian_fromJSON(j, obj) {
    Updater_fromJSON(j, obj);
}
exports.IndependentGaussian_fromJSON = IndependentGaussian_fromJSON;
function IndependentGaussian_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new IndependentGaussian();
    IndependentGaussian_fromJSON(j, obj);
    return obj;
}
exports.IndependentGaussian_fromJSON_string = IndependentGaussian_fromJSON_string;
function IndependentGaussian_to_json(j, obj) {
    Updater_to_json(j, obj);
}
exports.IndependentGaussian_to_json = IndependentGaussian_to_json;
function IndependentGaussian_from_json(j, obj) {
    Updater_from_json(j, obj);
}
exports.IndependentGaussian_from_json = IndependentGaussian_from_json;
function IndependentGaussian_to_json_string(self) {
    var j = {};
    IndependentGaussian_to_json(j, self);
    return JSON.stringify(j);
}
exports.IndependentGaussian_to_json_string = IndependentGaussian_to_json_string;
function IndependentGaussian_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new IndependentGaussian();
    IndependentGaussian_from_json(j, obj);
    return obj;
}
exports.IndependentGaussian_from_json_string = IndependentGaussian_from_json_string;
var CorrelatedGaussian = /** @class */ (function (_super) {
    __extends(CorrelatedGaussian, _super);
    function CorrelatedGaussian(correlation, state1, state2, title) {
        if (correlation === void 0) { correlation = Number.NaN; }
        if (state1 === void 0) { state1 = -88; }
        if (state2 === void 0) { state2 = -88; }
        if (title === void 0) { title = ""; }
        return _super.call(this, "CorrelatedGaussian", [state1, state2], [correlation], undefined, title) || this;
    }
    CorrelatedGaussian.prototype.json = function () {
        return CorrelatedGaussian_to_json_string(this);
    };
    return CorrelatedGaussian;
}(Updater));
exports.CorrelatedGaussian = CorrelatedGaussian;
function CorrelatedGaussian_equal(a, b) {
    if (!Updater_equal(a, b))
        return false;
    return true;
}
exports.CorrelatedGaussian_equal = CorrelatedGaussian_equal;
function CorrelatedGaussian_fromJSON(j, obj) {
    Updater_fromJSON(j, obj);
}
exports.CorrelatedGaussian_fromJSON = CorrelatedGaussian_fromJSON;
function CorrelatedGaussian_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new CorrelatedGaussian();
    CorrelatedGaussian_fromJSON(j, obj);
    return obj;
}
exports.CorrelatedGaussian_fromJSON_string = CorrelatedGaussian_fromJSON_string;
function CorrelatedGaussian_to_json(j, obj) {
    Updater_to_json(j, obj);
}
exports.CorrelatedGaussian_to_json = CorrelatedGaussian_to_json;
function CorrelatedGaussian_from_json(j, obj) {
    Updater_from_json(j, obj);
}
exports.CorrelatedGaussian_from_json = CorrelatedGaussian_from_json;
function CorrelatedGaussian_to_json_string(self) {
    var j = {};
    CorrelatedGaussian_to_json(j, self);
    return JSON.stringify(j);
}
exports.CorrelatedGaussian_to_json_string = CorrelatedGaussian_to_json_string;
function CorrelatedGaussian_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new CorrelatedGaussian();
    CorrelatedGaussian_from_json(j, obj);
    return obj;
}
exports.CorrelatedGaussian_from_json_string = CorrelatedGaussian_from_json_string;
var BrownianMotion = /** @class */ (function (_super) {
    __extends(BrownianMotion, _super);
    function BrownianMotion(start, drift, diffusion, title) {
        if (start === void 0) { start = Number.NaN; }
        if (drift === void 0) { drift = Number.NaN; }
        if (diffusion === void 0) { diffusion = Number.NaN; }
        if (title === void 0) { title = ""; }
        return _super.call(this, "BrownianMotion", [], [drift, diffusion], start, title) || this;
    }
    BrownianMotion.prototype.json = function () {
        return BrownianMotion_to_json_string(this);
    };
    return BrownianMotion;
}(Updater));
exports.BrownianMotion = BrownianMotion;
function BrownianMotion_equal(a, b) {
    if (!Updater_equal(a, b))
        return false;
    return true;
}
exports.BrownianMotion_equal = BrownianMotion_equal;
function BrownianMotion_fromJSON(j, obj) {
    Updater_fromJSON(j, obj);
}
exports.BrownianMotion_fromJSON = BrownianMotion_fromJSON;
function BrownianMotion_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new BrownianMotion();
    BrownianMotion_fromJSON(j, obj);
    return obj;
}
exports.BrownianMotion_fromJSON_string = BrownianMotion_fromJSON_string;
function BrownianMotion_to_json(j, obj) {
    Updater_to_json(j, obj);
}
exports.BrownianMotion_to_json = BrownianMotion_to_json;
function BrownianMotion_from_json(j, obj) {
    Updater_from_json(j, obj);
}
exports.BrownianMotion_from_json = BrownianMotion_from_json;
function BrownianMotion_to_json_string(self) {
    var j = {};
    BrownianMotion_to_json(j, self);
    return JSON.stringify(j);
}
exports.BrownianMotion_to_json_string = BrownianMotion_to_json_string;
function BrownianMotion_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new BrownianMotion();
    BrownianMotion_from_json(j, obj);
    return obj;
}
exports.BrownianMotion_from_json_string = BrownianMotion_from_json_string;
var BrownianMotionRef = /** @class */ (function (_super) {
    __extends(BrownianMotionRef, _super);
    function BrownianMotionRef(start, drift, diffusion, title) {
        if (start === void 0) { start = Number.NaN; }
        if (drift === void 0) { drift = -88; }
        if (diffusion === void 0) { diffusion = -88; }
        if (title === void 0) { title = ""; }
        return _super.call(this, "BrownianMotion", [drift, diffusion], [], start, title) || this;
    }
    BrownianMotionRef.prototype.json = function () {
        return BrownianMotionRef_to_json_string(this);
    };
    return BrownianMotionRef;
}(Updater));
exports.BrownianMotionRef = BrownianMotionRef;
function BrownianMotionRef_equal(a, b) {
    if (!Updater_equal(a, b))
        return false;
    return true;
}
exports.BrownianMotionRef_equal = BrownianMotionRef_equal;
function BrownianMotionRef_fromJSON(j, obj) {
    Updater_fromJSON(j, obj);
}
exports.BrownianMotionRef_fromJSON = BrownianMotionRef_fromJSON;
function BrownianMotionRef_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new BrownianMotionRef();
    BrownianMotionRef_fromJSON(j, obj);
    return obj;
}
exports.BrownianMotionRef_fromJSON_string = BrownianMotionRef_fromJSON_string;
function BrownianMotionRef_to_json(j, obj) {
    Updater_to_json(j, obj);
}
exports.BrownianMotionRef_to_json = BrownianMotionRef_to_json;
function BrownianMotionRef_from_json(j, obj) {
    Updater_from_json(j, obj);
}
exports.BrownianMotionRef_from_json = BrownianMotionRef_from_json;
function BrownianMotionRef_to_json_string(self) {
    var j = {};
    BrownianMotionRef_to_json(j, self);
    return JSON.stringify(j);
}
exports.BrownianMotionRef_to_json_string = BrownianMotionRef_to_json_string;
function BrownianMotionRef_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new BrownianMotionRef();
    BrownianMotionRef_from_json(j, obj);
    return obj;
}
exports.BrownianMotionRef_from_json_string = BrownianMotionRef_from_json_string;
var GeometricalBrownianMotion = /** @class */ (function (_super) {
    __extends(GeometricalBrownianMotion, _super);
    function GeometricalBrownianMotion(start, drift, diffusion, title) {
        if (start === void 0) { start = Number.NaN; }
        if (drift === void 0) { drift = Number.NaN; }
        if (diffusion === void 0) { diffusion = Number.NaN; }
        if (title === void 0) { title = ""; }
        return _super.call(this, "GeometricalBrownianMotion", [], [drift, diffusion], start, title) || this;
    }
    GeometricalBrownianMotion.prototype.json = function () {
        return GeometricalBrownianMotion_to_json_string(this);
    };
    return GeometricalBrownianMotion;
}(Updater));
exports.GeometricalBrownianMotion = GeometricalBrownianMotion;
function GeometricalBrownianMotion_equal(a, b) {
    if (!Updater_equal(a, b))
        return false;
    return true;
}
exports.GeometricalBrownianMotion_equal = GeometricalBrownianMotion_equal;
function GeometricalBrownianMotion_fromJSON(j, obj) {
    Updater_fromJSON(j, obj);
}
exports.GeometricalBrownianMotion_fromJSON = GeometricalBrownianMotion_fromJSON;
function GeometricalBrownianMotion_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new GeometricalBrownianMotion();
    GeometricalBrownianMotion_fromJSON(j, obj);
    return obj;
}
exports.GeometricalBrownianMotion_fromJSON_string = GeometricalBrownianMotion_fromJSON_string;
function GeometricalBrownianMotion_to_json(j, obj) {
    Updater_to_json(j, obj);
}
exports.GeometricalBrownianMotion_to_json = GeometricalBrownianMotion_to_json;
function GeometricalBrownianMotion_from_json(j, obj) {
    Updater_from_json(j, obj);
}
exports.GeometricalBrownianMotion_from_json = GeometricalBrownianMotion_from_json;
function GeometricalBrownianMotion_to_json_string(self) {
    var j = {};
    GeometricalBrownianMotion_to_json(j, self);
    return JSON.stringify(j);
}
exports.GeometricalBrownianMotion_to_json_string = GeometricalBrownianMotion_to_json_string;
function GeometricalBrownianMotion_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new GeometricalBrownianMotion();
    GeometricalBrownianMotion_from_json(j, obj);
    return obj;
}
exports.GeometricalBrownianMotion_from_json_string = GeometricalBrownianMotion_from_json_string;
var GeometricalBrownianMotionRef = /** @class */ (function (_super) {
    __extends(GeometricalBrownianMotionRef, _super);
    function GeometricalBrownianMotionRef(start, drift, diffusion, title) {
        if (start === void 0) { start = Number.NaN; }
        if (drift === void 0) { drift = -88; }
        if (diffusion === void 0) { diffusion = -88; }
        if (title === void 0) { title = ""; }
        return _super.call(this, "GeometricalBrownianMotion", [drift, diffusion], [], start, title) || this;
    }
    GeometricalBrownianMotionRef.prototype.json = function () {
        return GeometricalBrownianMotionRef_to_json_string(this);
    };
    return GeometricalBrownianMotionRef;
}(Updater));
exports.GeometricalBrownianMotionRef = GeometricalBrownianMotionRef;
function GeometricalBrownianMotionRef_equal(a, b) {
    if (!Updater_equal(a, b))
        return false;
    return true;
}
exports.GeometricalBrownianMotionRef_equal = GeometricalBrownianMotionRef_equal;
function GeometricalBrownianMotionRef_fromJSON(j, obj) {
    Updater_fromJSON(j, obj);
}
exports.GeometricalBrownianMotionRef_fromJSON = GeometricalBrownianMotionRef_fromJSON;
function GeometricalBrownianMotionRef_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new GeometricalBrownianMotionRef();
    GeometricalBrownianMotionRef_fromJSON(j, obj);
    return obj;
}
exports.GeometricalBrownianMotionRef_fromJSON_string = GeometricalBrownianMotionRef_fromJSON_string;
function GeometricalBrownianMotionRef_to_json(j, obj) {
    Updater_to_json(j, obj);
}
exports.GeometricalBrownianMotionRef_to_json = GeometricalBrownianMotionRef_to_json;
function GeometricalBrownianMotionRef_from_json(j, obj) {
    Updater_from_json(j, obj);
}
exports.GeometricalBrownianMotionRef_from_json = GeometricalBrownianMotionRef_from_json;
function GeometricalBrownianMotionRef_to_json_string(self) {
    var j = {};
    GeometricalBrownianMotionRef_to_json(j, self);
    return JSON.stringify(j);
}
exports.GeometricalBrownianMotionRef_to_json_string = GeometricalBrownianMotionRef_to_json_string;
function GeometricalBrownianMotionRef_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new GeometricalBrownianMotionRef();
    GeometricalBrownianMotionRef_from_json(j, obj);
    return obj;
}
exports.GeometricalBrownianMotionRef_from_json_string = GeometricalBrownianMotionRef_from_json_string;
var ZeroCouponBond = /** @class */ (function (_super) {
    __extends(ZeroCouponBond, _super);
    function ZeroCouponBond(underlying, start, title) {
        if (underlying === void 0) { underlying = -88; }
        if (start === void 0) { start = Number.NaN; }
        if (title === void 0) { title = ""; }
        return _super.call(this, "ZeroCouponBond", [underlying], [], start, title) || this;
    }
    ZeroCouponBond.prototype.json = function () {
        return ZeroCouponBond_to_json_string(this);
    };
    return ZeroCouponBond;
}(Updater));
exports.ZeroCouponBond = ZeroCouponBond;
function ZeroCouponBond_equal(a, b) {
    if (!Updater_equal(a, b))
        return false;
    return true;
}
exports.ZeroCouponBond_equal = ZeroCouponBond_equal;
function ZeroCouponBond_fromJSON(j, obj) {
    Updater_fromJSON(j, obj);
}
exports.ZeroCouponBond_fromJSON = ZeroCouponBond_fromJSON;
function ZeroCouponBond_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new ZeroCouponBond();
    ZeroCouponBond_fromJSON(j, obj);
    return obj;
}
exports.ZeroCouponBond_fromJSON_string = ZeroCouponBond_fromJSON_string;
function ZeroCouponBond_to_json(j, obj) {
    Updater_to_json(j, obj);
}
exports.ZeroCouponBond_to_json = ZeroCouponBond_to_json;
function ZeroCouponBond_from_json(j, obj) {
    Updater_from_json(j, obj);
}
exports.ZeroCouponBond_from_json = ZeroCouponBond_from_json;
function ZeroCouponBond_to_json_string(self) {
    var j = {};
    ZeroCouponBond_to_json(j, self);
    return JSON.stringify(j);
}
exports.ZeroCouponBond_to_json_string = ZeroCouponBond_to_json_string;
function ZeroCouponBond_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new ZeroCouponBond();
    ZeroCouponBond_from_json(j, obj);
    return obj;
}
exports.ZeroCouponBond_from_json_string = ZeroCouponBond_from_json_string;
var Option = /** @class */ (function (_super) {
    __extends(Option, _super);
    function Option(underlying, strike, call_put, title) {
        if (underlying === void 0) { underlying = -88; }
        if (strike === void 0) { strike = Number.NaN; }
        if (call_put === void 0) { call_put = -88; }
        if (title === void 0) { title = ""; }
        return _super.call(this, "Option", [underlying], [strike, call_put], 0, title) || this;
    }
    Option.prototype.json = function () {
        return Option_to_json_string(this);
    };
    Option.Call = 0;
    Option.Put = 1;
    return Option;
}(Updater));
exports.Option = Option;
function Option_equal(a, b) {
    if (!Updater_equal(a, b))
        return false;
    return true;
}
exports.Option_equal = Option_equal;
function Option_fromJSON(j, obj) {
    Updater_fromJSON(j, obj);
}
exports.Option_fromJSON = Option_fromJSON;
function Option_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Option();
    Option_fromJSON(j, obj);
    return obj;
}
exports.Option_fromJSON_string = Option_fromJSON_string;
function Option_to_json(j, obj) {
    Updater_to_json(j, obj);
}
exports.Option_to_json = Option_to_json;
function Option_from_json(j, obj) {
    Updater_from_json(j, obj);
}
exports.Option_from_json = Option_from_json;
function Option_to_json_string(self) {
    var j = {};
    Option_to_json(j, self);
    return JSON.stringify(j);
}
exports.Option_to_json_string = Option_to_json_string;
function Option_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Option();
    Option_from_json(j, obj);
    return obj;
}
exports.Option_from_json_string = Option_from_json_string;
var Barrier = /** @class */ (function (_super) {
    __extends(Barrier, _super);
    function Barrier(underlying, start, level, direction, action, value, title) {
        if (underlying === void 0) { underlying = -88; }
        if (start === void 0) { start = Number.NaN; }
        if (level === void 0) { level = Number.NaN; }
        if (direction === void 0) { direction = -88; }
        if (action === void 0) { action = -88; }
        if (value === void 0) { value = Number.NaN; }
        if (title === void 0) { title = ""; }
        return _super.call(this, "Barrier", [underlying], [level, value, direction, action], start, title) || this;
    }
    Barrier.prototype.json = function () {
        return Barrier_to_json_string(this);
    };
    Barrier.DirectionUp = 1;
    Barrier.DirectionDown = -1;
    Barrier.DirectionAny = 0;
    Barrier.ActionSet = 0;
    return Barrier;
}(Updater));
exports.Barrier = Barrier;
function Barrier_equal(a, b) {
    if (!Updater_equal(a, b))
        return false;
    return true;
}
exports.Barrier_equal = Barrier_equal;
function Barrier_fromJSON(j, obj) {
    Updater_fromJSON(j, obj);
}
exports.Barrier_fromJSON = Barrier_fromJSON;
function Barrier_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Barrier();
    Barrier_fromJSON(j, obj);
    return obj;
}
exports.Barrier_fromJSON_string = Barrier_fromJSON_string;
function Barrier_to_json(j, obj) {
    Updater_to_json(j, obj);
}
exports.Barrier_to_json = Barrier_to_json;
function Barrier_from_json(j, obj) {
    Updater_from_json(j, obj);
}
exports.Barrier_from_json = Barrier_from_json;
function Barrier_to_json_string(self) {
    var j = {};
    Barrier_to_json(j, self);
    return JSON.stringify(j);
}
exports.Barrier_to_json_string = Barrier_to_json_string;
function Barrier_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Barrier();
    Barrier_from_json(j, obj);
    return obj;
}
exports.Barrier_from_json_string = Barrier_from_json_string;
var Linear1DInterpolation = /** @class */ (function (_super) {
    __extends(Linear1DInterpolation, _super);
    function Linear1DInterpolation(ref, xmin, xmax, y, title) {
        if (ref === void 0) { ref = -88; }
        if (xmin === void 0) { xmin = -1; }
        if (xmax === void 0) { xmax = 1; }
        if (y === void 0) { y = []; }
        if (title === void 0) { title = ""; }
        var _this = _super.call(this, "Linear1DInterpolation", [ref], [], 0, title) || this;
        if (y.length < 2)
            throw new Error("Linear1DInterpolation: y-vector must have at least 2 elements: y(xmin), y(xmax)");
        _this.args = __spreadArray(__spreadArray([], [xmin, xmax], false), y, true);
        return _this;
    }
    Linear1DInterpolation.prototype.json = function () {
        return Linear1DInterpolation_to_json_string(this);
    };
    return Linear1DInterpolation;
}(Updater));
exports.Linear1DInterpolation = Linear1DInterpolation;
function Linear1DInterpolation_equal(a, b) {
    if (!Updater_equal(a, b))
        return false;
    return true;
}
exports.Linear1DInterpolation_equal = Linear1DInterpolation_equal;
function Linear1DInterpolation_fromJSON(j, obj) {
    Updater_fromJSON(j, obj);
}
exports.Linear1DInterpolation_fromJSON = Linear1DInterpolation_fromJSON;
function Linear1DInterpolation_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Linear1DInterpolation();
    Linear1DInterpolation_fromJSON(j, obj);
    return obj;
}
exports.Linear1DInterpolation_fromJSON_string = Linear1DInterpolation_fromJSON_string;
function Linear1DInterpolation_to_json(j, obj) {
    Updater_to_json(j, obj);
}
exports.Linear1DInterpolation_to_json = Linear1DInterpolation_to_json;
function Linear1DInterpolation_from_json(j, obj) {
    Updater_from_json(j, obj);
}
exports.Linear1DInterpolation_from_json = Linear1DInterpolation_from_json;
function Linear1DInterpolation_to_json_string(self) {
    var j = {};
    Linear1DInterpolation_to_json(j, self);
    return JSON.stringify(j);
}
exports.Linear1DInterpolation_to_json_string = Linear1DInterpolation_to_json_string;
function Linear1DInterpolation_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Linear1DInterpolation();
    Linear1DInterpolation_from_json(j, obj);
    return obj;
}
exports.Linear1DInterpolation_from_json_string = Linear1DInterpolation_from_json_string;
var Multiplication = /** @class */ (function (_super) {
    __extends(Multiplication, _super);
    function Multiplication(refs, factor, title) {
        if (refs === void 0) { refs = []; }
        if (factor === void 0) { factor = 1; }
        if (title === void 0) { title = ""; }
        return _super.call(this, "Multiplication", refs, [factor], 0, title) || this;
    }
    Multiplication.prototype.json = function () {
        return Multiplication_to_json_string(this);
    };
    return Multiplication;
}(Updater));
exports.Multiplication = Multiplication;
function Multiplication_equal(a, b) {
    if (!Updater_equal(a, b))
        return false;
    return true;
}
exports.Multiplication_equal = Multiplication_equal;
function Multiplication_fromJSON(j, obj) {
    Updater_fromJSON(j, obj);
}
exports.Multiplication_fromJSON = Multiplication_fromJSON;
function Multiplication_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Multiplication();
    Multiplication_fromJSON(j, obj);
    return obj;
}
exports.Multiplication_fromJSON_string = Multiplication_fromJSON_string;
function Multiplication_to_json(j, obj) {
    Updater_to_json(j, obj);
}
exports.Multiplication_to_json = Multiplication_to_json;
function Multiplication_from_json(j, obj) {
    Updater_from_json(j, obj);
}
exports.Multiplication_from_json = Multiplication_from_json;
function Multiplication_to_json_string(self) {
    var j = {};
    Multiplication_to_json(j, self);
    return JSON.stringify(j);
}
exports.Multiplication_to_json_string = Multiplication_to_json_string;
function Multiplication_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Multiplication();
    Multiplication_from_json(j, obj);
    return obj;
}
exports.Multiplication_from_json_string = Multiplication_from_json_string;
var HistogramAxis = /** @class */ (function () {
    function HistogramAxis(_state, _nbins, _min, _max) {
        if (_state === void 0) { _state = -88; }
        if (_nbins === void 0) { _nbins = -88; }
        if (_min === void 0) { _min = -88; }
        if (_max === void 0) { _max = -88; }
        this.state = _state;
        this.nbins = _nbins;
        this.min = _min;
        this.max = _max;
    }
    HistogramAxis.prototype.json = function () {
        return HistogramAxis_to_json_string(this);
    };
    return HistogramAxis;
}());
exports.HistogramAxis = HistogramAxis;
function HistogramAxis_equal(a, b) {
    if (!int_equal(a.state, b.state))
        return false;
    if (!int_equal(a.nbins, b.nbins))
        return false;
    if (!float_equal(a.min, b.min))
        return false;
    if (!float_equal(a.max, b.max))
        return false;
    return true;
}
exports.HistogramAxis_equal = HistogramAxis_equal;
function HistogramAxis_fromJSON(j, obj) {
    obj.state = j["state"];
    obj.nbins = j["nbins"];
    obj.min = j["min"];
    obj.max = j["max"];
}
exports.HistogramAxis_fromJSON = HistogramAxis_fromJSON;
function HistogramAxis_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new HistogramAxis();
    HistogramAxis_fromJSON(j, obj);
    return obj;
}
exports.HistogramAxis_fromJSON_string = HistogramAxis_fromJSON_string;
function HistogramAxis_to_json(j, obj) {
    j["state"] = obj.state;
    j["nbins"] = obj.nbins;
    j["min"] = obj.min;
    j["max"] = obj.max;
}
exports.HistogramAxis_to_json = HistogramAxis_to_json;
function HistogramAxis_from_json(j, obj) {
    obj.state = j["state"];
    obj.nbins = j["nbins"];
    obj.min = j["min"];
    obj.max = j["max"];
}
exports.HistogramAxis_from_json = HistogramAxis_from_json;
function HistogramAxis_to_json_string(self) {
    var j = {};
    HistogramAxis_to_json(j, self);
    return JSON.stringify(j);
}
exports.HistogramAxis_to_json_string = HistogramAxis_to_json_string;
function HistogramAxis_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new HistogramAxis();
    HistogramAxis_from_json(j, obj);
    return obj;
}
exports.HistogramAxis_from_json_string = HistogramAxis_from_json_string;
var Histogram = /** @class */ (function () {
    function Histogram(x, y) {
        if (x === void 0) { x = new HistogramAxis(); }
        if (y === void 0) { y = undefined; }
        this.x = x;
        this.y = y;
    }
    Histogram.prototype.json = function () {
        return Histogram_to_json_string(this);
    };
    return Histogram;
}());
exports.Histogram = Histogram;
function Histogram_equal(a, b) {
    if (!HistogramAxis_equal(a.x, b.x))
        return false;
    if (a.y === undefined && b.y !== undefined)
        return false;
    if (a.y !== undefined && b.y === undefined)
        return false;
    if (a.y !== undefined && b.y !== undefined)
        if (!HistogramAxis_equal(a.y, b.y))
            return false;
    return true;
}
exports.Histogram_equal = Histogram_equal;
function Histogram_fromJSON(j, obj) {
    obj.x = j["x"];
    if ("y" in j)
        obj.y = j["y"];
}
exports.Histogram_fromJSON = Histogram_fromJSON;
function Histogram_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Histogram();
    Histogram_fromJSON(j, obj);
    return obj;
}
exports.Histogram_fromJSON_string = Histogram_fromJSON_string;
function Histogram_to_json(j, obj) {
    {
        var jj = {};
        HistogramAxis_to_json(jj, obj.x);
        j["x"] = jj;
    }
    if (obj.y !== undefined) {
        {
            var jj = {};
            HistogramAxis_to_json(jj, obj.y);
            j["y"] = jj;
        }
    }
}
exports.Histogram_to_json = Histogram_to_json;
function Histogram_from_json(j, obj) {
    HistogramAxis_from_json(j["x"], obj.x);
    if ("y" in j)
        obj.y = j["y"];
}
exports.Histogram_from_json = Histogram_from_json;
function Histogram_to_json_string(self) {
    var j = {};
    Histogram_to_json(j, self);
    return JSON.stringify(j);
}
exports.Histogram_to_json_string = Histogram_to_json_string;
function Histogram_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Histogram();
    Histogram_from_json(j, obj);
    return obj;
}
exports.Histogram_from_json_string = Histogram_from_json_string;
var EvaluationPoint = /** @class */ (function () {
    function EvaluationPoint(state, time, value, error, histograms) {
        if (state === void 0) { state = -88; }
        if (time === void 0) { time = Number.NaN; }
        if (value === void 0) { value = undefined; }
        if (error === void 0) { error = undefined; }
        if (histograms === void 0) { histograms = []; }
        this.state = state;
        this.time = time;
        this.value = value;
        this.error = error;
        this.histograms = histograms;
    }
    EvaluationPoint.prototype.GetState = function () {
        return this.state;
    };
    EvaluationPoint.prototype.GetTime = function () {
        return this.time;
    };
    EvaluationPoint.prototype.GetValue = function () {
        if (this.value === undefined)
            throw new Error("value");
        return this.value;
    };
    EvaluationPoint.prototype.GetError = function () {
        if (this.error === undefined)
            throw new Error("error");
        return this.error;
    };
    EvaluationPoint.prototype.Add = function (histogram) {
        this.histograms.push(histogram);
        return this;
    };
    EvaluationPoint.prototype.json = function () {
        return EvaluationPoint_to_json_string(this);
    };
    return EvaluationPoint;
}());
exports.EvaluationPoint = EvaluationPoint;
function EvaluationPoint_equal(a, b) {
    if (!int_equal(a.state, b.state))
        return false;
    if (!float_equal(a.time, b.time))
        return false;
    if (a.value === undefined && b.value !== undefined)
        return false;
    if (a.value !== undefined && b.value === undefined)
        return false;
    if (a.value !== undefined && b.value !== undefined)
        if (!float_equal(a.value, b.value))
            return false;
    if (a.error === undefined && b.error !== undefined)
        return false;
    if (a.error !== undefined && b.error === undefined)
        return false;
    if (a.error !== undefined && b.error !== undefined)
        if (!float_equal(a.error, b.error))
            return false;
    if (!list_equal(a.histograms, b.histograms, Histogram_equal))
        return false;
    return true;
}
exports.EvaluationPoint_equal = EvaluationPoint_equal;
function EvaluationPoint_fromJSON(j, obj) {
    obj.state = j["state"];
    obj.time = j["time"];
    if ("value" in j)
        obj.value = j["value"];
    if ("error" in j)
        obj.error = j["error"];
    obj.histograms = j["histograms"];
}
exports.EvaluationPoint_fromJSON = EvaluationPoint_fromJSON;
function EvaluationPoint_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new EvaluationPoint();
    EvaluationPoint_fromJSON(j, obj);
    return obj;
}
exports.EvaluationPoint_fromJSON_string = EvaluationPoint_fromJSON_string;
function EvaluationPoint_to_json(j, obj) {
    j["state"] = obj.state;
    j["time"] = obj.time;
    if (obj.value !== undefined) {
        j["value"] = obj.value;
    }
    if (obj.error !== undefined) {
        j["error"] = obj.error;
    }
    j["histograms"] = [];
    for (var _i = 0, _a = obj.histograms; _i < _a.length; _i++) {
        var item = _a[_i];
        var jj = {};
        Histogram_to_json(jj, item);
        j["histograms"].push(jj);
    }
}
exports.EvaluationPoint_to_json = EvaluationPoint_to_json;
function EvaluationPoint_from_json(j, obj) {
    obj.state = j["state"];
    obj.time = j["time"];
    if ("value" in j)
        obj.value = j["value"];
    else
        obj.value = undefined;
    if ("error" in j)
        obj.error = j["error"];
    else
        obj.error = undefined;
    for (var _i = 0, _a = j["histograms"]; _i < _a.length; _i++) {
        var item = _a[_i];
        var v = new Histogram();
        Histogram_from_json(item, v);
        obj.histograms.push(v);
    }
}
exports.EvaluationPoint_from_json = EvaluationPoint_from_json;
function EvaluationPoint_to_json_string(self) {
    var j = {};
    EvaluationPoint_to_json(j, self);
    return JSON.stringify(j);
}
exports.EvaluationPoint_to_json_string = EvaluationPoint_to_json_string;
function EvaluationPoint_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new EvaluationPoint();
    EvaluationPoint_from_json(j, obj);
    return obj;
}
exports.EvaluationPoint_from_json_string = EvaluationPoint_from_json_string;
var Parameter = /** @class */ (function () {
    function Parameter(value, step, min, max) {
        if (value === void 0) { value = Number.NaN; }
        if (step === void 0) { step = Number.NaN; }
        if (min === void 0) { min = Number.NaN; }
        if (max === void 0) { max = Number.NaN; }
        this.value = value;
        this.step = step;
        this.min = min;
        this.max = max;
    }
    Parameter.prototype.json = function () {
        return Parameter_to_json_string(this);
    };
    return Parameter;
}());
exports.Parameter = Parameter;
function Parameter_equal(a, b) {
    if (!float_equal(a.value, b.value))
        return false;
    if (!float_equal(a.step, b.step))
        return false;
    if (!float_equal(a.min, b.min))
        return false;
    if (!float_equal(a.max, b.max))
        return false;
    return true;
}
exports.Parameter_equal = Parameter_equal;
function Parameter_fromJSON(j, obj) {
    obj.value = j["value"];
    obj.step = j["step"];
    obj.min = j["min"];
    obj.max = j["max"];
}
exports.Parameter_fromJSON = Parameter_fromJSON;
function Parameter_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Parameter();
    Parameter_fromJSON(j, obj);
    return obj;
}
exports.Parameter_fromJSON_string = Parameter_fromJSON_string;
function Parameter_to_json(j, obj) {
    j["value"] = obj.value;
    j["step"] = obj.step;
    j["min"] = obj.min;
    j["max"] = obj.max;
}
exports.Parameter_to_json = Parameter_to_json;
function Parameter_from_json(j, obj) {
    obj.value = j["value"];
    obj.step = j["step"];
    obj.min = j["min"];
    obj.max = j["max"];
}
exports.Parameter_from_json = Parameter_from_json;
function Parameter_to_json_string(self) {
    var j = {};
    Parameter_to_json(j, self);
    return JSON.stringify(j);
}
exports.Parameter_to_json_string = Parameter_to_json_string;
function Parameter_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Parameter();
    Parameter_from_json(j, obj);
    return obj;
}
exports.Parameter_from_json_string = Parameter_from_json_string;
var Model = /** @class */ (function () {
    function Model(TimeStart, TimeSteps, NumPaths, updaters, evaluations, RunTimeoutSeconds, MemoryLimitKB) {
        if (TimeStart === void 0) { TimeStart = Number.NaN; }
        if (TimeSteps === void 0) { TimeSteps = 0; }
        if (NumPaths === void 0) { NumPaths = 0; }
        if (updaters === void 0) { updaters = []; }
        if (evaluations === void 0) { evaluations = []; }
        if (RunTimeoutSeconds === void 0) { RunTimeoutSeconds = 1; }
        if (MemoryLimitKB === void 0) { MemoryLimitKB = 1; }
        this.TimeStart = TimeStart;
        this.TimeSteps = TimeSteps;
        this.NumPaths = NumPaths;
        this.updaters = updaters;
        this.evaluations = evaluations;
        this.RunTimeoutSeconds = RunTimeoutSeconds;
        this.MemoryLimitKB = MemoryLimitKB;
    }
    Model.prototype.GetNumberOfUpdaters = function () {
        return this.updaters.length;
    };
    Model.prototype.GetNumberOfStates = function () {
        return this.updaters.filter(function (u) { return u.HasState(); }).length;
    };
    Model.prototype.Add = function (updater) {
        this.updaters.push(updater);
        updater._equation = this.GetNumberOfUpdaters() - 1;
        if (updater.HasState())
            updater._state = this.GetNumberOfStates() - 1;
        return updater;
    };
    Model.prototype.json = function () {
        return Model_to_json_string(this);
    };
    return Model;
}());
exports.Model = Model;
function Model_equal(a, b) {
    if (!float_equal(a.TimeStart, b.TimeStart))
        return false;
    if (!int_equal(a.TimeSteps, b.TimeSteps))
        return false;
    if (!int_equal(a.NumPaths, b.NumPaths))
        return false;
    if (!list_equal(a.updaters, b.updaters, Updater_equal))
        return false;
    if (!list_equal(a.evaluations, b.evaluations, EvaluationPoint_equal))
        return false;
    if (!float_equal(a.RunTimeoutSeconds, b.RunTimeoutSeconds))
        return false;
    if (!int_equal(a.MemoryLimitKB, b.MemoryLimitKB))
        return false;
    return true;
}
exports.Model_equal = Model_equal;
function Model_fromJSON(j, obj) {
    obj.TimeStart = j["TimeStart"];
    obj.TimeSteps = j["TimeSteps"];
    obj.NumPaths = j["NumPaths"];
    obj.updaters = j["updaters"];
    obj.evaluations = j["evaluations"];
    obj.RunTimeoutSeconds = j["RunTimeoutSeconds"];
    obj.MemoryLimitKB = j["MemoryLimitKB"];
}
exports.Model_fromJSON = Model_fromJSON;
function Model_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Model();
    Model_fromJSON(j, obj);
    return obj;
}
exports.Model_fromJSON_string = Model_fromJSON_string;
function Model_to_json(j, obj) {
    j["TimeStart"] = obj.TimeStart;
    j["TimeSteps"] = obj.TimeSteps;
    j["NumPaths"] = obj.NumPaths;
    j["updaters"] = [];
    for (var _i = 0, _a = obj.updaters; _i < _a.length; _i++) {
        var item = _a[_i];
        var jj = {};
        Updater_to_json(jj, item);
        j["updaters"].push(jj);
    }
    j["evaluations"] = [];
    for (var _b = 0, _c = obj.evaluations; _b < _c.length; _b++) {
        var item = _c[_b];
        var jj = {};
        EvaluationPoint_to_json(jj, item);
        j["evaluations"].push(jj);
    }
    j["RunTimeoutSeconds"] = obj.RunTimeoutSeconds;
    j["MemoryLimitKB"] = obj.MemoryLimitKB;
}
exports.Model_to_json = Model_to_json;
function Model_from_json(j, obj) {
    obj.TimeStart = j["TimeStart"];
    obj.TimeSteps = j["TimeSteps"];
    obj.NumPaths = j["NumPaths"];
    for (var _i = 0, _a = j["updaters"]; _i < _a.length; _i++) {
        var item = _a[_i];
        var v = new Updater();
        Updater_from_json(item, v);
        obj.updaters.push(v);
    }
    for (var _b = 0, _c = j["evaluations"]; _b < _c.length; _b++) {
        var item = _c[_b];
        var v = new EvaluationPoint();
        EvaluationPoint_from_json(item, v);
        obj.evaluations.push(v);
    }
    obj.RunTimeoutSeconds = j["RunTimeoutSeconds"];
    obj.MemoryLimitKB = j["MemoryLimitKB"];
}
exports.Model_from_json = Model_from_json;
function Model_to_json_string(self) {
    var j = {};
    Model_to_json(j, self);
    return JSON.stringify(j);
}
exports.Model_to_json_string = Model_to_json_string;
function Model_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Model();
    Model_from_json(j, obj);
    return obj;
}
exports.Model_from_json_string = Model_from_json_string;
var Result = /** @class */ (function () {
    function Result(n, mean, stddev, skewness) {
        if (n === void 0) { n = 0; }
        if (mean === void 0) { mean = Number.NaN; }
        if (stddev === void 0) { stddev = Number.NaN; }
        if (skewness === void 0) { skewness = Number.NaN; }
        this.n = n;
        this.mean = mean;
        this.stddev = stddev;
        this.skewness = skewness;
    }
    Result.prototype.GetMean = function () {
        return this.mean;
    };
    Result.prototype.GetMeanError = function () {
        return this.n <= 0 ? Number.NaN : this.stddev / Math.sqrt(this.n);
    };
    Result.prototype.GetStdDev = function () {
        return this.stddev;
    };
    Result.prototype.GetSkewness = function () {
        return this.skewness;
    };
    Result.prototype.json = function () {
        return Result_to_json_string(this);
    };
    return Result;
}());
exports.Result = Result;
function Result_equal(a, b) {
    if (!int_equal(a.n, b.n))
        return false;
    if (!float_equal(a.mean, b.mean))
        return false;
    if (!float_equal(a.stddev, b.stddev))
        return false;
    if (!float_equal(a.skewness, b.skewness))
        return false;
    return true;
}
exports.Result_equal = Result_equal;
function Result_fromJSON(j, obj) {
    obj.n = j["n"];
    obj.mean = j["mean"];
    obj.stddev = j["stddev"];
    obj.skewness = j["skewness"];
}
exports.Result_fromJSON = Result_fromJSON;
function Result_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Result();
    Result_fromJSON(j, obj);
    return obj;
}
exports.Result_fromJSON_string = Result_fromJSON_string;
function Result_to_json(j, obj) {
    j["n"] = obj.n;
    j["mean"] = obj.mean;
    j["stddev"] = obj.stddev;
    j["skewness"] = obj.skewness;
}
exports.Result_to_json = Result_to_json;
function Result_from_json(j, obj) {
    obj.n = j["n"];
    obj.mean = j["mean"];
    obj.stddev = j["stddev"];
    obj.skewness = j["skewness"];
}
exports.Result_from_json = Result_from_json;
function Result_to_json_string(self) {
    var j = {};
    Result_to_json(j, self);
    return JSON.stringify(j);
}
exports.Result_to_json_string = Result_to_json_string;
function Result_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new Result();
    Result_from_json(j, obj);
    return obj;
}
exports.Result_from_json_string = Result_from_json_string;
var EvaluationResults = /** @class */ (function () {
    function EvaluationResults(names, npaths, mean, stddev, skewness, time_points, time_steps, histograms, model) {
        if (names === void 0) { names = []; }
        if (npaths === void 0) { npaths = []; }
        if (mean === void 0) { mean = []; }
        if (stddev === void 0) { stddev = []; }
        if (skewness === void 0) { skewness = []; }
        if (time_points === void 0) { time_points = []; }
        if (time_steps === void 0) { time_steps = []; }
        if (histograms === void 0) { histograms = []; }
        if (model === void 0) { model = undefined; }
        this.names = names;
        this.npaths = npaths;
        this.mean = mean;
        this.stddev = stddev;
        this.skewness = skewness;
        this.time_points = time_points;
        this.time_steps = time_steps;
        this.histograms = histograms;
        this.model = model;
    }
    EvaluationResults.prototype.GetNumberOfStates = function () {
        return this.names.length;
    };
    EvaluationResults.prototype.GetNumberOfEvaluations = function () {
        return this.time_points.length;
    };
    EvaluationResults.prototype.Index = function (state, point) {
        if (!(state >= 0 && state < this.GetNumberOfStates() && point >= 0 && point < this.GetNumberOfEvaluations()))
            throw new Error("Index");
        return point * this.GetNumberOfStates() + state;
    };
    EvaluationResults.prototype.GetStateEvaluationResult = function (state, point) {
        var n = this.Index(state, point);
        return new Result(this.npaths[n], this.mean[n], this.stddev[n], this.skewness[n]);
    };
    EvaluationResults.prototype.json = function () {
        return EvaluationResults_to_json_string(this);
    };
    return EvaluationResults;
}());
exports.EvaluationResults = EvaluationResults;
function EvaluationResults_equal(a, b) {
    if (!list_equal(a.names, b.names, string_equal))
        return false;
    if (!list_equal(a.npaths, b.npaths, int_equal))
        return false;
    if (!list_equal(a.mean, b.mean, float_equal))
        return false;
    if (!list_equal(a.stddev, b.stddev, float_equal))
        return false;
    if (!list_equal(a.skewness, b.skewness, float_equal))
        return false;
    if (!list_equal(a.time_points, b.time_points, float_equal))
        return false;
    if (!list_equal(a.time_steps, b.time_steps, int_equal))
        return false;
    if (!list_equal(a.histograms, b.histograms, Histogram_equal))
        return false;
    if (a.model === undefined && b.model !== undefined)
        return false;
    if (a.model !== undefined && b.model === undefined)
        return false;
    if (a.model !== undefined && b.model !== undefined)
        if (!Model_equal(a.model, b.model))
            return false;
    return true;
}
exports.EvaluationResults_equal = EvaluationResults_equal;
function EvaluationResults_fromJSON(j, obj) {
    obj.names = j["names"];
    obj.npaths = j["npaths"];
    obj.mean = j["mean"];
    obj.stddev = j["stddev"];
    obj.skewness = j["skewness"];
    obj.time_points = j["time_points"];
    obj.time_steps = j["time_steps"];
    obj.histograms = j["histograms"];
    if ("model" in j)
        obj.model = j["model"];
}
exports.EvaluationResults_fromJSON = EvaluationResults_fromJSON;
function EvaluationResults_fromJSON_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new EvaluationResults();
    EvaluationResults_fromJSON(j, obj);
    return obj;
}
exports.EvaluationResults_fromJSON_string = EvaluationResults_fromJSON_string;
function EvaluationResults_to_json(j, obj) {
    j["names"] = obj.names;
    j["npaths"] = obj.npaths;
    j["mean"] = obj.mean;
    j["stddev"] = obj.stddev;
    j["skewness"] = obj.skewness;
    j["time_points"] = obj.time_points;
    j["time_steps"] = obj.time_steps;
    j["histograms"] = [];
    for (var _i = 0, _a = obj.histograms; _i < _a.length; _i++) {
        var item = _a[_i];
        var jj = {};
        Histogram_to_json(jj, item);
        j["histograms"].push(jj);
    }
    if (obj.model !== undefined) {
        {
            var jj = {};
            Model_to_json(jj, obj.model);
            j["model"] = jj;
        }
    }
}
exports.EvaluationResults_to_json = EvaluationResults_to_json;
function EvaluationResults_from_json(j, obj) {
    obj.names = j["names"];
    obj.npaths = j["npaths"];
    obj.mean = j["mean"];
    obj.stddev = j["stddev"];
    obj.skewness = j["skewness"];
    obj.time_points = j["time_points"];
    obj.time_steps = j["time_steps"];
    for (var _i = 0, _a = j["histograms"]; _i < _a.length; _i++) {
        var item = _a[_i];
        var v = new Histogram();
        Histogram_from_json(item, v);
        obj.histograms.push(v);
    }
    if ("model" in j)
        obj.model = j["model"];
}
exports.EvaluationResults_from_json = EvaluationResults_from_json;
function EvaluationResults_to_json_string(self) {
    var j = {};
    EvaluationResults_to_json(j, self);
    return JSON.stringify(j);
}
exports.EvaluationResults_to_json_string = EvaluationResults_to_json_string;
function EvaluationResults_from_json_string(jstr) {
    var j = JSON.parse(jstr);
    var obj = new EvaluationResults();
    EvaluationResults_from_json(j, obj);
    return obj;
}
exports.EvaluationResults_from_json_string = EvaluationResults_from_json_string;
