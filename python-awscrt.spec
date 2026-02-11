%define module awscrt

Name:		python-awscrt
Version:	0.31.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	A common runtime for AWS Python projects
URL:		https://pypi.org/project/awscrt/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
A common runtime for AWS Python projects

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%files
%{py_platsitedir}/_%{module}.*.so
%{py_platsitedir}/%{module}
%{py_platsitedir}/%{module}-%{version}.dist-info
