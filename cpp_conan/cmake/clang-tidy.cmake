option(SKIP_LINTING_CLANG_TIDY "Enable/disable linting with clang-tidy." ON)

if(${SKIP_LINTING_CLANG_TIDY})
    message(STATUS "Skip linting: clang-tidy")
    return()
endif()

find_program(CLANG_TIDY_EXEC NAMES clang-tidy clang-tidy-17 REQUIRED)

message(STATUS "Found clang-tidy: ${CLANG_TIDY_EXEC}")

set(CMAKE_C_CLANG_TIDY ${CLANG_TIDY_EXEC})
set(CMAKE_CXX_CLANG_TIDY ${CLANG_TIDY_EXEC})