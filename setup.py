from distutils.core import setup, Extension

desc = """\
blender-mathutils module
========================

overview
++++++++

This module originated from blender (the opensource 3d package), where it has
been used for some years in production as a utility module for use in areas
including animation, games and mesh manipulation.

This differs from 'numpy' in that it is computer graphics focused, combining
Matrix and Vector types with rotation classes which is very useful for use with
animation or anywhere Euler and Quaternion values are used frequently.

This project is mainly a build system around the actively maintained mathutils
code in blender to allow non blender related projects to make use of it. A link
to the blender repository is used so the source never gets out of sync. 
"""

include_dirs = [
    "src/stubs",
    "src/blenlib",
    ]

source_files = [
    "src/stubs/stubs.c",

    "src/blenlib/intern/math_base.c",
    "src/blenlib/intern/math_base_inline.c",
    "src/blenlib/intern/math_color.c",
    "src/blenlib/intern/math_geom.c",
    "src/blenlib/intern/math_geom_inline.c",
    "src/blenlib/intern/math_matrix.c",
    "src/blenlib/intern/math_rotation.c",
    "src/blenlib/intern/math_vector.c",
    "src/blenlib/intern/math_vector_inline.c",

    "src/mathutils/mathutils.c",
    "src/mathutils/mathutils_Color.c",
    "src/mathutils/mathutils_Euler.c",
    "src/mathutils/mathutils_Matrix.c",
    "src/mathutils/mathutils_Quaternion.c",
    "src/mathutils/mathutils_Vector.c",
    "src/mathutils/mathutils_geometry.c",
    ]


setup(name="mathutils",
      version="2.58a",
      maintainer="Campbell Barton",
      maintainer_email="ideasman42@gmail.com",
      url="http://code.google.com/p/blender-mathutils",
      ext_modules=[Extension("mathutils",
                             source_files,
                             include_dirs=include_dirs,
                             define_macros=[("MATH_STANDALONE", None)]
                             )
                  ],
     )
