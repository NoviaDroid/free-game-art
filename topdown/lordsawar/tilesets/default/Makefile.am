MAINTAINERCLEANFILES = Makefile.in

lordsawartilesetdir = $(datadir)/lordsawar/tilesets

default.lwt: default.lwt.in
	LC_ALL=C $(INTLTOOL_MERGE) -x -u -c $(top_builddir)/po/.intltool-merge-cache $(top_srcdir)/po $(srcdir)/default.lwt.in $(builddir)/default.lwt
	$(top_srcdir)/create-lw-file $(builddir)/default.lwt $(IMAGES)

DISTCLEANFILES = default.lwt 

lordsawartileset_DATA = default.lwt

IMAGES = \
	$(srcdir)/bridges.png \
	$(srcdir)/explosion.png \
	$(srcdir)/flags.png \
	$(srcdir)/fog.png \
	$(srcdir)/forest.png \
	$(srcdir)/grass.png \
	$(srcdir)/hills.png \
	$(srcdir)/mountains.png \
	$(srcdir)/roads.png \
	$(srcdir)/selector.png \
	$(srcdir)/small_selector.png \
	$(srcdir)/swamp.png \
	$(srcdir)/water.png

EXTRA_DIST = \
	default.lwt.in \
	README \
	$(IMAGES)
