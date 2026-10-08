CXX := g++
CXXFLAGS := -std=c++17 -Wall -Wextra -Iinclude
TARGET := Familiar
SOURCE := \
	src/main.cpp \
	src/Application.cpp

OBJECTS := $(SOURCES:.cpp=.o)
.PHONY: all clean run test
all: $(TARGET)

$(TARGET): $(OBJECTS) -o $@

src/%.o: src/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@
run: $(TARGET)
	./$(TARGET)
test:
	@echo "Tests not configure yet."

clean:
	rm -f $(OBJECTS) $(TARGET)