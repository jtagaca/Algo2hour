all: GCD exec #this has to be like an if GCD and else Exec you can also make GCD and just run that code. @ sign is a way to  make it invisible but still run the code.

GCD: lab2.cpp
	g++ lab2.cpp -lstdc++

exec:
	@echo "Test with 5 cases"
	for number in 1 2 3 4 5; do \
		./a.out <input_$$number >> output; \
	done
	@cat output2

py:

	@echo "Test with 5 cases"
	make clean
	for number in 1 2 3; do \
		python3 heapsort.py <input_$$number >> output; \
	done
py1:

	python3 heapsort.py >> output; \



	
clean: 
	rm output
	touch output


do :
    @echo "What is your age?: "; \
    read AGE; \
    touch $$(AGE).py

build:  
    @read -p "Enter Module Name:" module; \  
    module_dir=./modules/$$module; \
    mkdir -p $$module_dir/build