#include <random>
#include <filesystem>
#include <iostream>
#include <fstream>
#include <stdexcept>

#include "dto.cpp"

namespace fs = std::filesystem;

std::random_device rd;
std::mt19937 generator(rd());

int random_int (int min = -1000, int max = 1000) {
    std::uniform_int_distribution<int> uniform_dist(min,max);
    return uniform_dist (generator);
}

// https://stackoverflow.com/questions/47977829/generate-a-random-string-in-c11
std::string random_string (int len=16) {
    static std::string str("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
    std::shuffle(str.begin(), str.end(), generator);
    return str.substr(0, len);
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

        if(struct_name=="UpdaterDoc"){
            f << to_json(UpdaterDoc(
                random_string(),
                random_string(),
                random_string(),
                random_string(),
                random_int(),
                random_int()
            ));
            if(!f)
                throw std::runtime_error("Operation 'create': IO error");
        } else {
            throw std::runtime_error("Not supported operation 'create' on struct " + struct_name);
        }

    } else if (command == "convert") {

        if(struct_name=="UpdaterDoc"){
            auto obj =
                UpdaterDoc_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << to_json(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error");
        } else {
            throw std::runtime_error("Not supported operation 'convert' on struct " + struct_name);
        }

    } else if (command == "compare") {

        if(struct_name=="UpdaterDoc"){
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
                throw std::runtime_error("Operation 'compare failed");
        } else {
            throw std::runtime_error("Not supported operation 'compare' on struct " + struct_name);
        }

    } else {
        throw std::runtime_error("Not supported command " + command);
    }

    return 0;

} catch (const std::exception &e) {
    std::cerr << "Exception:\n" << e.what() << "\n";
    return 1;
}

catch (...) {
    std::cerr << "Unknown exception:\n";
    return 1;
}
