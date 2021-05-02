All: dothis
# .PHONY: do
dothis:
    echo "TESTING"
    read -p "Name of file? " filetest ; touch "$${filetest}.py"