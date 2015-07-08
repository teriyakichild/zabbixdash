%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define module_name myui_plugin_example
%define _usr_share_dir /usr/share/myui_plugin_example
%define _var_lib_dir /var/lib/myui_plugin_example

Name:           %{module_name}
Version:        %(python setup.py --version)
Summary:        Myui Plugin Example
Release:        1

License:        ASLv2
URL:            https://github.com/teriyakichild/myui_plugin_example
Source0:        %{module_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools

Requires: python-tornado
Requires: python-myui

%description

%prep
%setup -q -n %{module_name}-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}


%files
#%doc README
%{python_sitelib}/*
%{_usr_share_dir}/templates/*
%{_usr_share_dir}/static/*
%{_var_lib_dir}/data/*
/etc/myui.conf

%changelog
