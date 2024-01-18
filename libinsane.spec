%define api 1.0
%global major 1
%global	sname insane
%global	libname %mklibname %{sname}
%global	devname %mklibname %{sname} -d
%global girname %mklibname %{sname}-gir %{api}

Summary:	Cross-platform access to image scanners
Name:		libinsane
Version:	1.0.10
Release:	1
License:	LGPL-3.0-or-later
URL:		https://doc.openpaper.work/libinsane/latest/libinsane/index.html
Source0:	https://gitlab.gnome.org/World/OpenPaperwork/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:	meson
BuildRequires:	pkgconfig(sane-backends)
BuildRequires:	pkgconfig(cunit)
BuildRequires:	valgrind
BuildRequires:	vala
BuildRequires:	vala-tools

%description
Libinsane is a library allowing access to image scanners. It is the
successor of Pyinsane.

Main features:

 *  Cross-platform: Linux, *BSD and Windows.
 *  Cross-API: Sane (Linux, *BSD), WIA2 (Windows), TWAIN (Windows).
 *  Cross-language: Thanks to GObject introspection.
 *  Cross-scanner and cross-driver: Because a lot of them have their
    own quirks (and sometimes bugs).
 *  Returns the scanned image as the scan goes (whenever the scanner
    driver permits it)

#----------------------------------------------------------------------

%package -n %{libname}
Summary:	Cross-platform access to image scanners
Group:		System/Libraries

%description -n %{libname}
Libinsane is a library allowing access to image scanners. It is the
successor of Pyinsane.

Main features:

 *  Cross-platform: Linux, *BSD and Windows.
 *  Cross-API: Sane (Linux, *BSD), WIA2 (Windows), TWAIN (Windows).
 *  Cross-language: Thanks to GObject introspection.
 *  Cross-scanner and cross-driver: Because a lot of them have their
    own quirks (and sometimes bugs).
 *  Returns the scanned image as the scan goes (whenever the scanner
    driver permits it)

%files -n %{libname}
%license LICENSE
%doc README.markdown ChangeLog
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.*

#----------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
Development libraries and header files for %{name}.

%files -n %{devname}
%license LICENSE
%doc doc
%doc %{_datadir}/gtk-doc
%{_includedir}/%{name}
%{_includedir}/%{name}-gobject
%{_libdir}/%{name}.so
%{_libdir}/%{name}_gobject.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Libinsane-%{api}.gir
%{_datadir}/vala/vapi/%{name}.deps
%{_datadir}/vala/vapi/%{name}.vapi

#----------------------------------------------------------------------

%package -n %{girname}
Summary:		GObject introspection interface library for %{name}
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject introspection interface library for %{name}.

%files -n %{girname}
%{_libdir}/%{name}_gobject.so.1
%{_libdir}/%{name}_gobject.so.1.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Libinsane-%{api}.typelib

#----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%meson
%meson_build

# docs
%meson_build doc

%install
%meson_install

%check
#meson_test -v -t 10

