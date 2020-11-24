### Override disk requirements
Use "--force" on the controller and then run:
```
ERTS_PATH=/opt/bluedata/common-install/bd_mgmt/erts-*/bin
NODETOOL=/opt/bluedata/common-install/bd_mgmt/bin/nodetool
NAME_ARG=`egrep '^-s?name' $ERTS_PATH/../../releases/1/vm.args`
RPCCMD="$ERTS_PATH/escript $NODETOOL $NAME_ARG rpcterms"
$RPCCMD bd_mgmt_config update "bdshared_install_forecworkers. true."
```
### Delete a stubborn cluster or a cluster in state "error"
On the Controller - enter these commands on the command line:
```
ERTS_PATH=/opt/bluedata/common-install/bd_mgmt/erts-*/bin
NODETOOL=$ERTS_PATH/../../bin/nodetool
NAME_ARG=`egrep ‘^-s?name’ $ERTS_PATH/../../releases/1/vm.args`
RPCCMD=“$ERTS_PATH/escript $NODETOOL $NAME_ARG rpcterms”
${RPCCMD} bd_mgmt_config lookup ‘tenant_storage_root.’
```
<should show a data structure/record, and not ‘undefined’>
Set it to undefined, to crudely wipe out memory of tenant storage :-)
```
${RPCCMD} bd_mgmt_config update ‘tenant_storage_root. undefined.’ (edited) 
```
