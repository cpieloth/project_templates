option(SKIP_LINTING_CPPCHECK "Enable/disable linting with cppcheck." ON)

if(${SKIP_LINTING_CPPCHECK})
    message(STATUS "Skip linting: cppcheck")
    return()
endif()

find_program(CPPCHECK_EXEC NAMES cppcheck REQUIRED)

message(STATUS "Found cppcheck: ${CPPCHECK_EXEC}")

set(CMAKE_C_CPPCHECK ${CPPCHECK_EXEC};--std=c11;--check-level=exhaustive;-I ${PROJECT_SOURCE_DIR}/src)
set(CMAKE_CXX_CPPCHECK ${CPPCHECK_EXEC};--std=c++17;--check-level=exhaustive;-I ${PROJECT_SOURCE_DIR}/src)