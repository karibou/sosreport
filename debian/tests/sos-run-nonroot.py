#!/usr/bin/python3
import sys
import unittest
import os
import tempfile
import shutil
import glob
import time
import subprocess

# PYCOMPAT
import six
try:
    from StringIO import StringIO
except:
    from io import StringIO


class SosRunTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.workdir = tempfile.mkdtemp()

    @classmethod
    def tearDownClass(self):
        shutil.rmtree(self.workdir)

    def test_run_sosreport(self):
        try:
            proc = subprocess.Popen(['sosreport', '--batch',
                                     '--tmp-dir', '%s' % self.workdir],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            out, err = proc.communicate()
            self.assertEqual(err.strip().decode('utf8'),
                             'no valid plugins were enabled')
        except subprocess.CalledProcessError as err:
            self.fail('sosreport Error : %s' % err)


if __name__ == "__main__":
    unittest.main(verbosity=0)

# vim: et ts=4 sw=4
