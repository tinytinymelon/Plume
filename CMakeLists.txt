cmake_minimum_required(VERSION 3.16)

project(plume LANGUAGES CXX)

# sync with systemc-2.3.3 CXXFLAGS -> -std=c++14
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# third-party libraries
set(THIRD_PARTY_DIR ${CMAKE_CURRENT_SOURCE_FILE}/third-party)
set(THIRD_PARTY_LIB ${THIRD_PARTY_DIR}/lib)

# setup systemc-2.3.3 libpath
set(SYSTEM_PATH ${THIRD_PARTY_LIB}/systemc-2.3.3)
set(SYSTEMC_INCLUDE_DIRS ${SYSTEMC_PATH}/include)
set(SYSTEMC_LIBRARIES systemc)
set(SYSTEMC_LIBRARY_DIRS ${SYSTEMC_PATH}/lib)

# append include files
file(GLOB_RECURSE INC_FILES "include/*.h")
set(INCLUDES ${INC_FILES}) 

# glob source files
file(GLOB_RECURSE SRC_FILES "src/*.cpp")
set(SOURCES ${SRC_FILES})
add_executable(plume ${SOURCES})

# include
target_include_directories(
    plume PRIVATE 
    ${SYSTEMC_INCLUDE_DIRS}
    ${INCLUDES}
)

# link
target_link_libraries(plume PRIVATE ${SYSTEMC_LIBRARIES})
