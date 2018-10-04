.. _lsst.skymap:

###############
lsst.skymap
###############

<<<<<<< HEAD
.. A sky map describes a pixelization of image data that covers most or all of the sky.
    The imaging data is arranged as a sequence of overlapping rectangular "tracts".
    Each tract is, in essence, a single large exposure. However, tracts are typically too large
    to fit into memory, so tracts are subdivided into rectangular, possibly overlapping "patches".
    The patch size is chosen to easily fit into memory.
=======
.. Paragraph that describes what this Python module does and links to related modules and frameworks.
>>>>>>> a5fcfbaab9d68ebd0f1d307686ef17586be5702d

.. Add subsections with toctree to individual topic pages.

Python API reference
====================

.. automodapi:: lsst.skymap
.. automodapi:: lsst.skymap.detail
.. automodapi:: lsst.skymap.baseSkyMap
.. automodapi:: lsst.skymap.cachingSkyMap
.. automodapi:: lsst.skymap.healpixSkyMap
.. automodapi:: lsst.skymap.ringsSkyMap