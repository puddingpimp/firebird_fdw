Summary: A PostgreSQL foreign data wrapper (FDW) for Firebird
Name: postgresql93-firebird_fdw
Version: 0.2.5
Release: 1
Source: firebird_fdw-%{version}.tar.gz
URL: https://github.com/ibarwick/firebird_fdw
License: PostgreSQL
Group: Productivity/Databases/Tools
Packager: Ian Barwick
BuildRequires: postgresql93-devel
BuildRequires: libfq
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Requires: postgresql93-server libfq

%description
This is an experimental foreign data wrapper (FDW) to connect PostgreSQL
to Firebird. It provides both read (SELECT) and write (INSERT/UPDATE/DELETE)
support, WHERE-clause pushdowns, connection caching and Firebird transaction
support.

This code is very much work-in-progress; USE AT YOUR OWN RISK.


%prep
%setup

%build

PG_CPPFLAGS="-I/usr/include/firebird" make

%install
rm -rf $RPM_BUILD_ROOT
export PG_CONFIG=/usr/bin/pg_config
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/usr/lib/postgresql93/lib64/firebird_fdw.so
/usr/share/postgresql93/extension/firebird_fdw--%{version}.sql
/usr/share/postgresql93/extension/firebird_fdw.control

%changelog
* Tue Feb 11 2014 Ian Barwick (barwick@gmail.com)
- First draft

