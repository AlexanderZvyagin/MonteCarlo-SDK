
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
    sources: ['/Users/zvyagin/Projects/az/mcsdk/output/test/mcsdk_test.cpp'],
    include_directories : ['/Users/zvyagin/Projects/az/mcsdk/output/dto'],
    link_with    : [],
    dependencies : []
)
