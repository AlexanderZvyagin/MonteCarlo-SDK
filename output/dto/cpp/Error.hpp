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


namespace dto {
class Error;
std::string Error_to_json_string(const Error &obj);
class Error {
public:

    std::optional<std::string> message;
    std::optional<std::string> details;
    std::optional<int> code;
    std::optional<std::vector<Error>> errors;

    
    Error (
        std::optional<std::string> message = {},
        std::optional<std::string> details = {},
        std::optional<int> code = {},
        std::optional<std::vector<Error>> errors = {}
    )
    : message (
        message
    )
    , details (
        details
    )
    , code (
        code
    )
    , errors (
        errors
    )
    {
    }

    bool operator == (const Error &other) const {
        if (message != other.message) return false;
        if (details != other.details) return false;
        if (code != other.code) return false;
        if (errors != other.errors) return false;
        return true;
    }
    bool operator != (const Error &other) const {return not(*this==other);}
    std::string json (void) const {
        return Error_to_json_string(*this);
    }
}; // Error
inline
void to_json(json &j, const Error &obj) try {
    j = json::object();
    if(obj.message.has_value())
        j["message"] = obj.message.value();
    if(obj.details.has_value())
        j["details"] = obj.details.value();
    if(obj.code.has_value())
        j["code"] = obj.code.value();
    if(obj.errors.has_value())
        j["errors"] = obj.errors.value();
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const Error &obj) exception"));
}

inline
std::string Error_to_json_string(const Error &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, Error &obj) try {
    if(auto it=j.find("message"); it!=j.end() and !it->is_null())
        obj.message = *it;
    if(auto it=j.find("details"); it!=j.end() and !it->is_null())
        obj.details = *it;
    if(auto it=j.find("code"); it!=j.end() and !it->is_null())
        obj.code = *it;
    if(auto it=j.find("errors"); it!=j.end() and !it->is_null())
        obj.errors = *it;
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, Error &obj) exception"));
}
inline
Error Error_from_json(const json &j) {
    Error obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

