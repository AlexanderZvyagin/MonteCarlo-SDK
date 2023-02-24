"use strict";
// This file was automatically generated!
// - by <software> <version>
// - from <DTO-s spec>
exports.__esModule = true;
var fs = require("fs");
var dto = require("./dto");
var dto_1 = require("./dto");
function random_int(min, max) {
    if (min === void 0) { min = -1000; }
    if (max === void 0) { max = 1000; }
    return Math.floor(min + Math.random() * (max - min + 1));
}
function yes_no() {
    return random_int(0, 1) == 1;
}
function random_optional_int() {
    return yes_no() ? random_int() : undefined;
}
function random_float(min, max) {
    if (min === void 0) { min = -1e6; }
    if (max === void 0) { max = 1e6; }
    return random_int();
}
function random_optional_float() {
    return yes_no() ? random_float() : undefined;
}
function random_string(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var out = '';
    var input = 'abcdefghijklmnopqrstuvwxyz0123456789';
    for (var i = 0; i < 32; i++)
        out += input.charAt(random_int(0, input.length));
    return out;
}
function random_optional_string() {
    return yes_no() ? random_string() : undefined;
}
function random_list_int(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = random_int(min, max);
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_int());
    return list;
}
function random_optional_list_int() {
    return yes_no() ? random_list_int() : undefined;
}
function random_list_float(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = random_int(min, max);
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_float());
    return list;
}
function random_optional_list_float() {
    return yes_no() ? random_list_float() : undefined;
}
function random_list_string(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = random_int(min, max);
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_string());
    return list;
}
function random_optional_list_string() {
    return yes_no() ? random_list_string() : undefined;
}
function random_UpdaterDoc() {
    return new dto_1.UpdaterDoc(random_string(), random_string(), random_string(), random_string(), random_int(), random_int());
}
function random_optional_UpdaterDoc() {
    if (yes_no())
        return undefined;
    return random_UpdaterDoc();
}
function random_list_UpdaterDoc(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_UpdaterDoc());
    return list;
}
function random_optional_list_UpdaterDoc() {
    if (yes_no())
        return undefined;
    return random_list_UpdaterDoc();
}
function random_UpdaterDto() {
    return new dto_1.UpdaterDto(random_string(), random_optional_list_int(), random_optional_list_float(), random_optional_float());
}
function random_optional_UpdaterDto() {
    if (yes_no())
        return undefined;
    return random_UpdaterDto();
}
function random_list_UpdaterDto(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_UpdaterDto());
    return list;
}
function random_optional_list_UpdaterDto() {
    if (yes_no())
        return undefined;
    return random_list_UpdaterDto();
}
function random_Updater() {
    return new dto_1.Updater(random_string(), random_list_int(), random_list_float(), random_optional_float(), random_string());
}
function random_optional_Updater() {
    if (yes_no())
        return undefined;
    return random_Updater();
}
function random_list_Updater(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_Updater());
    return list;
}
function random_optional_list_Updater() {
    if (yes_no())
        return undefined;
    return random_list_Updater();
}
function random_IndependentGaussian() {
    return new dto_1.IndependentGaussian(random_list_int(), random_string());
}
function random_optional_IndependentGaussian() {
    if (yes_no())
        return undefined;
    return random_IndependentGaussian();
}
function random_list_IndependentGaussian(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_IndependentGaussian());
    return list;
}
function random_optional_list_IndependentGaussian() {
    if (yes_no())
        return undefined;
    return random_list_IndependentGaussian();
}
function random_CorrelatedGaussian() {
    return new dto_1.CorrelatedGaussian(random_float(), random_int(), random_int(), random_string());
}
function random_optional_CorrelatedGaussian() {
    if (yes_no())
        return undefined;
    return random_CorrelatedGaussian();
}
function random_list_CorrelatedGaussian(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_CorrelatedGaussian());
    return list;
}
function random_optional_list_CorrelatedGaussian() {
    if (yes_no())
        return undefined;
    return random_list_CorrelatedGaussian();
}
function random_BrownianMotion() {
    return new dto_1.BrownianMotion(random_float(), random_float(), random_float(), random_string());
}
function random_optional_BrownianMotion() {
    if (yes_no())
        return undefined;
    return random_BrownianMotion();
}
function random_list_BrownianMotion(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_BrownianMotion());
    return list;
}
function random_optional_list_BrownianMotion() {
    if (yes_no())
        return undefined;
    return random_list_BrownianMotion();
}
function random_BrownianMotionRef() {
    return new dto_1.BrownianMotionRef(random_float(), random_int(), random_int(), random_string());
}
function random_optional_BrownianMotionRef() {
    if (yes_no())
        return undefined;
    return random_BrownianMotionRef();
}
function random_list_BrownianMotionRef(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_BrownianMotionRef());
    return list;
}
function random_optional_list_BrownianMotionRef() {
    if (yes_no())
        return undefined;
    return random_list_BrownianMotionRef();
}
function random_GeometricalBrownianMotion() {
    return new dto_1.GeometricalBrownianMotion(random_float(), random_float(), random_float(), random_string());
}
function random_optional_GeometricalBrownianMotion() {
    if (yes_no())
        return undefined;
    return random_GeometricalBrownianMotion();
}
function random_list_GeometricalBrownianMotion(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_GeometricalBrownianMotion());
    return list;
}
function random_optional_list_GeometricalBrownianMotion() {
    if (yes_no())
        return undefined;
    return random_list_GeometricalBrownianMotion();
}
function random_GeometricalBrownianMotionRef() {
    return new dto_1.GeometricalBrownianMotionRef(random_float(), random_int(), random_int(), random_string());
}
function random_optional_GeometricalBrownianMotionRef() {
    if (yes_no())
        return undefined;
    return random_GeometricalBrownianMotionRef();
}
function random_list_GeometricalBrownianMotionRef(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_GeometricalBrownianMotionRef());
    return list;
}
function random_optional_list_GeometricalBrownianMotionRef() {
    if (yes_no())
        return undefined;
    return random_list_GeometricalBrownianMotionRef();
}
function random_ZeroCouponBond() {
    return new dto_1.ZeroCouponBond(random_int(), random_float(), random_string());
}
function random_optional_ZeroCouponBond() {
    if (yes_no())
        return undefined;
    return random_ZeroCouponBond();
}
function random_list_ZeroCouponBond(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_ZeroCouponBond());
    return list;
}
function random_optional_list_ZeroCouponBond() {
    if (yes_no())
        return undefined;
    return random_list_ZeroCouponBond();
}
function random_Option() {
    return new dto_1.Option(random_int(), random_float(), random_int(), random_string());
}
function random_optional_Option() {
    if (yes_no())
        return undefined;
    return random_Option();
}
function random_list_Option(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_Option());
    return list;
}
function random_optional_list_Option() {
    if (yes_no())
        return undefined;
    return random_list_Option();
}
function random_Barrier() {
    return new dto_1.Barrier(random_int(), random_float(), random_float(), random_int(), random_int(), random_float(), random_string());
}
function random_optional_Barrier() {
    if (yes_no())
        return undefined;
    return random_Barrier();
}
function random_list_Barrier(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_Barrier());
    return list;
}
function random_optional_list_Barrier() {
    if (yes_no())
        return undefined;
    return random_list_Barrier();
}
function random_Multiplication() {
    return new dto_1.Multiplication(random_list_int(), random_float(), random_string());
}
function random_optional_Multiplication() {
    if (yes_no())
        return undefined;
    return random_Multiplication();
}
function random_list_Multiplication(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_Multiplication());
    return list;
}
function random_optional_list_Multiplication() {
    if (yes_no())
        return undefined;
    return random_list_Multiplication();
}
function random_HistogramAxis() {
    return new dto_1.HistogramAxis(random_int(), random_int(), random_float(), random_float());
}
function random_optional_HistogramAxis() {
    if (yes_no())
        return undefined;
    return random_HistogramAxis();
}
function random_list_HistogramAxis(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_HistogramAxis());
    return list;
}
function random_optional_list_HistogramAxis() {
    if (yes_no())
        return undefined;
    return random_list_HistogramAxis();
}
function random_Histogram() {
    return new dto_1.Histogram(random_HistogramAxis(), random_optional_HistogramAxis());
}
function random_optional_Histogram() {
    if (yes_no())
        return undefined;
    return random_Histogram();
}
function random_list_Histogram(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_Histogram());
    return list;
}
function random_optional_list_Histogram() {
    if (yes_no())
        return undefined;
    return random_list_Histogram();
}
function random_EvaluationPoint() {
    return new dto_1.EvaluationPoint(random_int(), random_float(), random_optional_float(), random_optional_float(), random_list_Histogram());
}
function random_optional_EvaluationPoint() {
    if (yes_no())
        return undefined;
    return random_EvaluationPoint();
}
function random_list_EvaluationPoint(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_EvaluationPoint());
    return list;
}
function random_optional_list_EvaluationPoint() {
    if (yes_no())
        return undefined;
    return random_list_EvaluationPoint();
}
function random_Parameter() {
    return new dto_1.Parameter(random_float(), random_float(), random_float(), random_float());
}
function random_optional_Parameter() {
    if (yes_no())
        return undefined;
    return random_Parameter();
}
function random_list_Parameter(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_Parameter());
    return list;
}
function random_optional_list_Parameter() {
    if (yes_no())
        return undefined;
    return random_list_Parameter();
}
function random_Model() {
    return new dto_1.Model(random_float(), random_int(), random_int(), random_list_Updater(), random_list_EvaluationPoint(), random_float(), random_int());
}
function random_optional_Model() {
    if (yes_no())
        return undefined;
    return random_Model();
}
function random_list_Model(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_Model());
    return list;
}
function random_optional_list_Model() {
    if (yes_no())
        return undefined;
    return random_list_Model();
}
function random_Result() {
    return new dto_1.Result(random_int(), random_float(), random_float(), random_float());
}
function random_optional_Result() {
    if (yes_no())
        return undefined;
    return random_Result();
}
function random_list_Result(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_Result());
    return list;
}
function random_optional_list_Result() {
    if (yes_no())
        return undefined;
    return random_list_Result();
}
function random_EvaluationResults() {
    return new dto_1.EvaluationResults(random_list_string(), random_list_int(), random_list_float(), random_list_float(), random_list_float(), random_list_float(), random_list_int(), random_list_Histogram(), random_optional_Model());
}
function random_optional_EvaluationResults() {
    if (yes_no())
        return undefined;
    return random_EvaluationResults();
}
function random_list_EvaluationResults(min, max) {
    if (min === void 0) { min = 0; }
    if (max === void 0) { max = 3; }
    var size = Math.floor(min + Math.random() * (max - min));
    var list = [];
    for (var i = 0; i < size; i++)
        list.push(random_EvaluationResults());
    return list;
}
function random_optional_list_EvaluationResults() {
    if (yes_no())
        return undefined;
    return random_list_EvaluationResults();
}
function create(struct_name, file_name) {
    if (false) {
    }
    else if (struct_name === 'UpdaterDoc') {
        var obj1 = random_UpdaterDoc();
        var j = {};
        dto.UpdaterDoc_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.UpdaterDoc();
        dto.UpdaterDoc_from_json(j, obj2);
        if (!dto.UpdaterDoc_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'UpdaterDto') {
        var obj1 = random_UpdaterDto();
        var j = {};
        dto.UpdaterDto_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.UpdaterDto();
        dto.UpdaterDto_from_json(j, obj2);
        if (!dto.UpdaterDto_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Updater') {
        var obj1 = random_Updater();
        var j = {};
        dto.Updater_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.Updater();
        dto.Updater_from_json(j, obj2);
        if (!dto.Updater_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'IndependentGaussian') {
        var obj1 = random_IndependentGaussian();
        var j = {};
        dto.IndependentGaussian_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.IndependentGaussian();
        dto.IndependentGaussian_from_json(j, obj2);
        if (!dto.IndependentGaussian_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'CorrelatedGaussian') {
        var obj1 = random_CorrelatedGaussian();
        var j = {};
        dto.CorrelatedGaussian_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.CorrelatedGaussian();
        dto.CorrelatedGaussian_from_json(j, obj2);
        if (!dto.CorrelatedGaussian_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'BrownianMotion') {
        var obj1 = random_BrownianMotion();
        var j = {};
        dto.BrownianMotion_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.BrownianMotion();
        dto.BrownianMotion_from_json(j, obj2);
        if (!dto.BrownianMotion_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'BrownianMotionRef') {
        var obj1 = random_BrownianMotionRef();
        var j = {};
        dto.BrownianMotionRef_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.BrownianMotionRef();
        dto.BrownianMotionRef_from_json(j, obj2);
        if (!dto.BrownianMotionRef_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'GeometricalBrownianMotion') {
        var obj1 = random_GeometricalBrownianMotion();
        var j = {};
        dto.GeometricalBrownianMotion_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.GeometricalBrownianMotion();
        dto.GeometricalBrownianMotion_from_json(j, obj2);
        if (!dto.GeometricalBrownianMotion_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'GeometricalBrownianMotionRef') {
        var obj1 = random_GeometricalBrownianMotionRef();
        var j = {};
        dto.GeometricalBrownianMotionRef_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.GeometricalBrownianMotionRef();
        dto.GeometricalBrownianMotionRef_from_json(j, obj2);
        if (!dto.GeometricalBrownianMotionRef_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'ZeroCouponBond') {
        var obj1 = random_ZeroCouponBond();
        var j = {};
        dto.ZeroCouponBond_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.ZeroCouponBond();
        dto.ZeroCouponBond_from_json(j, obj2);
        if (!dto.ZeroCouponBond_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Option') {
        var obj1 = random_Option();
        var j = {};
        dto.Option_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.Option();
        dto.Option_from_json(j, obj2);
        if (!dto.Option_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Barrier') {
        var obj1 = random_Barrier();
        var j = {};
        dto.Barrier_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.Barrier();
        dto.Barrier_from_json(j, obj2);
        if (!dto.Barrier_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Multiplication') {
        var obj1 = random_Multiplication();
        var j = {};
        dto.Multiplication_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.Multiplication();
        dto.Multiplication_from_json(j, obj2);
        if (!dto.Multiplication_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'HistogramAxis') {
        var obj1 = random_HistogramAxis();
        var j = {};
        dto.HistogramAxis_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.HistogramAxis();
        dto.HistogramAxis_from_json(j, obj2);
        if (!dto.HistogramAxis_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Histogram') {
        var obj1 = random_Histogram();
        var j = {};
        dto.Histogram_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.Histogram();
        dto.Histogram_from_json(j, obj2);
        if (!dto.Histogram_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'EvaluationPoint') {
        var obj1 = random_EvaluationPoint();
        var j = {};
        dto.EvaluationPoint_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.EvaluationPoint();
        dto.EvaluationPoint_from_json(j, obj2);
        if (!dto.EvaluationPoint_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Parameter') {
        var obj1 = random_Parameter();
        var j = {};
        dto.Parameter_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.Parameter();
        dto.Parameter_from_json(j, obj2);
        if (!dto.Parameter_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Model') {
        var obj1 = random_Model();
        var j = {};
        dto.Model_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.Model();
        dto.Model_from_json(j, obj2);
        if (!dto.Model_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Result') {
        var obj1 = random_Result();
        var j = {};
        dto.Result_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.Result();
        dto.Result_from_json(j, obj2);
        if (!dto.Result_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'EvaluationResults') {
        var obj1 = random_EvaluationResults();
        var j = {};
        dto.EvaluationResults_to_json(j, obj1);
        fs.writeFileSync(file_name, JSON.stringify(j));
        var obj2 = new dto_1.EvaluationResults();
        dto.EvaluationResults_from_json(j, obj2);
        if (!dto.EvaluationResults_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else
        throw new Error("Cannot create an object of the structure ".concat(struct_name, "."));
}
function convert(struct_name, file1_name, file2_name) {
    if (false) {
    }
    else if (struct_name === 'UpdaterDoc') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.UpdaterDoc_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'UpdaterDto') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.UpdaterDto_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'Updater') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.Updater_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'IndependentGaussian') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.IndependentGaussian_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'CorrelatedGaussian') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.CorrelatedGaussian_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'BrownianMotion') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.BrownianMotion_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'BrownianMotionRef') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.BrownianMotionRef_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'GeometricalBrownianMotion') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.GeometricalBrownianMotion_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'GeometricalBrownianMotionRef') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.GeometricalBrownianMotionRef_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'ZeroCouponBond') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.ZeroCouponBond_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'Option') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.Option_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'Barrier') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.Barrier_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'Multiplication') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.Multiplication_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'HistogramAxis') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.HistogramAxis_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'Histogram') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.Histogram_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'EvaluationPoint') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.EvaluationPoint_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'Parameter') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.Parameter_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'Model') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.Model_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'Result') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.Result_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else if (struct_name === 'EvaluationResults') {
        var jstr = fs.readFileSync(file1_name, 'utf-8');
        var obj = dto.EvaluationResults_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
    }
    else
        throw new Error("Cannot convert an object of the structure ".concat(struct_name, "."));
}
function compare(struct_name, file1_name, file2_name) {
    if (false) {
    }
    else if (struct_name === 'UpdaterDoc') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.UpdaterDoc_fromJSON_string(jstr1);
        var obj2 = dto.UpdaterDoc_fromJSON_string(jstr2);
        if (!dto.UpdaterDoc_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'UpdaterDto') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.UpdaterDto_fromJSON_string(jstr1);
        var obj2 = dto.UpdaterDto_fromJSON_string(jstr2);
        if (!dto.UpdaterDto_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Updater') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.Updater_fromJSON_string(jstr1);
        var obj2 = dto.Updater_fromJSON_string(jstr2);
        if (!dto.Updater_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'IndependentGaussian') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.IndependentGaussian_fromJSON_string(jstr1);
        var obj2 = dto.IndependentGaussian_fromJSON_string(jstr2);
        if (!dto.IndependentGaussian_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'CorrelatedGaussian') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.CorrelatedGaussian_fromJSON_string(jstr1);
        var obj2 = dto.CorrelatedGaussian_fromJSON_string(jstr2);
        if (!dto.CorrelatedGaussian_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'BrownianMotion') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.BrownianMotion_fromJSON_string(jstr1);
        var obj2 = dto.BrownianMotion_fromJSON_string(jstr2);
        if (!dto.BrownianMotion_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'BrownianMotionRef') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.BrownianMotionRef_fromJSON_string(jstr1);
        var obj2 = dto.BrownianMotionRef_fromJSON_string(jstr2);
        if (!dto.BrownianMotionRef_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'GeometricalBrownianMotion') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.GeometricalBrownianMotion_fromJSON_string(jstr1);
        var obj2 = dto.GeometricalBrownianMotion_fromJSON_string(jstr2);
        if (!dto.GeometricalBrownianMotion_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'GeometricalBrownianMotionRef') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.GeometricalBrownianMotionRef_fromJSON_string(jstr1);
        var obj2 = dto.GeometricalBrownianMotionRef_fromJSON_string(jstr2);
        if (!dto.GeometricalBrownianMotionRef_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'ZeroCouponBond') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.ZeroCouponBond_fromJSON_string(jstr1);
        var obj2 = dto.ZeroCouponBond_fromJSON_string(jstr2);
        if (!dto.ZeroCouponBond_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Option') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.Option_fromJSON_string(jstr1);
        var obj2 = dto.Option_fromJSON_string(jstr2);
        if (!dto.Option_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Barrier') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.Barrier_fromJSON_string(jstr1);
        var obj2 = dto.Barrier_fromJSON_string(jstr2);
        if (!dto.Barrier_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Multiplication') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.Multiplication_fromJSON_string(jstr1);
        var obj2 = dto.Multiplication_fromJSON_string(jstr2);
        if (!dto.Multiplication_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'HistogramAxis') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.HistogramAxis_fromJSON_string(jstr1);
        var obj2 = dto.HistogramAxis_fromJSON_string(jstr2);
        if (!dto.HistogramAxis_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Histogram') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.Histogram_fromJSON_string(jstr1);
        var obj2 = dto.Histogram_fromJSON_string(jstr2);
        if (!dto.Histogram_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'EvaluationPoint') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.EvaluationPoint_fromJSON_string(jstr1);
        var obj2 = dto.EvaluationPoint_fromJSON_string(jstr2);
        if (!dto.EvaluationPoint_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Parameter') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.Parameter_fromJSON_string(jstr1);
        var obj2 = dto.Parameter_fromJSON_string(jstr2);
        if (!dto.Parameter_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Model') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.Model_fromJSON_string(jstr1);
        var obj2 = dto.Model_fromJSON_string(jstr2);
        if (!dto.Model_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'Result') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.Result_fromJSON_string(jstr1);
        var obj2 = dto.Result_fromJSON_string(jstr2);
        if (!dto.Result_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else if (struct_name === 'EvaluationResults') {
        var jstr1 = fs.readFileSync(file1_name, 'utf-8');
        var jstr2 = fs.readFileSync(file2_name, 'utf-8');
        var obj1 = dto.EvaluationResults_fromJSON_string(jstr1);
        var obj2 = dto.EvaluationResults_fromJSON_string(jstr2);
        if (!dto.EvaluationResults_equal(obj1, obj2))
            throw new Error("".concat(struct_name, " objects are not equal."));
    }
    else
        throw new Error("Cannot compare an object of the structure ".concat(struct_name, "."));
}
function main() {
    // expect at least 3 args
    if (process.argv.length < 3)
        throw new Error("Expect at least 3 args, found ".concat(process.argv.length));
    var command = process.argv[2];
    if (command == 'create') {
        if (process.argv.length < 5)
            throw new Error("Command \"".concat(command, "\" expects at least 5 args, found ").concat(process.argv.length));
        create(process.argv[3], process.argv[4]);
    }
    else if (command == 'convert') {
        if (process.argv.length < 6)
            throw new Error("Command \"".concat(command, "\" expects at least 6 args, found ").concat(process.argv.length));
        convert(process.argv[3], process.argv[4], process.argv[5]);
    }
    else if (command == 'compare') {
        if (process.argv.length < 6)
            throw new Error("Command \"".concat(command, "\" expects at least 6 args, found ").concat(process.argv.length));
        compare(process.argv[3], process.argv[4], process.argv[5]);
    }
    else
        throw new Error("Unknown command \"".concat(command, "\""));
}
main();
