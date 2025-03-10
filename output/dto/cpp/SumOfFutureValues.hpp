#pragma once
// 
// https://github.com/AlexanderZvyagin/dto-code-generator
// Generated by CODE GENERATOR OF DATA TRANSFER OBJECTS (cgdto) version 0.8.2
// 
// Generated from schema: MonteCarlo SDK version (0.8.1)
// 


#include <optional>
#include <string>
#include <vector>
#include <map>
#include <stdexcept>
#include <cmath>

#include <nlohmann/json.hpp>
using json = nlohmann::json;


#include "Updater.hpp"
namespace dto {
class SumOfFutureValues;
std::string SumOfFutureValues_to_json_string(const SumOfFutureValues &obj);
class SumOfFutureValues: public Updater {
public:


    
    SumOfFutureValues (
        int state = -88,
        std::vector<float> t = {},
        std::string title = ""
    )
    : Updater (
        "SumOfFutureValues",
        {state},
        t,
        {},
        1,
        title
    )
    {
    }

    bool operator == (const SumOfFutureValues &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const SumOfFutureValues &other) const {return not(*this==other);}
    std::string json (void) const {
        return SumOfFutureValues_to_json_string(*this);
    }
}; // SumOfFutureValues
inline
void to_json(json &j, const SumOfFutureValues &obj) try {
    j = json::object();
    to_json(j,static_cast<const Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const SumOfFutureValues &obj) exception"));
}

inline
std::string SumOfFutureValues_to_json_string(const SumOfFutureValues &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, SumOfFutureValues &obj) try {
    from_json(j,static_cast<Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, SumOfFutureValues &obj) exception"));
}
inline
SumOfFutureValues SumOfFutureValues_from_json(const json &j) {
    SumOfFutureValues obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

