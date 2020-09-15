corpus.prevert: script.py
	python3 ./script.py $(shell ls | grep .csv) > $@ 

.PHONY: clean
clean:
	rm *.csv