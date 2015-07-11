%bcond_without	uclibc

Summary:	Interact with the EFI Boot Manager
Name:		efibootmgr
Version:	0.11.0
Release:	1
License:	GPLv2
Group:		System/Kernel and hardware
Url:		https://github.com/vathpela/efibootmgr
Source0:	https://github.com/vathpela/efibootmgr/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(efivar)
%if %{with uclibc}
BuildRequires:	uClibc-devel
%endif
Requires:	efivar


%description
This is efibootmgr, a Linux user-space application to modify the Intel
Extensible Firmware Interface (EFI) Boot Manager. This application can
create and destroy boot entries, change the boot order, change the
next running boot option, and more.

Details on the EFI Boot Manager are available from the EFI
Specification, v1.02 or above, available from <http://developer.intel.com>.

Note: efibootmgr no longer requires the kernel module efivars to be loaded
OpenMandriva kernels later than 3.15.15-2 provide a later interface
This version of efibootmgr requires the support library and utility contained
in the efivar package.

%if %{with uclibc}
%package -n	uclibc-%{name}
Summary:	Interact with the EFI Boot Manager (uClibc build)
Group:		System/Kernel and hardware
Requires:	uclibc-efivar

%description -n	uclibc-%{name}
This is efibootmgr, a Linux user-space application to modify the Intel
Extensible Firmware Interface (EFI) Boot Manager. This application can
create and destroy boot entries, change the boot order, change the
next running boot option, and more.

Details on the EFI Boot Manager are available from the EFI
Specification, v1.02 or above, available from <http://developer.intel.com>.

Note: efibootmgr no longer requires the kernel module efivars to be loaded
OpenMandriva kernels later than 3.15.15-2 provide a later interface
This version of efibootmgr requires the support library and utility contained
in the efivar package.
%endif

%prep
%setup -q
%if %{with uclibc}
mkdir .uclibc
cp -a * .uclibc
%endif

%build
CFLAGS="%{optflags}" %make
%if %{with uclibc}
CC=%{uclibc_cc} CFLAGS="%{uclibc_cflags}" %make -C .uclibc
%endif

%install
install -m755 src/efibootmgr/efibootmgr -D %{buildroot}%{_sbindir}/efibootmgr
%if %{with uclibc}
install -m755 .uclibc/src/efibootmgr/efibootmgr -D %{buildroot}%{uclibc_root}%{_sbindir}/efibootmgr
%endif

%files
%doc AUTHORS COPYING README
%doc doc/ChangeLog doc/TODO
%{_sbindir}/efibootmgr

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}%{_sbindir}/efibootmgr
%endif
