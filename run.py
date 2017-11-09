#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
from glob import *
import sys
import errno
import subprocess as sbp

#------------------------------
# class run
#------------------------------
class run:
    def __init__(self):
        self.login_node = sbp.check_output('hostname').split(".")[0][:-1]
        self.queue = ''

    def tssrun(self, exec_file, \
               p=1, c=1, t=1, mem="3840M",\
               wtime = "1:0", queue = ''):
        
        if len(queue) == 0:
            mycom = 'tssrun -A p=' + str(p) + \
                    ':c=' + str(c) + \
                    ':t=' + str(t) + \
                    ':m=' + mem + \
                    ' -W ' + wtime + \
                    ' ' + exec_file
        else:
            mycom = 'tssrun -A p=' + str(p) + \
                    ':c=' + str(c) + \
                    ':t=' + str(t) + \
                    ':m=' + mem + \
                    ' -W ' + wtime + \
                    ' -q ' + queue + \
                    ' -ug ' + queue[:-1] + \
                    ' ' + exec_file

        print mycom
        os.system(mycom)

    def submit(self, exec_file,\
                p=1, c=1, t=1, mem="3840M", wtime = "1:0" ,\
                queue = '', \
                stdout = '', errout = '', mailaddr = '', mailopt = '', \
                rstrt = True, jobname = ''):

        if len(queue) == 0:
            queue = self.queue
            ugroup = self.queue[:-1]

            if len(queue) == 0:
                print "Error:queue is not specified."
                exit

        jobscript_file = 'job.sh'

        jobscript = open(jobscript_file, 'w')

        if not queue_ischecked(queue,self.login_node):
            print "warning:Wrong queue is specified."
            new_queue = queue[:-1] + sys_symbol[self.login_node]
            print "queue is modified " + queue + "->" + new_queue
            queue = new_queue

        jobscript.write('#!/bin/bash\n')
        jobscript.write('#============ PBS Option ============\n')
        jobscript.write('#QSUB -q ' + queue + '\n')
        jobscript.write('#QSUB -ug ' + ugroup + '\n')
        jobscript.write('#QSUB -W ' + wtime + '\n')
        jobscript.write('#QSUB -A p=' + str(p) + ':t=' + str(t) +\
                        ':c=' + str(c) + ':m=' + mem + '\n')
       
        if len(stdout) > 0: jobscript.write('#QSUB -o ' + stdout + '\n')
        if len(errout) > 0: jobscript.write('#QSUB -e ' + errout + '\n')
        if len(mailaddr) > 0: jobscript.write('#QSUB -M ' + mailaddr + '\n')
        if len(mailopt) > 0: jobscript.write('#QSUB -m ' + mailopt + '\n')

        if not rstrt: jobscript.write('#QSUB -r n \n')

        if self.login_node == 'camphor':
            if len(jobname) > 0: jobscript.write('#QSUB -N ' + jobname + '\n')            
        jobscript.write('#============ Shell Script ============\n')
 
        if self.login_node == 'camphor':
            jobscript.write('aprun -n $QSUB_PROCS -d $QSUB_THREADS -N $QSUB_PPN ' + exec_file + '\n')
        elif self.login_node == 'laurel' or self.login_node == 'cinnamon':
            if p == 1: 
                jobscript.write(exec_file)
            else : jobscript.write('mpiexec.hydra ' + exec_file)

        jobscript.close()

        sbp.call('chmod u+x ' + jobscript_file, shell=True) 
        
        qsub_cmd = 'qsub ' + jobscript_file
        # print qsub_cmd
        qsub_result = sbp.check_output(qsub_cmd, shell=True)
        return qsub_result

#functions
sys_symbol = {'camphor':'a',\
              'laurel':'b',\
              'cinnamon':'c',\
              'camellia':'e'}

def queue_ischecked(queue,node):
    if queue[-1] == sys_symbol[node]: return True
    else: return False

