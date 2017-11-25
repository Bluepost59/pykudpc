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
        qs_keys = ["queue","user","jobid","status",\
                   "proc","thread","core","memory","time"]

        qs_rawresult = sbp.check_output('qs')
        
        job_list = qs_rawresult.split('\n')
        qs_list = [mystr.split() for mystr in job_list[1:-1]]

        qs_result = [dict(zip(qs_keys,qs_list[i])) \
                     for i in range(len(qs_list))]
        
        return qs_result
        
    def qstat(self):
        keys = ["jobid","name","user","time","s","queue"]
        
        qstat_rawresult = sbp.check_output('qstat')
        qstat_list = qstat_rawresult.split('\n')
        qstat_result = [mystr.split() for mystr in qstat_list[2:-1]]
        
        return [dict(zip(keys,qstat_result[i])) \
                for i in range(len(qstat_result)) ]

    def qstatq(self):
        keys = ["queue","memory","cputime","walltime","node",\
                "run","que","lm","state"]

        qstatq_rawresult = sbp.check_output('qstat -q', shell=True)
        qstatq_linelist = qstatq_rawresult.split("\n")

        len_list = [len(mystr) for mystr in qstatq_linelist[1].split()]
        pos_list = [sum(len_list[:i]) + i for i in range(len(len_list)+1)]
        
        qstatq_result = [ [ mystr[pos_list[i]:pos_list[i+1]].strip()\
                            for i in range(len(len_list))] \
                          for mystr in qstatq_linelist[2:-1]]
    
        return [dict(zip(keys,mydata)) \
                for mydata in qstatq_result]

    def qdel(self,job):
        sbp.call('qdel ' + job, shell=True)



