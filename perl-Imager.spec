#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Imager
%define		pnam	Imager
Summary:	Imager - Perl extension for generating images
Summary(pl.UTF-8):	Imager - rozszerzenie Perla do generowania obrazków
Name:		perl-Imager
Version:	0.97
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Imager/%{pnam}-%{version}.tar.gz
# Source0-md5:	38856623b113e2c73bdbf61119adc353
URL:		http://www.develop-help.com/imager/
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	giflib-devel >= 4.1.0-4
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	t1lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Imager is a module for creating and altering images. It can read and
write various image formats, draw primitive shapes like lines, and
polygons, blend multiple images together in various ways, scale, crop,
render text and more.

%description -l pl.UTF-8
Imager to moduł do tworzenia i modyfikowania obrazków. Potrafi czytać
i zapisywać różne formaty obrazków, rysować proste kształty takie jak
linie i wielokąty, mieszać wiele obrazków razem na różne sposoby,
skalować, obcinać, nanosić tekst itd.

%prep
%setup -q -n %{pnam}-%{version}

%build
# manual configuration: we want freetype2 enabled and freetype1 disabled
# y/n for: win32, ft1, t1lib, ft2, tiff, png, ungif, jpeg, gif
IM_MANUAL=y \
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor <<EOF

n
n
n
y
y
y
n
y
y
EOF

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Imager

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Imager/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Imager.pm
%{perl_vendorarch}/Imager
%dir %{perl_vendorarch}/auto/Imager
%{perl_vendorarch}/auto/Imager/Imager.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/Imager.so
%dir %{perl_vendorarch}/auto/Imager/CountColor
%{perl_vendorarch}/auto/Imager/CountColor/CountColor.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/CountColor/CountColor.so
%dir %{perl_vendorarch}/auto/Imager/File
%dir %{perl_vendorarch}/auto/Imager/File/GIF
%{perl_vendorarch}/auto/Imager/File/GIF/GIF.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/File/GIF/GIF.so
%dir %{perl_vendorarch}/auto/Imager/File/ICO
%{perl_vendorarch}/auto/Imager/File/ICO/ICO.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/File/ICO/ICO.so
%dir %{perl_vendorarch}/auto/Imager/File/JPEG
%{perl_vendorarch}/auto/Imager/File/JPEG/JPEG.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/File/JPEG/JPEG.so
%dir %{perl_vendorarch}/auto/Imager/File/PNG
%{perl_vendorarch}/auto/Imager/File/PNG/PNG.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/File/PNG/PNG.so
%dir %{perl_vendorarch}/auto/Imager/File/SGI
%{perl_vendorarch}/auto/Imager/File/SGI/SGI.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/File/SGI/SGI.so
%dir %{perl_vendorarch}/auto/Imager/File/TIFF
%{perl_vendorarch}/auto/Imager/File/TIFF/TIFF.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/File/TIFF/TIFF.so
%dir %{perl_vendorarch}/auto/Imager/Filter
%dir %{perl_vendorarch}/auto/Imager/Filter/DynTest
%{perl_vendorarch}/auto/Imager/Filter/DynTest/DynTest.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/Filter/DynTest/DynTest.so
%dir %{perl_vendorarch}/auto/Imager/Filter/Flines
%{perl_vendorarch}/auto/Imager/Filter/Flines/Flines.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/Filter/Flines/Flines.so
%dir %{perl_vendorarch}/auto/Imager/Filter/Mandelbrot
%{perl_vendorarch}/auto/Imager/Filter/Mandelbrot/Mandelbrot.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/Filter/Mandelbrot/Mandelbrot.so
%dir %{perl_vendorarch}/auto/Imager/Font
%dir %{perl_vendorarch}/auto/Imager/Font/FT2
%{perl_vendorarch}/auto/Imager/Font/FT2/FT2.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/Font/FT2/FT2.so
%dir %{perl_vendorarch}/auto/Imager/Font/T1
%{perl_vendorarch}/auto/Imager/Font/T1/T1.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/Font/T1/T1.so
%dir %{perl_vendorlib}/Imager
%{_mandir}/man3/Imager*.3pm*
