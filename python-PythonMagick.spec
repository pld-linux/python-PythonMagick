%define 	module	PythonMagick
Summary:	PythonMagick
Summary(pl.UTF-8):	Interfejs Pythona do ImageMagicka
Name:		python-%{module}
Version:	0.9.1
Release:	1
License:	GPL v3
Group:		Development/Languages/Python
Source0:	http://www.imagemagick.org/download/python/%{module}-%{version}.tar.lzma
# Source0-md5:	fb6227e86628aa2f6eea04dcacfe013b
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-python-devel
BuildRequires:	libtool
BuildRequires:	lzma >= 1:4.42
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#%pyrequires_eq	python-libs
%pyrequires_eq	python-modules
# Build fails D_FORTIFY_SOURCE
%define		filterout_cpp		-D_FORTIFY_SOURCE=[0-9]+
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PythonMagick is the Python API for the ImageMagick.

%description -l pl.UTF-8
PythonMagick to moduł Pythona do ImageMagicka.

%prep
%setup -q -c -T -n %{module}-%{version}
lzma -dc %{SOURCE0} | tar xf - -C ..

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-static=no \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/PythonMagick
%{py_sitedir}/PythonMagick/*.py[co]
%attr(755,root,root) %{py_sitedir}/PythonMagick/*.so
