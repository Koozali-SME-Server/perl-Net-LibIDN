COMMON_URL := https://src.koozali.org/smeserver/common.git
NAME := perl-Net-LibIDN
SPECFILE = $(firstword $(wildcard *.spec))

define find-makefile-common
	for d in common ../common ../../common ; do if [ -f "$$d/Makefile.common" ] ; then echo "$$d/Makefile.common" ; break ; fi ; done
endef

MAKEFILE_COMMON := $(shell $(call find-makefile-common))

ifeq ($(MAKEFILE_COMMON),)
# attept a checkout
define checkout-makefile-common
test -f .git/config && { git clone $(COMMON_URL) "../common" && echo "../common/Makefile.common" ; } || { echo "ERROR: I can't figure out how to clone the 'common' module." ; exit -1 ; } >&2
endef

MAKEFILE_COMMON := $(shell $(checkout-makefile-common))
else
# update with a git pull
define pull_latest_common
	for d in common ../common ../../common ; do if [ -f "$$d/Makefile.common" ] ; then ( cd "$$d" && git pull ) ; break ; fi ; done
endef
# display result
RESULT = $(shell $(call pull_latest_common))
$(info $(MAKEFILE_COMMON) is $(RESULT))
endif

include $(MAKEFILE_COMMON)

