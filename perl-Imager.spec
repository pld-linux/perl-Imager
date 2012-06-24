#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Imager
%define	pnam	Imager
Summary:	Imager - Perl extension for generating images
Summary(pl):	Imager - rozszerzenie Perla do generowania obrazk�w
Name:		perl-Imager
Version:	0.43
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	53b25b7de75625bfc9c9c3a44c8c2f76
Patch0:		%{name}-tiff.patch
URL:		http://www.develop-help.com/imager/
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
# giflib >= 4.1.0-4 or libungif
BuildRequires:	libungif-devel >= 4.1.0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Imager is a module for creating and altering images. It can read and
write various image formats, draw primitive shapes like lines, and
polygons, blend multiple images together in various ways, scale, crop,
render text and more.

%description -l pl
Imager to modu� do tworzenia i modyfikowania obrazk�w. Potrafi czyta�
i zapisywa� r�ne formaty obrazk�w, rysowa� proste kszta�ty takie jak
linie i wielok�ty, miesza� wiele obrazk�w razem na r�ne sposoby,
skalowa�, obcina�, nanosi� tekst itd.

%prep
%setup -q -n %{pnam}-%{version}
%patch -p1

%build
# manual configuration: we want freetype2 enabled and freetype1 disabled
# y/n for: win32, ft1, t1lib, ft2, tiff, png, ungif, jpeg, gif, nogif
IM_MANUAL=y \
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor <<EOF

n
n
n
y
y
y
y
y
n
n
EOF

%{__make} \
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
%{perl_vendorarch}/%{pdir}.pm
%{perl_vendorarch}/%{pdir}
%dir %{perl_vendorarch}/auto/%{pdir}
%{perl_vendorarch}/auto/%{pdir}/%{pdir}.bs
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pdir}.so
%dir %{perl_vendorlib}/%{pdir}
%{_mandir}/man3/*
