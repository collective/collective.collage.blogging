import sys
import unittest
from IPython.Shell import IPShellEmbed

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite

ztc.installProduct('Collage')
ptc.setupPloneSite(products=['collective.collage.blogging',])

import collective.collage.blogging

class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml',
                             collective.collage.blogging)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass

    def ipython(self, locals=None):
        """Provides an interactive shell aka console inside your testcase.
        Uses ipython for on steroids shell...

        It looks exact like in a doctestcase and you can copy and paste
        code from the shell into your doctest. The locals in the testcase are
        available, becasue you are in the testcase.

        In your testcase or doctest you can invoke the shell at any point by
        calling::

            >>> self.ipython( locals() )

        locals -- passed to InteractiveInterpreter.__init__()
        """
        savestdout = sys.stdout
        sys.stdout = sys.stderr
        sys.stderr.write('='*70)
        embedshell = IPShellEmbed(argv=[],
                                  banner="""
IPython Interactive Console

Note: You have the same locals available as in your test-case.
""",
                                  exit_msg="""end of ZopeTestCase Interactive Console session""",
                                  user_ns=locals)
        embedshell()
        sys.stdout.write('='*70+'\n')
        sys.stdout = savestdout

def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='collective.collage.blogging',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='collective.collage.blogging.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'README.txt', package='collective.collage.blogging',
            test_class=TestCase),

        ztc.FunctionalDocFileSuite(
            'browser.txt', package='collective.collage.blogging',
            test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
