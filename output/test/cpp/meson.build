
project (
        'cpp',
        ['cpp'],
        default_options : [
                'cpp_std=c++20',
                'buildtype=release',
        ]
)

add_global_arguments('-Wno-narrowing', language : 'cpp')

executable (
    'test-cpp',
    sources: ['/home/zvyagin/Projects/MonteCarlo/f/mcsdk/output/test/mcsdk_test.cpp'],
    include_directories : ['/home/zvyagin/Projects/MonteCarlo/f/mcsdk/output/dto'],
    link_with    : [],
    dependencies : []
)
