MAINTAINERCLEANFILES = Makefile.in

lordsawartilesetdir = $(datadir)/lordsawar/tilesets

bigdefault.lwt: bigdefault.lwt.in
	LC_ALL=C $(INTLTOOL_MERGE) -x -u -c $(top_builddir)/po/.intltool-merge-cache $(top_srcdir)/po $(srcdir)/bigdefault.lwt.in $(builddir)/bigdefault.lwt
	$(top_srcdir)/create-lw-file $(builddir)/bigdefault.lwt $(IMAGES)

DISTCLEANFILES = bigdefault.lwt 

lordsawartileset_DATA = bigdefault.lwt

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
	bigdefault.lwt.in \
	README \
	$(IMAGES)
