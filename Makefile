# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = build

# User-friendly check for sphinx-build
ifneq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 0)
define ERROR_MESSAGE
The '$(SPHINXBUILD)' command was not found!
Make sure you have Sphinx installed, then set the SPHINXBUILD make variable to the full path of the '$(SPHINXBUILD)' executable.
Alternatively you can add the executable's directory to your PATH.
If you don't have Sphinx installed, grab it from http://sphinx-doc.org/
endef
$(error ${ERROR_MESSAGE})
endif

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
