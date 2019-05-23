SUBDIRS := $(wildcard */)

# $(SUBDIRS) without trailing slashes.
SUBDIRS2 := $(patsubst %/,%,$(SUBDIRS))

all: $(SUBDIRS)

$(SUBDIRS) $(SUBDIRS2):
	$(MAKE) -C $@ image

.PHONY: all $(SUBDIRS) $(SUBDIRS2)

