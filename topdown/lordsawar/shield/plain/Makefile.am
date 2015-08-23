MAINTAINERCLEANFILES = Makefile.in

lordsawarshielddir = $(datadir)/lordsawar/shield

plain.lws: plain.lws.in
	LC_ALL=C $(INTLTOOL_MERGE) -x -u -c $(top_builddir)/po/.intltool-merge-cache $(top_srcdir)/po $(srcdir)/plain.lws.in $(builddir)/plain.lws
	$(top_srcdir)/create-lw-file $(builddir)/plain.lws $(IMAGES)

DISTCLEANFILES = plain.lws 

lordsawarshield_DATA = plain.lws

IMAGES = \
	$(srcdir)/large-neutral-shield.png \
	$(srcdir)/large-shield.png \
	$(srcdir)/medium-neutral-shield.png \
	$(srcdir)/medium-shield.png \
	$(srcdir)/small-neutral-shield.png \
	$(srcdir)/small-shield.png

EXTRA_DIST = \
	plain.lws.in \
	README \
	$(IMAGES)
