all:
	@if [ -f final_state.json ]; then \
	    echo 'Deleting final_state.json' ;\
		rm final_state.json ;\
	fi
	python3 main.py