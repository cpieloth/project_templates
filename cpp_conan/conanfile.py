from conan import ConanFile


required_conan_version = ">=2.0.0"


class ExampleConan(ConanFile):
    name = "example"
    version = "0.1.0-snapshot"
    settings = "os", "arch", "compiler", "build_type"

    requires = "boost/1.83.0"
    test_requires = "gtest/1.14.0"

    generators = "CMakeDeps", "CMakeToolchain"

    options = {"documentation": [True, False],
               "linting": [True, False],
               }

    default_options = {"documentation": False,
                       "linting": False,
                       }

    def build_requirements(self):
        if self.options.documentation:
            self.tool_requires("doxygen/1.9.4")
        if self.options.linting:
            self.tool_requires("cppcheck/2.12.1")
