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
class Division;
std::string Division_to_json_string(const Division &obj);
class Division: public Updater {
public:


    
    Division (
        int numerator = -88,
        int denominator = -88,
        float eps = 0,
        std::string title = ""
    )
    : Updater (
        "Division",
        {numerator,denominator},
        {eps},
        {},
        1,
        title
    )
    {
    }

    bool operator == (const Division &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const Division &other) const {return not(*this==other);}
    std::string json (void) const {
        return Division_to_json_string(*this);
    }
}; // Division
inline
void to_json(json &j, const Division &obj) try {
    j = json::object();
    to_json(j,static_cast<const Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const Division &obj) exception"));
}

inline
std::string Division_to_json_string(const Division &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, Division &obj) try {
    from_json(j,static_cast<Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, Division &obj) exception"));
}
inline
Division Division_from_json(const json &j) {
    Division obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

