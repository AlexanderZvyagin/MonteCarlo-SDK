
#include <random>
#include <limits>
#include <filesystem>
#include <iostream>
#include <fstream>
#include <stdexcept>

#include "mcsdk.cpp"

namespace fs = std::filesystem;

std::random_device rd;
std::mt19937 generator(rd());

int random_int (
    int min = -1000,
    int max = 1000
) {
    std::uniform_int_distribution<int> uniform_dist(min,max);
    return uniform_dist (generator);
}

auto yes_no = [] (void) -> bool {return random_int(0,1);};

std::optional<int> random_optional_int (
    int min = -1000,
    int max = 1000
) {
    if(yes_no())
        return random_int(min,max);
    else
        return {};
}

std::vector<int> random_list_int (
    int len_min = 0,
    int len_max = 3,
    int int_min = -1000,
    int int_max = 1000
) {
    const auto size = random_int (len_min, len_max);
    std::vector<int> list;
    for(int i=0; i<size; i++)
        list.push_back(random_int(int_min,int_max));
    return list;
}

std::optional<std::vector<int>> random_optional_list_int (
    int len_min = 0,
    int len_max = 3,
    int int_min = -1000,
    int int_max = 1000
) {
    if(yes_no())
        return random_list_int(len_min,len_max,int_min,int_max);
    else
        return {};
}

float random_float (
    float min            = -1e6,
    float max            =  1e6,
    bool can_be_nan      = false,
    bool can_be_infinity = false
) {
    // FIXME
    return (float) random_int(min,max);
#if 0
    if(can_be_nan and yes_no())
        return NAN;

    if(can_be_infinity and yes_no())
        return (yes_no() ? -1 : 1) * std::numeric_limits<float>::infinity();

    std::uniform_real_distribution uniform_dist(min,max);
    return uniform_dist (generator);
#endif
}

std::optional<float> random_optional_float (
    float min            = -1e6,
    float max            =  1e6,
    bool can_be_nan      = false,
    bool can_be_infinity = false
) {
    if(yes_no())
        return random_float(min,max,can_be_nan,can_be_infinity);
    else
        return {};
}

std::vector<float> random_list_float (
    int   len_min         = 0,
    int   len_max         = 3,
    float min             = -1e6,
    float max             =  1e6,
    bool  can_be_nan      = false,
    bool  can_be_infinity = false
) {
    const auto size = random_int (len_min, len_max);
    std::vector<float> list;
    for(int i=0; i<size; i++)
        list.push_back(random_float(min,max,can_be_nan,can_be_infinity));
    return list;
}

std::optional<std::vector<float>> random_optional_list_float (
    int   len_min         = 0,
    int   len_max         = 3,
    float min             = -1e6,
    float max             =  1e6,
    bool  can_be_nan      = false,
    bool  can_be_infinity = false
) {
    if(yes_no())
        return random_list_float(len_min,len_max,min,max,can_be_nan,can_be_infinity);
    else
        return {};
}

