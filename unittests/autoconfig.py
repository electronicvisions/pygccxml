# Copyright 2004 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys
import getpass

#__pychecker__ = 'limit=1000'
#import pychecker.checker

compiler = None
gccxml_path = ''
data_directory = os.path.abspath( os.path.join( os.curdir, 'data' ) )
build_dir = os.path.abspath( os.path.join( os.curdir, 'temp' ) )

if 'roman' in getpass.getuser():
    if sys.platform == 'win32':
        compiler = 'msvc71'
        gccxml_path = r'D:/dev/gccxml/gccxml.exe'
    else:
        gccxml_path = '/home/roman/gccxml/bin/gccxml'

try:
    import pygccxml
    print 'unittests will run on INSTALLED version'
except ImportError:
    sys.path.append( os.path.join( os.curdir, '..' ) )
    import pygccxml
    print 'unittests will run on DEVELOPMENT version'

pygccxml.declarations.class_t.USE_DEMANGLED_AS_NAME = True

class cxx_parsers_cfg:
    gccxml = pygccxml.parser.gccxml_configuration_t( gccxml_path=gccxml_path
                                                     , working_directory=data_directory
                                                     , compiler=compiler )

    synopsis = pygccxml.parser.synopsis_configuration_t( working_directory=data_directory )


#~ try:
    #~ import pydsc
    #~ pydsc.include( r'D:\pygccxml_sources\sources\pygccxml_dev' )
    #~ pydsc.ignore( [ 'Yakovenko'
             #~ , 'Bierbaum'
             #~ , 'org'
             #~ , 'http'
             #~ , 'bool'
             #~ , 'str'
             #~ , 'www'
             #~ , 'param'
             #~ , 'txt'
             #~ , 'decl'
             #~ , 'decls'
             #~ , 'namespace'
             #~ , 'namespaces'
             #~ , 'enum'
             #~ , 'const'
             #~ , 'GCC'
             #~ , 'xcc'
             #~ , 'TODO'
             #~ , 'typedef'
             #~ , 'os'
             #~ , 'normcase'
             #~ , 'normpath'
             #~ , 'scopedef'
             #~ , 'ira'#part of Matthias mail address
             #~ , 'uka'#part of Matthias mail address
             #~ , 'de'#part of Matthias mail address
             #~ , 'dat'#file extension of directory cache
             #~ , 'config'#parameter description
             #~ , 'gccxml'#parameter description
             #~ , 'Py++'
             #~ , 'pygccxml'
             #~ , 'calldef'
             #~ , 'XXX'
             #~ , 'wstring'
             #~ , 'py'
             #~ ] )
#~ except ImportError:
    #~ pass
