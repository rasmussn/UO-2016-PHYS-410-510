#
# this is a comment

#
# define environment variables (compilers/linker/libraries...)

FC = gfortran
FFLAGS = -g
LIBS =

#
# define targets

all: hello io-example

hello.o: hello.f90
	$(FC) -c $(FFLAGS) hello.f90 -o hello.o

hello: hello.o
	$(FC) -o hello hello.o

io-example: io-example.f90
	$(FC) $(FFLAGS) -o io-example io-example.f90

# run tests
check: hello
	@echo "Running program hello..."
	@hello

clean:
	rm -f hello.o hello io-example fort.20

