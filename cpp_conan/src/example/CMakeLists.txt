find_package(Boost COMPONENTS program_options REQUIRED)
add_library("ExampleIo" SHARED
            "io.cpp"
)

add_executable(example "example.cpp")
target_link_libraries(example ExampleIo Boost::program_options)
