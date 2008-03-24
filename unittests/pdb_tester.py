import os
import unittest
import autoconfig

from pygccxml.msvc import pdb
from pygccxml import declarations

class tester_t( unittest.TestCase ):
    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        self.pdb_file = os.path.join( autoconfig.data_directory
                                      , 'msvc_build'
                                      , 'Debug'
                                      , 'msvc_build.pdb' )

    def __test_splitter_impl( self, name, expected_result ):
        splitter = pdb.impl_details.full_name_splitter_t( name )
        self.failUnless( len(splitter.scope_names) == len(expected_result) )
        self.failUnless( splitter.scope_names == expected_result )

    def __test_name_splitter(self):
        name = "std::_Tree<std::_Tmap_traits<engine_objects::ouuid_t,engine_objects::sql_query::parameterized_query::sql_fragment_t,std::less<engine_objects::ouuid_t>,std::allocator<std::pair<engine_objects::ouuid_t const ,engine_objects::sql_query::parameterized_query::sql_fragment_t> >,0> >::const_iterator::operator->"
        expected_result = [
            'std'
            , 'std::_Tree<std::_Tmap_traits<engine_objects::ouuid_t,engine_objects::sql_query::parameterized_query::sql_fragment_t,std::less<engine_objects::ouuid_t>,std::allocator<std::pair<engine_objects::ouuid_t const ,engine_objects::sql_query::parameterized_query::sql_fragment_t> >,0> >', 'std::_Tree<std::_Tmap_traits<engine_objects::ouuid_t,engine_objects::sql_query::parameterized_query::sql_fragment_t,std::less<engine_objects::ouuid_t>,std::allocator<std::pair<engine_objects::ouuid_t const ,engine_objects::sql_query::parameterized_query::sql_fragment_t> >,0> >::const_iterator'
        ]
        self.__test_splitter_impl( name, expected_result )

        name = 'boost::reference_wrapper<engine_objects::ops::pathable_t const >::operator engine_objects::ops::pathable_t const &'
        expected_result = [
            'boost'
            , 'boost::reference_wrapper<engine_objects::ops::pathable_t const >'
        ]
        self.__test_splitter_impl( name, expected_result )

    def __test_create_nss(self):
        reader = pdb.decl_loader_t( self.pdb_file )
        print reader.symbols_table.name
        reader.read()
        f = file( 'decls.cpp', 'w+' )
        declarations.print_declarations( reader.global_ns )#, writer=f.write )
        f.close()

    def test_undecorate_name(self):
        #basic test, that verify that function wrapper works as expected
        data = [
              # mangled, unmangled
              ( '?$rebind@D', 'rebind<char>' )
            , ( '?$rebind@PAU_Node@?$_Tree_nod@V?$_Tmap_traits@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V12@U?$less@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V12@@std@@@2@$0A@@std@@@std@@'
                , 'rebind<std::_Tree_nod<std::_Tmap_traits<std::basic_string<char,std::char_traits<char>,std::allocator<char> >,std::basic_string<char,std::char_traits<char>,std::allocator<char> >,std::less<std::basic_string<char,std::char_traits<char>,std::allocator<char> > >,std::allocator<std::pair<std::basic_string<char,std::char_traits<char>,std::allocator<char> > const ,std::basic_string<char,std::char_traits<char>,std::allocator<char> > > >,0> >::_Node *>' )
            , ( '?$rebind@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@'
                , 'rebind<std::basic_string<char,std::char_traits<char>,std::allocator<char> > >' )
            , ( '?$rebind@U_Node@?$_Tree_nod@V?$_Tmap_traits@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V12@U?$less@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V12@@std@@@2@$00@std@@@std@@'
                , 'rebind<std::_Tree_nod<std::_Tmap_traits<std::basic_string<char,std::char_traits<char>,std::allocator<char> >,std::basic_string<char,std::char_traits<char>,std::allocator<char> >,std::less<std::basic_string<char,std::char_traits<char>,std::allocator<char> > >,std::allocator<std::pair<std::basic_string<char,std::char_traits<char>,std::allocator<char> > const ,std::basic_string<char,std::char_traits<char>,std::allocator<char> > > >,1> >::_Node>' )
        ]
        for decorated, undecorated in data:
            #~ print '\n', pdb.impl_details.undecorate_name( decorated )
            #~ print undecorated
            self.failUnless( pdb.impl_details.undecorate_name( decorated ) == undecorated )

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite(tester_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
