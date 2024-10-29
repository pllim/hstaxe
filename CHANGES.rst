version 1.0.6 (2024-10-29)
--------------------------

- Bumped numpy max pin to <2.0 to fix install issue and addressed some
  related deprecations. [#98]

version 1.0.5 (2023-07-11)
--------------------------

- Fixed a capitalization issue that would cause ACS prism processing to
  fail with a KeyError. [#84]

version 1.0.4 (2023-05-22)
--------------------------

- Assorted code fixes to fix warnings. [#82]

version 1.0.3 (2023-01-06)
--------------------------

Bug fixes
^^^^^^^^^

- Hotfix to avoid incompatibility with numpy 1.24.

version 1.0.2 (2023-01-06)
--------------------------

Bug Fixes
^^^^^^^^^

- ``axeprep`` no longer looks for fringe column if ``backgr`` is False. [#31]
- Added missing flag to allow local background subtraction. [#35]
- Input checks now properly allow interp 0. [#39]

Other Changes
^^^^^^^^^^^^^

- Disabled sensitivity adjustment for UVIS rather than failing silently. [#40]
- Updated package installation to work with more recent python versions.
- Updated installation instructions and documentation.

version 1.0.1 (2022-01-10)
--------------------------
- changed licensing to be inline with GPLv3
- updates to setup and cfg
- updated package setup to allow pip installations

version 1.0.0 (2021-02-19)
--------------------------
- fixed bug in drzprep call to lower level C that affected ACS data
- added more fstring conversions and some documentation text
- minor changes to the pytests
- update build system for inclusion in astroconda

version 0.7.0 (2020-11-03)
--------------------------
- changed the default settings for optimal extraction for safety
- wfc3 is verified working
- acs tentative verification
- added example notebook for WFC3 full axe extraction to jupyter directory

version 0.6.5 (2020-11-01)
--------------------------
- changed the axeprep call from runall to run

version 0.6.0 (2020-09-28)
--------------------------
package namechange from pyaxe to hstaxe
Beta release for testing.
This version should complete for WFC3 and ACS and includes axedrizzle

version 0.5a (2019-12-14)
-------------------------
Alpha release verison of pyaxe for testing.
This version should complete for both regular extraction and optimal extraction, except optimal extraction still has a bug in the final STP and SPC files, which may have blank data.

submit all bugs and problems to the issue tracker for this repository


Some feature notes from the previous IRAF software package
----------------------------------------------------------
- Version 2.4.4:
    axeprep doesn't require direct image column for input list file

- Version 2.4.3:
    - #978 - added full support for astrodrizzle cases with dimen_info not zero
    - #779 - check for subarray input images in axeprep and return an error
    - #678 - dont do background subtraction in axeprep when < 10% pixels are deemed good
    - #1033 - I put a catch in so that if the C code reports 0 good sky pixels no background subtraction is done and it doesn't fatal error out

- Version 2.4.2:
    - #1017 resolved. User reported an error with the "SCI" extension when the segementation image was read in fcubeprep. The code was updated to be more generic in the way headers are read and constructed.

- Version 0.20: PyDrizzle will be automatically run to generate coeffs files
    - if not already present for input image.

- Version 0.21: Syntax for calling PyDrizzle updated for new 'bits' syntax.
    - Created wtran to use wtraxy and wtranback, and hence be MUCH faster in
      list mode.
    - Updated 'raise' statements to use Exception class, to conform to latest
      python syntax rules.

- Version 0.12 for STSDAS 3.3 release, October 2004
