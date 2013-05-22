Summary: Web based WebDAV client for dCache
Vendor: dCache.org
Name: dcache-webdav
Version: 1.0.0
Release: 1
BuildArch: noarch
Prefix: /
Packager: dCache.org <support@dcache.org>.

AutoReqProv: no
Requires: dcache >= 2.6

License: Proprietary
Group: Applications/System
Source0: %{name}-%{version}.tar


%description
Web based WebDAV client for dCache

%prep
%setup -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

cp -pr * %{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
/

%changelog
* Wed May 22 2013 Tigran Mkrtchyan <tigran.mkrtchyan@desy.de>
- initial package for webdav client
