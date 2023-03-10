Summary:	Q16.16 format fixed point operations in C
Summary(pl.UTF-8):	Operacje na formacie stałoprzecinkowym Q16.16 w C
Name:		libfixmath
Version:	0
%define	gitref	b987044c73dcaba496bb5bc86e69d134cd8790ec
%define	snap	20230121
Release:	0.%{snap}.1
License:	MIT
Group:		Libraries
Source0:	https://github.com/PetteriAimonen/libfixmath/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	dbf2e2f22589c46a8c385b7738f49188
URL:		https://github.com/PetteriAimonen/libfixmath
BuildRequires:	cmake >= 3.13
BuildRequires:	gcc >= 6:4.7
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# only static library
%define		_enable_debug_packages	0

%description
Libfixmath implements Q16.16 format fixed point operations in C.

%description -l pl.UTF-8
Libfixmath implementuje operacje na formacie stałoprzecinkowym Q16.16
w C.

%package devel
Summary:	Q16.16 format fixed point operations in C
Summary(pl.UTF-8):	Operacje na formacie stałoprzecinkowym Q16.16 w C
Group:		Development/Libraries

%description devel
Libfixmath implements Q16.16 format fixed point operations in C.

%description devel -l pl.UTF-8
Libfixmath implementuje operacje na formacie stałoprzecinkowym Q16.16
w C.

%prep
%setup -q -n %{name}-%{gitref}

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/libfixmath}

# as expected by libreoffice (7.5.x)
cp -p libfixmath/*.{h,hpp} $RPM_BUILD_ROOT%{_includedir}/libfixmath
cp -p build/liblibfixmath.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%{_libdir}/liblibfixmath.a
%{_includedir}/libfixmath
