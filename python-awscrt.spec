Name:		python-awscrt
Version:	0.27.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/a/awscrt/awscrt-%{version}.tar.gz
Summary:	A common runtime for AWS Python projects
URL:		https://pypi.org/project/awscrt/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:	cmake
BuildSystem:	python

%description
A common runtime for AWS Python projects

%files
%{py_platsitedir}/_awscrt.*.so
%{py_platsitedir}/awscrt
%{py_platsitedir}/awscrt-*.*-info
