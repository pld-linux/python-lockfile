#
# Conditional build:
%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module

%define 	module	lockfile
Summary:	Exports a LockFile class which provides a simple API for locking files
Name:		python-%{module}
Version:	0.12.2
Release:	6
License:	MIT
Group:		Development/Languages/Python
Source0:	https://github.com/openstack/pylockfile/archive/%{version}.tar.gz
# Source0-md5:	f2927523a056f4943604d08f4aa4c260
URL:		http://pypi.python.org/pypi/lockfile
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-pbr
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The lockfile package exports a LockFile class which provides a simple
API for locking files. Unlike the Windows msvcrt.locking function, the
fcntl.lockf and flock functions, and the deprecated posixfile module,
the API is identical across both Unix (including Linux and Mac) and
Windows platforms. The lock mechanism relies on the atomic nature of
the link (on Unix) and mkdir (on Windows) system calls. An
implementation based on SQLite is also provided, more as a
demonstration of the possibilities it provides than as
production-quality code.

%package -n python3-%{module}
Summary:	Exports a LockFile class which provides a simple API for locking files
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
The lockfile package exports a LockFile class which provides a simple
API for locking files. Unlike the Windows msvcrt.locking function, the
fcntl.lockf and flock functions, and the deprecated posixfile module,
the API is identical across both Unix (including Linux and Mac) and
Windows platforms. The lock mechanism relies on the atomic nature of
the link (on Unix) and mkdir (on Windows) system calls. An
implementation based on SQLite is also provided, more as a
demonstration of the possibilities it provides than as
production-quality code.

%prep
%setup -q -n pylockfile-%{version}

%build
%if %{with python2}
export PBR_VERSION=$(rpm -q --qf '%{VERSION}' python-pbr)
%py_build
%endif

%if %{with python3}
export PBR_VERSION=$(rpm -q --qf '%{VERSION}' python3-pbr)
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
export PBR_VERSION=$(rpm -q --qf '%{VERSION}' python-pbr)
%py_install

%py_postclean
%endif

%if %{with python3}
export PBR_VERSION=$(rpm -q --qf '%{VERSION}' python3-pbr)
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ACKS README.rst RELEASE-NOTES
%dir %{py_sitescriptdir}/lockfile
%{py_sitescriptdir}/lockfile/*.py[co]
%{py_sitescriptdir}/lockfile-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc ACKS README.rst RELEASE-NOTES
%{py3_sitescriptdir}/lockfile
%{py3_sitescriptdir}/lockfile-*.egg-info
%endif
