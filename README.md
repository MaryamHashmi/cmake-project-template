## CMake C++ Project Structure Template

This project, dirivative of the [CMake Tutorial](https://cmake.org/cmake-tutorial/), is aimed at showing a preferred "common" CMake/C++ project structure.

If your project is mulit-language, and you absolutely have to keep them together, make the root one level above, and create folders such as "cpp" and "ruby", or "python", etc.

### Project Intention and Structure

By "exporting a component" we mean that the component is meant to be consumed by other projects or developers. IE. it's public, not private to the project.

### Example Project

For the simplicity sake, we'll build a tool that for every input number prints out if it's divisible by a particular number, that can also be supplied as an argument, or defaults to 2. It's very simple, and we'll call it **divisible**, and that name will now be our project's name too.

Our goal is to have:


```bash
bin/divisible [ -h/--help ] [ -d/--denominator N ] value
```

Sources:

 * `src/divisible` — C++ code that ultimately compiles into a library
 * `src/cli.cpp` C++ CLI interface parser that parses arguments and flags passed to a binary
 * a tiny `src/main.cpp` that links with both of the above
 
Tests: 


 * A `test` folder with the automated tests and fixtures that mimics the directory structure of `src`.
 * For every C++ file in `src/A/B/<name>.cpp` there is a corresponding test file `test/A/B/<name>_test.cpp`
 * Tests compile into a single binary `test/bin/runner` that is run on a command line to run the tests.
 * `test/lib` folder with a git submodule in `test/lib/googletest`, and possibly other libraries.
 
 
Here is the structure proposed here:
 

```
divisible/ 
   CMakeLists.txt       -> Top level CMake file
   bin/                 -> exported compiled executables
   doc/                 -> and compiled documentation
       usage/           -> documentation folder for how to use the tool
       design/          -> documentation folder for the developers of the tool
   include/             -> externally exported header files
       name/
   lib/                 -> compiled library we are exporting
       extern/          -> external libraries if they must be included
      
   src/                 -> sources of the project
       cli.cpp          -> the CLI argument parser/wrapper
       main.cpp         -> small main.cpp that calls into the CLI module
   test/                -> sources for all the tests
       bin/             -> where the binary `test-runner` is installed
       lib/             -> where any external libraries live
           googletest/ -> most importantly, our googletest library as a submodule
       src/
   util/                -> any bash tools, build wrappers, etc.
```


 
## Development

TBD. 

#### Contributing

Bug reports and pull requests are welcome on GitHub at [https://github.com/kigster/cmake-project-template](https://github.com/kigster/cmake-project-template)

### License

**CMake Project Template** is &copy; 2017 Konstantin Gredeskoul, available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT). 