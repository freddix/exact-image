Summary:	Image processing library
Name:		exact-image
Version:	0.8.9
Release:	1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://dl.exactcode.de/oss/exact-image/%{name}-%{version}.tar.bz2
# Source0-md5:	a8694722cd7cc9aa9407950a8440f0cd
Patch0:		%{name}-libpng15.patch
URL:		http://www.exactcode.de/site/open_source/exactimage/
BuildRequires:	OpenEXR-devel
BuildRequires:	expat-devel
BuildRequires:	freetype-devel
BuildRequires:	giflib-devel
BuildRequires:	jasper-devel
BuildRequires:	lcms-devel
BuildRequires:	libagg-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	lua-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fast, modern and generic image processing library.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{rpmcxxflags}"
export CFLAGS="%{rpmcflags}"
./configure \
	--prefix=%{_prefix}	\
	--without-perl		\
	--without-php		\
	--without-python	\
	--without-ruby
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/bardecode
%attr(755,root,root) %{_bindir}/e2mtiff
%attr(755,root,root) %{_bindir}/econvert
%attr(755,root,root) %{_bindir}/edentify
%attr(755,root,root) %{_bindir}/empty-page
%attr(755,root,root) %{_bindir}/hocr2pdf
%attr(755,root,root) %{_bindir}/optimize2bw

