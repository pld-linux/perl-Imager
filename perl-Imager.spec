#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Imager
%define		pnam	Imager
Summary:	Imager - Perl extension for generating images
Summary(pl.UTF-8):	Imager - rozszerzenie Perla do generowania obrazków
Name:		perl-Imager
Version:	1.028
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Imager/%{pnam}-%{version}.tar.gz
# Source0-md5:	ff2d19333beb96ba29c07d741f5c1e80
URL:		http://imager.perl.org/
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--enable ft2 \
	--enable gif \
	--enable jpeg \
	--enable png \
	--enable t1 \
	--enable tiff

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Imager

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Imager/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Imager.pm
%{perl_vendorarch}/Imager
%dir %{perl_vendorarch}/auto/Imager
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/Imager.so
%dir %{perl_vendorarch}/auto/Imager/CountColor
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/CountColor/CountColor.so
%dir %{perl_vendorarch}/auto/Imager/File
%dir %{perl_vendorarch}/auto/Imager/File/GIF
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/File/GIF/GIF.so
%dir %{perl_vendorarch}/auto/Imager/File/ICO
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/File/ICO/ICO.so
%dir %{perl_vendorarch}/auto/Imager/File/JPEG
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/File/JPEG/JPEG.so
%dir %{perl_vendorarch}/auto/Imager/File/PNG
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/File/PNG/PNG.so
%dir %{perl_vendorarch}/auto/Imager/File/SGI
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/File/SGI/SGI.so
%dir %{perl_vendorarch}/auto/Imager/File/TIFF
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/File/TIFF/TIFF.so
%dir %{perl_vendorarch}/auto/Imager/Filter
%dir %{perl_vendorarch}/auto/Imager/Filter/DynTest
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/Filter/DynTest/DynTest.so
%dir %{perl_vendorarch}/auto/Imager/Filter/Flines
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/Filter/Flines/Flines.so
%dir %{perl_vendorarch}/auto/Imager/Filter/Mandelbrot
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/Filter/Mandelbrot/Mandelbrot.so
%dir %{perl_vendorarch}/auto/Imager/Font
%dir %{perl_vendorarch}/auto/Imager/Font/FT2
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/Font/FT2/FT2.so
%dir %{perl_vendorarch}/auto/Imager/Font/T1
%attr(755,root,root) %{perl_vendorarch}/auto/Imager/Font/T1/T1.so
%dir %{perl_vendorlib}/Imager
%{_mandir}/man3/Imager*.3pm*
