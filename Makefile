C_SRC := $(wildcard **/*.c)
C_EXE := $(patsubst %.c, %, $(C_SRC))

CPP_SRC := $(wildcard **/*.cpp)
CPP_EXE := $(patsubst %.cpp, %, $(CPP_SRC))

HS_SRC := $(wildcard **/*.hs)
HS_EXE := $(patsubst %.hs, %, $(HS_SRC))

ZIG_SRC := $(wildcard **/*.zig)
ZIG_EXE := $(patsubst %.zig, %, $(ZIG_SRC))

RS_SRC := $(wildcard **/*.rs)
RS_EXE := $(foreach wrd, $(RS_SRC), $(dir $(wrd))target/debug/$(subst /,,$(dir $(wrd))))

JAVA_SRC := $(wildcard **/*.java)
JAVA_EXE := $(patsubst %.java, %.class, $(JAVA_SRC))

CC			:=	gcc
CPPC		:=	g++

CFLAGS		:=	-Wall -Wextra -Werror

HSC			:= ghc -dynamic

ZIGC		:= zig build-exe

JAVAC		:= javac

RUSTC		:= cargo build

.PHONY: all

all: $(C_EXE) $(CPP_EXE) $(HS_EXE) $(ZIG_EXE) $(JAVA_EXE) $(RS_EXE)

$(C_EXE): %: %.c
	$(CC) $(CFLAGS) $^ -o $@

$(CPP_EXE): %: %.cpp
	$(CPPC) $(CFLAGS) $^ -o $@

$(HS_EXE): %: %.hs
	$(HSC) $^ -o $@

$(ZIG_EXE): %: %.zig
	$(ZIGC) -I. $^ -femit-bin=$@

$(JAVA_EXE): %.class: %.java
	$(JAVAC) $^

.SECONDEXPANSION:
$(RS_EXE): %: $$(foreach wrd, $$(firstword $$(subst /, ,$$(dir %))), $$(wrd)/$$(wrd).rs)
	$(RUSTC) --manifest-path $(dir $^)Cargo.toml