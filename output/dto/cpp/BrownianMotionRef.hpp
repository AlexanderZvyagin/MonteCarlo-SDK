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
class BrownianMotionRef;
std::string BrownianMotionRef_to_json_string(const BrownianMotionRef &obj);
class BrownianMotionRef: public Updater {
public:


    
    BrownianMotionRef (
        float start = NAN,
        int drift = -88,
        int diffusion = -88,
        std::string title = ""
    )
    : Updater (
        "BrownianMotion",
        {drift,diffusion},
        {},
        {start},
        1,
        title
    )
    {
    }

    bool operator == (const BrownianMotionRef &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const BrownianMotionRef &other) const {return not(*this==other);}
    std::string json (void) const {
        return BrownianMotionRef_to_json_string(*this);
    }
}; // BrownianMotionRef
inline
void to_json(json &j, const BrownianMotionRef &obj) try {
    j = json::object();
    to_json(j,static_cast<const Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const BrownianMotionRef &obj) exception"));
}

inline
std::string BrownianMotionRef_to_json_string(const BrownianMotionRef &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, BrownianMotionRef &obj) try {
    from_json(j,static_cast<Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, BrownianMotionRef &obj) exception"));
}
inline
BrownianMotionRef BrownianMotionRef_from_json(const json &j) {
    BrownianMotionRef obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

