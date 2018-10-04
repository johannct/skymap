#
# LSST Data Management System
# Copyright 2008, 2009, 2010 LSST Corporation.
#
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <http://www.lsstcorp.org/LegalNotices/>.
#

from lsst.sphgeom import ConvexPolygon
from lsst.afw.geom import Box2D

__all__ = ["PatchInfo", "makeSkyPolygonFromBBox", ]


def makeSkyPolygonFromBBox(bbox, wcs):
    """Make an on-sky polygon from a bbox and a SkyWcs

    Parameters
    ----------
    bbox : `lsst.afw.geom.Box2I` or `lsst.afw.geom.Box2D`
        Bounding box of region, in pixel coordinates
    wcs : `lsst.afw.geom.SkyWcs`
        Celestial WCS

    Returns
    -------
    polygon : `lsst.sphgeom.ConvexPolygon`
        On-sky region
    """
    pixelPoints = Box2D(bbox).getCorners()
    skyPoints = wcs.pixelToSky(pixelPoints)
    return ConvexPolygon.convexHull([sp.getVector() for sp in skyPoints])


class PatchInfo:
    """Information about a patch within a tract of a sky map

    See TractInfo for more information.
    """

    def __init__(self, index, innerBBox, outerBBox):
        """Construct a PatchInfo

        Parameters
        ----------
        index :
            x,y index of patch (a pair of ints)
        innerBBox :
            inner bounding box (an afwGeom.Box2I)
        outerBBox :
            inner bounding box (an afwGeom.Box2I)
        """
        self._index = index
        self._innerBBox = innerBBox
        self._outerBBox = outerBBox
        if not outerBBox.contains(innerBBox):
            raise RuntimeError("outerBBox=%s does not contain innerBBox=%s" % (outerBBox, innerBBox))

    def getIndex(self):
        """Return patch index: a tuple of (x, y)

        Returns
        -------
        result : `callable`
            patch index: a tuple of (x, y)
        """
        return self._index

    def getInnerBBox(self):
        """Get inner bounding box

        Returns
        -------
        result : `callable`
        """
        return self._innerBBox

    def getOuterBBox(self):
        """Get outer bounding box

        Returns
        -------
        result : `callable`
        """
        return self._outerBBox

    def getInnerSkyPolygon(self, tractWcs):
        """Get the inner on-sky region as an sphgeom.ConvexPolygon.

        Returns
        -------
        result : `callable`
        """
        return makeSkyPolygonFromBBox(bbox=self.getInnerBBox(), wcs=tractWcs)

    def getOuterSkyPolygon(self, tractWcs):
        """Get the outer on-sky region as a sphgeom.ConvexPolygon.

        Returns
        -------
        result : `callable`
        """
        return makeSkyPolygonFromBBox(bbox=self.getOuterBBox(), wcs=tractWcs)

    def __eq__(self, rhs):
        """Support ==
        """
        return (self.getIndex() == rhs.getIndex()) \
            and (self.getInnerBBox() == rhs.getInnerBBox()) \
            and (self.getOuterBBox() == rhs.getOuterBBox())

    def __ne__(self, rhs):
        """Support !=

        Returns
        -------
        result : 'callable'
        """
        return not self.__eq__(rhs)

    def __str__(self):
        """Return a brief string representation

        Returns
        -------
        result : 'callabe'
        """
        return "PatchInfo(index=%s)" % (self.getIndex(),)

    def __repr__(self):
        """Return a detailed string representation

        Returns
        -------
        result : 'callable'
        """
        return "PatchInfo(index=%s, innerBBox=%s, outerBBox=%s)" % \
            (self.getIndex(), self.getInnerBBox(), self.getOuterBBox())
