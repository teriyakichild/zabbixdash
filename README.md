# Myui-example-plugin

## Things to know
This will create an RPM that  
%define module_name myui_plugin_example  
%define _usr_share_dir /usr/share/myui_plugin_example  
%define _var_lib_dir /var/lib/myui_plugin_example  

%{_usr_share_dir}/templates/*  
%{_usr_share_dir}/static/*  
%{_var_lib_dir}/data/*  



## Usage:

myui --config_file=myui.conf  
