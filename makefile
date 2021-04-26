

All: do
.PHONY: do
do:
    @echo "What is the name of the file?: "; \
    read file && touch "$${file}.py"