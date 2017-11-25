# pykudpc

Python2.7 tools for kudpc(Kyoto-univ supercomputer system).

# Usage
## functions
Almost same with kupdc shell commands.

### qs()
return type:list of dicts

### qstat()
return type:list of dict

### qstatq()
return type:list of dict
This is equivalent to command "qstat -q".

### qdel(jobid)

## class run
### tssrun
|Arguments|type|default value|description| 
|:-|:-|:-|:-|
|exec_file|character|required|Executing file| 
|p|integer|1|Process|
|c|integer|1|Core|
|t|integer|1|Threads|
|mem|character|"3840M"|Memory|
|wtime|character|"1:0"|Limitation of execute time|
|queue|character|defalut queue|Use queue|

### submit
For batch execution.

|Arguments|type|default value|description| 
|:-|:-|:-|:-|
|exec_file|character|required|Executing file| 
|p|integer|1|Process|
|c|integer|1|Core|
|t|integer|1|Threads|
|mem|character|"3840M"|Memory|
|wtime|character|"1:0"|Limitation of execute time|
|queue|character|defalut queue|Use queue|
|stdout|character|defalut|Stdout file|
|errout|character|defalut|Errout file|
|mailaddr|character|defalut|Email address|
|rstrt|bool|True|Permission of restart|
|jobname|character|default|Name of job|
