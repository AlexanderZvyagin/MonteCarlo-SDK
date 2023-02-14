project (
        'cpp',
        ['cpp'],
        default_options : [
                'cpp_std=c++20',
                'buildtype=release',
        ]
)

add_global_arguments('-Wno-c++11-narrowing', language : 'cpp')

executable (
    'run-cpp',
    sources: [
        '../../output/dto-tests.cpp',
    ],
    include_directories : ['../../output'],
    link_with    : [],
    dependencies : []
)
