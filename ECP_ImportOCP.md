Importing OCP into ECP

Install OCP on AWS:
https://docs.openshift.com/container-platform/4.5/installing/installing_aws/installing-aws-default.html

Set up peer cxn between the 

Follow instructions here:
http://docs.bluedata.com/51_k8s-importing-an-external-kubernetes-cluster

Use updated bd_util_k8s_http.beam file that Krisha sent

Clear Default Storage if set:
bdconfig --set "bds_global_provisionmapr=false"

Modify /opt/bluedata/common-install/bd_mgmt/k8s_manifest.json to remove install of kube-state-metrics

Confgure KSM:
https://docs.openshift.com/container-platform/4.3/monitoring/cluster_monitoring/configuring-the-monitoring-stack.html

CLEANUP
Run script which does not remove KSM and then re-create binding
kubectl create clusterrolebinding add-on-cluster-admin --clusterrole=cluster-admin --serviceaccount=default:abc123
