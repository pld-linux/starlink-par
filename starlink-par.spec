Summary:	PAR - ADAM parameter system
Summary(pl):	PAR - system parametrów ADAM
Name:		starlink-par
Version:	2.3.218
Release:	1
License:	non-commercial use and distribution (see PAR_CONDITIONS)
Group:		Libraries
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/par/par.tar.Z
# Source0-md5:	6ab7ae3d35eb4fad52bbd59d75a78cbf
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_PAR.html
BuildRequires:	gcc-g77
BuildRequires:	sed >= 4.0
BuildRequires:	starlink-err-devel
BuildRequires:	starlink-sae-devel
Requires:	starlink-sae
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
PAR is a library of Fortran subroutines that provides convenient
mechanisms for applications to exchange information with the outside
world, through input-output channels called parameters. Parameters
enable a user to control an application's behaviour. PAR supports
numeric, character, and logical parameters, and is currently
implemented only on top of the ADAM parameter system.

The PAR library permits parameter values to be obtained, without or
with a variety of constraints. Results may be put into parameters to
be passed onto other applications. Other facilities include setting a
prompt string, and suggested defaults.

%description -l pl
PAR to biblioteka funkcji fortranowych dostarczaj±ca wygodne
mechanizmy dla aplikacji do wymiany informacji z zewnêtrznym ¶wiatem
poprzez kana³y wej¶cia-wyj¶cia nazywane parametrami. Parametry
pozwalaj± u¿ytkownikowi sterowaæ zachowaniem aplikacji. PAR obs³uguje
parametry numeryczne, znakowe i logiczne; aktualnie jest
zaimplementowany tylko w oparciu o system parametrów ADAM.

Biblioteka PAR pozwala na uzyskanie warto¶ci parametrów bez lub z
ró¿nymi ograniczeniami. Wyniki mog± byæ umieszczone w parametrach do
przekazania do innych aplikacji. Inne mo¿liwo¶ci obejmuj± ustawianie
³añcucha zachêty i sugerowanych warto¶ci domy¶lnych.

%package devel
Summary:	Header files for PAR library
Summary(pl):	Pliki nag³ówkowe biblioteki PAR
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for PAR library.

%description devel -l pl
Pliki nag³ówkowe biblioteki PAR.

%package static
Summary:	Static Starlink PAR library
Summary(pl):	Statyczna biblioteka Starlink PAR
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Starlink PAR library.

%description static -l pl
Statyczna biblioteka Starlink PAR.

%prep
%setup -q -c

sed -i -e "s/ -O'/ %{rpmcflags} -fPIC'/;s/ ld -shared -soname / g77 -shared \\\$\\\$3 -Wl,-soname=/" mk
sed -i -e "s/\\('-L\\\$(STAR_\\)LIB) /\\1SHARE) -lsubpar_adam -lerr_adam /" makefile

%build
SYSTEM=ix86_Linux \
./mk build \
	STARLINK=%{stardir} \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/help

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc PAR_CONDITIONS par.news
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/sun*
%{stardir}/help/fac*
%attr(755,root,root) %{stardir}/share/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{stardir}/bin/par_dev
%attr(755,root,root) %{stardir}/bin/par_link*
%{stardir}/include/*

%files static
%defattr(644,root,root,755)
%{stardir}/lib/*.a
