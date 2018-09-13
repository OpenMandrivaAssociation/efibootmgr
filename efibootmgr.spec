%define minor %(echo %{version} |cut -d. -f2)
%define efidir openmandriva

Summary:	Interact with the EFI Boot Manager
Name:		efibootmgr
Version:	0.16
Release:	2
License:	GPLv2
Group:		System/Kernel and hardware
Url:		https://github.com/rhinstaller/efibootmgr
Source0:	https://github.com/rhinstaller/efibootmgr/releases/download/%{name}-%{minor}/%{name}-%{minor}.tar.bz2
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(efivar) >= 31
BuildRequires:	pkgconfig(efiboot)
BuildRequires:	pkgconfig(popt)
Requires:	efivar >= 31

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

%prep
%setup -q -n %{name}-%{minor}

%build
%setup_compile_flags
CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" CC=gcc CXX=g++ %make EFIDIR=%{efidir}
xz src/efibootmgr.8 src/efibootdump.8

%install
install -m755 src/efibootmgr -D %{buildroot}%{_sbindir}/efibootmgr
install -m755 src/efibootmgr -D %{buildroot}%{_sbindir}/efibootdump
install -m644 src/efibootmgr.8.xz -D %{buildroot}%{_mandir}/man8/efibootmgr.8.xz
install -m644 src/efibootdump.8.xz -D %{buildroot}%{_mandir}/man8/efibootdump.8.xz

%files
%doc AUTHORS COPYING README
%{_sbindir}/efibootmgr
%{_sbindir}/efibootdump
%{_mandir}/*/*.?.xz
