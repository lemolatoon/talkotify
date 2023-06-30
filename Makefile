.PHONY: setup run
	
setup:
	sudo apt-get install portaudio19-dev
	
run:
	python3 -m talkotify
runr:
	cd src && rye run python -m talkotify