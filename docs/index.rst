.. hstaxe Manual documentation master file, created by
   sphinx-quickstart on Tue Feb 19 15:56:53 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: hstaxe/images/ACS_aXe02.png


Welcome to the HSTaXe package documentation!
============================================

HSTaXe is a Python package to provide a uniform process to perform spectral
extraction for the Hubble Space Telescope. HSTaXe supports all slitless
spectroscopy modes provided by the Wide Field Camera 3 (WFC3) and Advanced
Camera for Surveys (ACS).

The core ``hstaxe`` is written in ANSI C and is highly cross-platform by
leveraging ``CFITSIO``, ``GSL``, and ``WCSLIB``, which have been successfully
employed under Linux, Solaris, and MacOS X.

HSTaXe is the successor to aXe, a similar package written on PyRAF/IRAF.

.. warning::
   We will end maintenance of HSTaXe on 3/15/2026. We currently do not accept new feature requests
   or application upgrades, and are only supporting major bug fixes until 3/15/2026. After that
   date the software will remain available in perpetuity, but we will no longer provide user support,
   bug fixes, feature requests or system upgrades. Please migrate to using Slitlessutils (see
   https://github.com/spacetelescope/slitlessutils and https://slitlessutils.readthedocs.io/en/latest/)
   for your work, and please give us feedback on the new tool and how we can best support your
   transition to using Slitlessutils.

.. warning::
   This documentation mostly overlaps with, but is not identical to, the original
   aXe manual. This means that many of the descriptions and code snippets provided
   refer to the old command line/IRAF-based version of aXe rather than the current
   python-based ``hstaxe``. The installation and example notebooks sections, as well
   as some content related to background subtraction, has been more recently updated
   to be up-to-date for ``hstaxe``. The rest of the older content is nonetheless
   useful for understanding what is going on "under the hood".

   The last version of the aXe manual can be downloaded from
   `the hstaxe repository <https://github.com/spacetelescope/hstaxe/tree/main/docs/aXe_manual/axe-user-manual-v-2-3.pdf>`_.

Attribution
-----------
This software was originally developed by the ACS group of the
Space Telescope - European Coordinating Facility (ST-ECF). The ST-ECF is a
department jointly run by the European Space Agency and the European Southern
Observatory. It is located at the ESO headquarters at Garching near Munich.
The ST-ECF staff supports the European astronomical community in exploiting the
research opportunities provided by the earth-orbiting Hubble Space Telescope.

STECF supported the use of the aXe software and the slitless spectroscopic
modes of ACS and WFC3 until late 2010. Since the beginning of 2011 support has
been provided by STScI. Please send questions to: http://hsthelp.stsci.edu


:Developers:
   Norbert Pirzkal (ST-ECF/STScI),
   Markus Demleitner (ST-ECF),
   Martin Kuemmel (ST-ECF),
   Richard Hook (ST-ECF/STScI),
   Howard Bushouse (STScI),
   Megan Sosey (STScI),
   Ricky O'Steen (STScI),
   Duy Nguyen (STScI)


Using HSTaXe
------------
.. toctree::
   :maxdepth: 2
   :numbered: 3

    Installation <hstaxe/installing.rst>
    Example Notebooks <hstaxe/examples.rst>
    Description <hstaxe/description.rst>
    Calibration Files <hstaxe/calibration_files.rst>
    Using Axe <hstaxe/using_axe.rst>
    aXe Tasks <hstaxe/axe_tasks.rst>
    Configuration Files <hstaxe/configuration_files.rst>
    File Formats <hstaxe/file_formats.rst>
    Appendix <hstaxe/appendix.rst>
    Bibliography <hstaxe/bibliography.rst>