// https://stackoverflow.com/questions/47977829/generate-a-random-string-in-c11
std::string random_string (int len=16) {
    static std::string str("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
    std::shuffle(str.begin(), str.end(), generator);
    return str.substr(0, len);
}

std::optional<std::string> random_optional_string (int len=16) {
    if(yes_no())
        return random_string(len);
    else
        return {};
}

std::vector<std::string> random_list_string (
    int len_min = 0,
    int len_max = 3,
    int strlen_max = 16
) {
    const auto size = random_int (len_min, len_max);
    std::vector<std::string> list;
    for(int i=0; i<size; i++)
        list.push_back(random_string(strlen_max));
    return list;
}

std::optional<std::vector<std::string>> random_optional_list_string (
    int len_min = 0,
    int len_max = 3,
    int strlen_max = 16
) {
    if(yes_no())
        return random_list_string(len_min,len_max,strlen_max);
    else
        return {};
}


UpdaterDoc random_UpdaterDoc (void) {
    return UpdaterDoc (
        random_string(),
        random_string(),
        random_string(),
        random_string(),
        random_int(),
        random_int()

    );
}


std::optional<UpdaterDoc> random_optional_UpdaterDoc (void) {
    if(yes_no())
        return {};
    return random_UpdaterDoc ();
}


std::vector<UpdaterDoc> random_list_UpdaterDoc (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<UpdaterDoc> list;
    for(int i=0; i<size; i++)
        list.push_back(random_UpdaterDoc());
    return list;
}


std::vector<UpdaterDoc> random_optional_list_UpdaterDoc (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_UpdaterDoc (min,max);
}


UpdaterDto random_UpdaterDto (void) {
    return UpdaterDto (
        random_string(),
        random_optional_list_int(),
        random_optional_list_float(),
        random_optional_float()

    );
}


std::optional<UpdaterDto> random_optional_UpdaterDto (void) {
    if(yes_no())
        return {};
    return random_UpdaterDto ();
}


std::vector<UpdaterDto> random_list_UpdaterDto (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<UpdaterDto> list;
    for(int i=0; i<size; i++)
        list.push_back(random_UpdaterDto());
    return list;
}


std::vector<UpdaterDto> random_optional_list_UpdaterDto (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_UpdaterDto (min,max);
}


Updater random_Updater (void) {
    return Updater (
        random_string(),
        random_list_int(),
        random_list_float(),
        random_optional_float(),
        random_string()

    );
}


std::optional<Updater> random_optional_Updater (void) {
    if(yes_no())
        return {};
    return random_Updater ();
}


std::vector<Updater> random_list_Updater (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<Updater> list;
    for(int i=0; i<size; i++)
        list.push_back(random_Updater());
    return list;
}


std::vector<Updater> random_optional_list_Updater (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_Updater (min,max);
}


IndependentGaussian random_IndependentGaussian (void) {
    return IndependentGaussian (
        random_list_int(),
        random_string()

    );
}


std::optional<IndependentGaussian> random_optional_IndependentGaussian (void) {
    if(yes_no())
        return {};
    return random_IndependentGaussian ();
}


std::vector<IndependentGaussian> random_list_IndependentGaussian (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<IndependentGaussian> list;
    for(int i=0; i<size; i++)
        list.push_back(random_IndependentGaussian());
    return list;
}


std::vector<IndependentGaussian> random_optional_list_IndependentGaussian (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_IndependentGaussian (min,max);
}


CorrelatedGaussian random_CorrelatedGaussian (void) {
    return CorrelatedGaussian (
        random_float(),
        random_int(),
        random_int(),
        random_string()

    );
}


std::optional<CorrelatedGaussian> random_optional_CorrelatedGaussian (void) {
    if(yes_no())
        return {};
    return random_CorrelatedGaussian ();
}


std::vector<CorrelatedGaussian> random_list_CorrelatedGaussian (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<CorrelatedGaussian> list;
    for(int i=0; i<size; i++)
        list.push_back(random_CorrelatedGaussian());
    return list;
}


std::vector<CorrelatedGaussian> random_optional_list_CorrelatedGaussian (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_CorrelatedGaussian (min,max);
}


BrownianMotion random_BrownianMotion (void) {
    return BrownianMotion (
        random_float(),
        random_float(),
        random_float(),
        random_string()

    );
}


std::optional<BrownianMotion> random_optional_BrownianMotion (void) {
    if(yes_no())
        return {};
    return random_BrownianMotion ();
}


std::vector<BrownianMotion> random_list_BrownianMotion (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<BrownianMotion> list;
    for(int i=0; i<size; i++)
        list.push_back(random_BrownianMotion());
    return list;
}


std::vector<BrownianMotion> random_optional_list_BrownianMotion (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_BrownianMotion (min,max);
}


BrownianMotionRef random_BrownianMotionRef (void) {
    return BrownianMotionRef (
        random_float(),
        random_int(),
        random_int(),
        random_string()

    );
}


std::optional<BrownianMotionRef> random_optional_BrownianMotionRef (void) {
    if(yes_no())
        return {};
    return random_BrownianMotionRef ();
}


std::vector<BrownianMotionRef> random_list_BrownianMotionRef (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<BrownianMotionRef> list;
    for(int i=0; i<size; i++)
        list.push_back(random_BrownianMotionRef());
    return list;
}


std::vector<BrownianMotionRef> random_optional_list_BrownianMotionRef (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_BrownianMotionRef (min,max);
}


GeometricalBrownianMotion random_GeometricalBrownianMotion (void) {
    return GeometricalBrownianMotion (
        random_float(),
        random_float(),
        random_float(),
        random_string()

    );
}


std::optional<GeometricalBrownianMotion> random_optional_GeometricalBrownianMotion (void) {
    if(yes_no())
        return {};
    return random_GeometricalBrownianMotion ();
}


std::vector<GeometricalBrownianMotion> random_list_GeometricalBrownianMotion (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<GeometricalBrownianMotion> list;
    for(int i=0; i<size; i++)
        list.push_back(random_GeometricalBrownianMotion());
    return list;
}


std::vector<GeometricalBrownianMotion> random_optional_list_GeometricalBrownianMotion (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_GeometricalBrownianMotion (min,max);
}


GeometricalBrownianMotionRef random_GeometricalBrownianMotionRef (void) {
    return GeometricalBrownianMotionRef (
        random_float(),
        random_int(),
        random_int(),
        random_string()

    );
}


std::optional<GeometricalBrownianMotionRef> random_optional_GeometricalBrownianMotionRef (void) {
    if(yes_no())
        return {};
    return random_GeometricalBrownianMotionRef ();
}


std::vector<GeometricalBrownianMotionRef> random_list_GeometricalBrownianMotionRef (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<GeometricalBrownianMotionRef> list;
    for(int i=0; i<size; i++)
        list.push_back(random_GeometricalBrownianMotionRef());
    return list;
}


std::vector<GeometricalBrownianMotionRef> random_optional_list_GeometricalBrownianMotionRef (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_GeometricalBrownianMotionRef (min,max);
}


ZeroCouponBond random_ZeroCouponBond (void) {
    return ZeroCouponBond (
        random_int(),
        random_float(),
        random_string()

    );
}


std::optional<ZeroCouponBond> random_optional_ZeroCouponBond (void) {
    if(yes_no())
        return {};
    return random_ZeroCouponBond ();
}


std::vector<ZeroCouponBond> random_list_ZeroCouponBond (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<ZeroCouponBond> list;
    for(int i=0; i<size; i++)
        list.push_back(random_ZeroCouponBond());
    return list;
}


std::vector<ZeroCouponBond> random_optional_list_ZeroCouponBond (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_ZeroCouponBond (min,max);
}


Option random_Option (void) {
    return Option (
        random_int(),
        random_float(),
        random_int(),
        random_string()

    );
}


std::optional<Option> random_optional_Option (void) {
    if(yes_no())
        return {};
    return random_Option ();
}


std::vector<Option> random_list_Option (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<Option> list;
    for(int i=0; i<size; i++)
        list.push_back(random_Option());
    return list;
}


std::vector<Option> random_optional_list_Option (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_Option (min,max);
}


Barrier random_Barrier (void) {
    return Barrier (
        random_int(),
        random_float(),
        random_float(),
        random_int(),
        random_int(),
        random_float(),
        random_string()

    );
}


std::optional<Barrier> random_optional_Barrier (void) {
    if(yes_no())
        return {};
    return random_Barrier ();
}


std::vector<Barrier> random_list_Barrier (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<Barrier> list;
    for(int i=0; i<size; i++)
        list.push_back(random_Barrier());
    return list;
}


std::vector<Barrier> random_optional_list_Barrier (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_Barrier (min,max);
}


Multiplication random_Multiplication (void) {
    return Multiplication (
        random_list_int(),
        random_float(),
        random_string()

    );
}


std::optional<Multiplication> random_optional_Multiplication (void) {
    if(yes_no())
        return {};
    return random_Multiplication ();
}


std::vector<Multiplication> random_list_Multiplication (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<Multiplication> list;
    for(int i=0; i<size; i++)
        list.push_back(random_Multiplication());
    return list;
}


std::vector<Multiplication> random_optional_list_Multiplication (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_Multiplication (min,max);
}


HistogramAxis random_HistogramAxis (void) {
    return HistogramAxis (
        random_int(),
        random_int(),
        random_float(),
        random_float()

    );
}


std::optional<HistogramAxis> random_optional_HistogramAxis (void) {
    if(yes_no())
        return {};
    return random_HistogramAxis ();
}


std::vector<HistogramAxis> random_list_HistogramAxis (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<HistogramAxis> list;
    for(int i=0; i<size; i++)
        list.push_back(random_HistogramAxis());
    return list;
}


std::vector<HistogramAxis> random_optional_list_HistogramAxis (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_HistogramAxis (min,max);
}


Histogram random_Histogram (void) {
    return Histogram (
        random_HistogramAxis(),
        random_optional_HistogramAxis()

    );
}


std::optional<Histogram> random_optional_Histogram (void) {
    if(yes_no())
        return {};
    return random_Histogram ();
}


std::vector<Histogram> random_list_Histogram (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<Histogram> list;
    for(int i=0; i<size; i++)
        list.push_back(random_Histogram());
    return list;
}


std::vector<Histogram> random_optional_list_Histogram (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_Histogram (min,max);
}


EvaluationPoint random_EvaluationPoint (void) {
    return EvaluationPoint (
        random_int(),
        random_float(),
        random_optional_float(),
        random_optional_float(),
        random_list_Histogram()

    );
}


std::optional<EvaluationPoint> random_optional_EvaluationPoint (void) {
    if(yes_no())
        return {};
    return random_EvaluationPoint ();
}


std::vector<EvaluationPoint> random_list_EvaluationPoint (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<EvaluationPoint> list;
    for(int i=0; i<size; i++)
        list.push_back(random_EvaluationPoint());
    return list;
}


std::vector<EvaluationPoint> random_optional_list_EvaluationPoint (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_EvaluationPoint (min,max);
}


Parameter random_Parameter (void) {
    return Parameter (
        random_float(),
        random_float(),
        random_float(),
        random_float()

    );
}


std::optional<Parameter> random_optional_Parameter (void) {
    if(yes_no())
        return {};
    return random_Parameter ();
}


std::vector<Parameter> random_list_Parameter (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<Parameter> list;
    for(int i=0; i<size; i++)
        list.push_back(random_Parameter());
    return list;
}


std::vector<Parameter> random_optional_list_Parameter (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_Parameter (min,max);
}


Model random_Model (void) {
    return Model (
        random_float(),
        random_int(),
        random_int(),
        random_list_Updater(),
        random_list_EvaluationPoint(),
        random_int(),
        random_float(),
        random_int()

    );
}


std::optional<Model> random_optional_Model (void) {
    if(yes_no())
        return {};
    return random_Model ();
}


std::vector<Model> random_list_Model (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<Model> list;
    for(int i=0; i<size; i++)
        list.push_back(random_Model());
    return list;
}


std::vector<Model> random_optional_list_Model (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_Model (min,max);
}


Result random_Result (void) {
    return Result (
        random_int(),
        random_float(),
        random_float(),
        random_float()

    );
}


std::optional<Result> random_optional_Result (void) {
    if(yes_no())
        return {};
    return random_Result ();
}


std::vector<Result> random_list_Result (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<Result> list;
    for(int i=0; i<size; i++)
        list.push_back(random_Result());
    return list;
}


std::vector<Result> random_optional_list_Result (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_Result (min,max);
}


EvaluationResults random_EvaluationResults (void) {
    return EvaluationResults (
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


std::optional<EvaluationResults> random_optional_EvaluationResults (void) {
    if(yes_no())
        return {};
    return random_EvaluationResults ();
}


std::vector<EvaluationResults> random_list_EvaluationResults (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<EvaluationResults> list;
    for(int i=0; i<size; i++)
        list.push_back(random_EvaluationResults());
    return list;
}


std::vector<EvaluationResults> random_optional_list_EvaluationResults (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    return random_list_EvaluationResults (min,max);
}


int main (int argc, const char **argv) try {

    const std::string
        command         = argc>1 ? argv[1] : "",
        struct_name     = argc>2 ? argv[2] : "",
        file1_path      = argc>3 ? argv[3] : "",
        file2_path      = argc>4 ? argv[4] : "";

    if (command == "create") {

        if(!file2_path.empty())
            throw std::runtime_error("Command 'create' expects empty file2 name, got:'" + file2_path + '"');

        std::ofstream f (file1_path);

        if (false) {

        } else if (struct_name == "UpdaterDoc") {
            auto obj1 = random_UpdaterDoc();
            std::ofstream(file1_path) << UpdaterDoc_to_json_string(obj1);
            auto obj2 =
                UpdaterDoc_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "UpdaterDto") {
            auto obj1 = random_UpdaterDto();
            std::ofstream(file1_path) << UpdaterDto_to_json_string(obj1);
            auto obj2 =
                UpdaterDto_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Updater") {
            auto obj1 = random_Updater();
            std::ofstream(file1_path) << Updater_to_json_string(obj1);
            auto obj2 =
                Updater_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "IndependentGaussian") {
            auto obj1 = random_IndependentGaussian();
            std::ofstream(file1_path) << IndependentGaussian_to_json_string(obj1);
            auto obj2 =
                IndependentGaussian_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "CorrelatedGaussian") {
            auto obj1 = random_CorrelatedGaussian();
            std::ofstream(file1_path) << CorrelatedGaussian_to_json_string(obj1);
            auto obj2 =
                CorrelatedGaussian_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "BrownianMotion") {
            auto obj1 = random_BrownianMotion();
            std::ofstream(file1_path) << BrownianMotion_to_json_string(obj1);
            auto obj2 =
                BrownianMotion_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "BrownianMotionRef") {
            auto obj1 = random_BrownianMotionRef();
            std::ofstream(file1_path) << BrownianMotionRef_to_json_string(obj1);
            auto obj2 =
                BrownianMotionRef_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "GeometricalBrownianMotion") {
            auto obj1 = random_GeometricalBrownianMotion();
            std::ofstream(file1_path) << GeometricalBrownianMotion_to_json_string(obj1);
            auto obj2 =
                GeometricalBrownianMotion_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "GeometricalBrownianMotionRef") {
            auto obj1 = random_GeometricalBrownianMotionRef();
            std::ofstream(file1_path) << GeometricalBrownianMotionRef_to_json_string(obj1);
            auto obj2 =
                GeometricalBrownianMotionRef_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "ZeroCouponBond") {
            auto obj1 = random_ZeroCouponBond();
            std::ofstream(file1_path) << ZeroCouponBond_to_json_string(obj1);
            auto obj2 =
                ZeroCouponBond_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Option") {
            auto obj1 = random_Option();
            std::ofstream(file1_path) << Option_to_json_string(obj1);
            auto obj2 =
                Option_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Barrier") {
            auto obj1 = random_Barrier();
            std::ofstream(file1_path) << Barrier_to_json_string(obj1);
            auto obj2 =
                Barrier_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Multiplication") {
            auto obj1 = random_Multiplication();
            std::ofstream(file1_path) << Multiplication_to_json_string(obj1);
            auto obj2 =
                Multiplication_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "HistogramAxis") {
            auto obj1 = random_HistogramAxis();
            std::ofstream(file1_path) << HistogramAxis_to_json_string(obj1);
            auto obj2 =
                HistogramAxis_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Histogram") {
            auto obj1 = random_Histogram();
            std::ofstream(file1_path) << Histogram_to_json_string(obj1);
            auto obj2 =
                Histogram_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "EvaluationPoint") {
            auto obj1 = random_EvaluationPoint();
            std::ofstream(file1_path) << EvaluationPoint_to_json_string(obj1);
            auto obj2 =
                EvaluationPoint_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Parameter") {
            auto obj1 = random_Parameter();
            std::ofstream(file1_path) << Parameter_to_json_string(obj1);
            auto obj2 =
                Parameter_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Model") {
            auto obj1 = random_Model();
            std::ofstream(file1_path) << Model_to_json_string(obj1);
            auto obj2 =
                Model_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Result") {
            auto obj1 = random_Result();
            std::ofstream(file1_path) << Result_to_json_string(obj1);
            auto obj2 =
                Result_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "EvaluationResults") {
            auto obj1 = random_EvaluationResults();
            std::ofstream(file1_path) << EvaluationResults_to_json_string(obj1);
            auto obj2 =
                EvaluationResults_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);

        } else {
            throw std::runtime_error("Not supported operation 'create' on struct " + struct_name);
        }
        if(!f)
            throw std::runtime_error("Operation 'create': IO error");

    } else if (command == "convert") {

        if (false) {

        } else if (struct_name == "UpdaterDoc") {
            auto obj =
                UpdaterDoc_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << UpdaterDoc_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "UpdaterDto") {
            auto obj =
                UpdaterDto_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << UpdaterDto_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "Updater") {
            auto obj =
                Updater_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << Updater_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "IndependentGaussian") {
            auto obj =
                IndependentGaussian_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << IndependentGaussian_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "CorrelatedGaussian") {
            auto obj =
                CorrelatedGaussian_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << CorrelatedGaussian_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "BrownianMotion") {
            auto obj =
                BrownianMotion_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << BrownianMotion_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "BrownianMotionRef") {
            auto obj =
                BrownianMotionRef_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << BrownianMotionRef_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "GeometricalBrownianMotion") {
            auto obj =
                GeometricalBrownianMotion_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << GeometricalBrownianMotion_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "GeometricalBrownianMotionRef") {
            auto obj =
                GeometricalBrownianMotionRef_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << GeometricalBrownianMotionRef_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "ZeroCouponBond") {
            auto obj =
                ZeroCouponBond_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << ZeroCouponBond_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "Option") {
            auto obj =
                Option_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << Option_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "Barrier") {
            auto obj =
                Barrier_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << Barrier_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "Multiplication") {
            auto obj =
                Multiplication_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << Multiplication_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "HistogramAxis") {
            auto obj =
                HistogramAxis_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << HistogramAxis_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "Histogram") {
            auto obj =
                Histogram_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << Histogram_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "EvaluationPoint") {
            auto obj =
                EvaluationPoint_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << EvaluationPoint_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "Parameter") {
            auto obj =
                Parameter_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << Parameter_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "Model") {
            auto obj =
                Model_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << Model_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "Result") {
            auto obj =
                Result_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << Result_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "EvaluationResults") {
            auto obj =
                EvaluationResults_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << EvaluationResults_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);

        } else {
            throw std::runtime_error("Not supported operation 'convert' on struct " + struct_name);
        }

    } else if (command == "compare") {

        if (false) {

        } else if (struct_name == "UpdaterDoc") {
            auto obj1 =
                UpdaterDoc_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                UpdaterDoc_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "UpdaterDto") {
            auto obj1 =
                UpdaterDto_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                UpdaterDto_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Updater") {
            auto obj1 =
                Updater_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                Updater_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "IndependentGaussian") {
            auto obj1 =
                IndependentGaussian_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                IndependentGaussian_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "CorrelatedGaussian") {
            auto obj1 =
                CorrelatedGaussian_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                CorrelatedGaussian_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "BrownianMotion") {
            auto obj1 =
                BrownianMotion_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                BrownianMotion_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "BrownianMotionRef") {
            auto obj1 =
                BrownianMotionRef_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                BrownianMotionRef_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "GeometricalBrownianMotion") {
            auto obj1 =
                GeometricalBrownianMotion_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                GeometricalBrownianMotion_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "GeometricalBrownianMotionRef") {
            auto obj1 =
                GeometricalBrownianMotionRef_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                GeometricalBrownianMotionRef_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "ZeroCouponBond") {
            auto obj1 =
                ZeroCouponBond_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                ZeroCouponBond_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Option") {
            auto obj1 =
                Option_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                Option_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Barrier") {
            auto obj1 =
                Barrier_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                Barrier_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Multiplication") {
            auto obj1 =
                Multiplication_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                Multiplication_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "HistogramAxis") {
            auto obj1 =
                HistogramAxis_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                HistogramAxis_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Histogram") {
            auto obj1 =
                Histogram_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                Histogram_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "EvaluationPoint") {
            auto obj1 =
                EvaluationPoint_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                EvaluationPoint_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Parameter") {
            auto obj1 =
                Parameter_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                Parameter_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Model") {
            auto obj1 =
                Model_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                Model_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "Result") {
            auto obj1 =
                Result_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                Result_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "EvaluationResults") {
            auto obj1 =
                EvaluationResults_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                EvaluationResults_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);

        } else {
            throw std::runtime_error("Not supported operation 'compare' on struct " + struct_name);
        }

    } else {
        throw std::runtime_error("Not supported command " + command);
    }

    return 0;

} catch (const std::exception &e) {
    std::cerr << "Exception:" << std::endl << e.what() << std::endl;
    return 1;
}

catch (...) {
    std::cerr << "Unknown exception:" << std::endl;
    return 1;
}

