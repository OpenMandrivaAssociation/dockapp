%define name          dockapp
%define version       0.4.0
%define release       %mkrel 8
%define lib_name_orig libdockapp
%define lib_major     1
%define lib_name      %mklibname %{name} %{lib_major}
%define	lib_name_devel	%mklibname %{name} -d


# virtual package to enforce naming convention

Summary:	A library useful for dockapps
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:	GPL
Source:		libdockapp-0.4.0.tar.bz2
Patch1:		libdockapp-0.4.0.patch
URL:		ftp://shadowmere.student.utwente.nl/pub/WindowMaker
Group:		System/Libraries
BuildRequires:	libx11-devel
BuildRequires:	libxpm-devel
BuildRequires:	libxext-devel
BuildRoot:	%{_tmppath}/%{lib_name}-buildroot

%description
libDockApp is a rather small library dedicated to writting dock apps
for wmaker. 


%package -n %{lib_name}
Summary: A library useful for dockapps
Group: System/Libraries
Provides: %{name} = %{version}-%{release}
Obsoletes: %{_lib}dockapp0 < %{version}-%{release}

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with %{lib_name_orig}.


%package -n %{lib_name_devel}
Summary: A library useful for dockapps - development environment
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: %{lib_name_orig}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{_lib}dockapp0-devel < %{version}-%{release}

%description -n %{lib_name_devel}
Install %{name} if you need to compile an application with %{lib_name}
support.

%prep 
%setup -q -n libdockapp-%{version}
%patch1 -p1

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%defattr(-,root,root)
%doc AUTHORS COPYING 
%{_libdir}/libdockapp.so.%{lib_major}.*
%{_libdir}/libdockapp.so.%{lib_major)

%files  -n %{lib_name_devel}
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README
%{_libdir}/libdockapp.a
%{_libdir}/libdockapp.la
%{_libdir}/libdockapp.so
%{_includedir}/dockapp.h
