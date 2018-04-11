# Build example_io library
list(APPEND example_io_sources 
    "io.cpp"
)

add_library("ExampleIo" SHARED
            ${example_io_sources}
)

# Build example executable
list(APPEND example_sources 
    "example.cpp"
    "io.cpp"
)

add_executable(example ${example_sources})
