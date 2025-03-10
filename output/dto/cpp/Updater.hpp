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


#include "UpdaterDto.hpp"
namespace dto {
class Updater;
std::string Updater_to_json_string(const Updater &obj);
class Updater: public UpdaterDto {
public:

    int _state;
    int _nstates;
    std::string title;

    
    Updater (
        std::string name = "",
        std::vector<int> refs = {},
        std::vector<float> args = {},
        std::vector<float> start = {},
        int nstates = 1,
        std::string title = ""
    )
    : UpdaterDto (
        name,
        refs,
        args,
        start
    )
    , _state (
        -88
    )
    , _nstates (
        nstates
    )
    , title (
        title
    )
    {
    }

    int GetStateNumber (
    )
    {
        
        if(_state<0)
            throw std::runtime_error("An updater has no state.");
        return _state;
        
    }

    std::vector<float> GetStart (
    ) const
    {
        
        return start.value_or(std::vector<float>{});
        
    }

    bool operator == (const Updater &other) const {
        if (UpdaterDto::operator != (other)) return false;
        return true;
    }
    bool operator != (const Updater &other) const {return not(*this==other);}
    std::string json (void) const {
        return Updater_to_json_string(*this);
    }
}; // Updater
inline
void to_json(json &j, const Updater &obj) try {
    j = json::object();
    to_json(j,static_cast<const UpdaterDto &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const Updater &obj) exception"));
}

inline
std::string Updater_to_json_string(const Updater &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, Updater &obj) try {
    from_json(j,static_cast<UpdaterDto &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, Updater &obj) exception"));
}
inline
Updater Updater_from_json(const json &j) {
    Updater obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

