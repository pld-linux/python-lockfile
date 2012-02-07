%define 	module	lockfile
Summary:	Exports a LockFile class which provides a simple API for locking files
Name:		python-%{module}
Version:	0.9.1
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pylockfile.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	4e4c7ea4c4301500da5e7f3b51e01cfe
URL:		http://pypi.python.org/pypi/lockfile
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKS README RELEASE-NOTES
%dir %{py_sitescriptdir}/lockfile
%{py_sitescriptdir}/lockfile/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/lockfile-*.egg-info
%endif
