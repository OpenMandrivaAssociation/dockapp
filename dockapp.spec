%define name          dockapp
%define version       0.4.0
%define release       %mkrel 4
%define lib_name_orig libdockapp
%define lib_major     0
%define lib_name      %mklibname %{name} %{lib_major}
%define	lib_name_devel	%mklibname %{name} %{lib_major} -d


# virtual package to enforce naming convention

Summary:	A library useful for dockapps
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:	GPL
Source:		libdockapp-0.4.0.tar.bz2
Patch1:		libdockapp-0.4.0.patch.bz2
URL:		ftp://shadowmere.student.utwente.nl/pub/WindowMaker
Group:		System/Libraries
BuildRequires:	X11-devel xpm-devel
BuildRoot:	%{_tmppath}/%{lib_name}-buildroot

%description
libDockApp is a rather small library dedicated to writting dock apps
for wmaker. 


%package -n %{lib_name}
Summary: A library useful for dockapps
Group: System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with %{lib_name_orig}.


%package -n %{lib_name_devel}
Summary: A library useful for dockapps - development environment
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: %{lib_name_orig}-devel = %{version}-%{release} %{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
Install %{name} if you need to compile an application with %{lib_name}
support.

%prep 
%setup -q -n libdockapp-%{version}
%patch1 -p1

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root)
%doc AUTHORS COPYING 
%{_libdir}/libdockapp.so.1.0.0
%{_libdir}/libdockapp.so.1

%files  -n %{lib_name_devel}
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README
%{_libdir}/libdockapp.a
%{_libdir}/libdockapp.la
%{_libdir}/libdockapp.so
%{_includedir}/dockapp.h

