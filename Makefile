.PHONY: test figs eval100 clean

test:
	pytest tests/ -q

eval100:
	python scripts/exp_eval100.py

figs:
	mkdir -p figures
	python scripts/run_all_figures.py

clean:
	rm -rf figures build *.egg-info data/eval100.csv
