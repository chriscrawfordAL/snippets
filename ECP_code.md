### Override disk requirements
Use "--force" on the controller and then run:
```
ERTS_PATH=/opt/bluedata/common-install/bd_mgmt/erts-*/bin
NODETOOL=/opt/bluedata/common-install/bd_mgmt/bin/nodetool
NAME_ARG=`egrep '^-s?name' $ERTS_PATH/../../releases/1/vm.args`
RPCCMD="$ERTS_PATH/escript $NODETOOL $NAME_ARG rpcterms"
$RPCCMD bd_mgmt_config update "bdshared_install_forecworkers. true."
```
