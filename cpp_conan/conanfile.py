from conan import ConanFile


required_conan_version = ">=2.0.0"


class ExampleConan(ConanFile):
    name = "example"
    version = "0.1.0-snapshot"
    settings = "os", "arch", "compiler", "build_type"

    #requires = "boost/1.83.0"
    tool_requires = "doxygen/1.9.4"
    #test_requires = "boost/1.83.0"

    generators = "CMakeDeps", "CMakeToolchain"