# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


webServer:
	(cd ./build/html; python -m SimpleHTTPServer)

local:
	make clean; make html

publish:
	make clean; make html
	(cd ../../; make)

aws:
	(cd build && aws s3 sync html s3://ga-odc-eros-archive-west)


install_sphinx:
	pip3 install sphinx
	pip3 install recommonmark
	pip3 install sphinx_rtd_theme
