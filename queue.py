#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
from glob import *
import sys
import errno
import subprocess as sbp

class queue:
    def __init__(self):
        pass

    def qs(self):
        qs_rawresult = sbp.check_output('qs')
        
        job_list = qs_rawresult.split('\n')
        qs_result = [mystr.split() for mystr in job_list[1:-1]]

        return qs_result
        
    def qstat(self):
        qstat_rawresult = sbp.check_output('qstat')
        qstat_list = qstat_rawresult.split('\n')
        qstat_result = [mystr.split() for mystr in qstat_list[2:-1]]

        return qstat_result
    
    def qstatq(self):
        qstatq_rawresult = sbp.check_output('qstat -q', shell=True)
        qstatq_list = qstatq_rawresult.split("\n")
        qstatq_result = [mystr.split() for mystr in qstatq_list[2:-1]]
        return qstatq_result

    def qdel(self,job):
        sbp.call('qdel ' + job, shell=True)



