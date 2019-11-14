DOT=dot -Tsvg
DOTP=dot -Tpng
DOTS = odcT1.dot
DOTSVG = odcT1.svg
DOTPNG = STACflow.png dataLakeGeneral.png lakeToViz.png processRefModel.png year1.png year2.png odcstac.png

%.svg: %.dot
	$(DOT) -o $@ $<

%.png: %.dot
	$(DOTP) -o $@ $<

#.PHONY: dot
#dot: $(DOTSVG) 

.PHONY: dot2
dot2: $(DOTPNG)
