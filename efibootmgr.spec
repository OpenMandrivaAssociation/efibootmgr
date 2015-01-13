Summary:	Interact with the EFI Boot Manager
Name:		efibootmgr
Version:	0.11.0
Release:	0
License:	GPLv2
Group:		System/Kernel and hardware
Url:		https://github.com/vathpela/efibootmgr
Source0:	https://github.com/vathpela/efibootmgr/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:	%{ix86} ia64 x86_64
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(efivar)
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

%prep
%setup -q


%build
%make

%install
mkdir -p %{buildroot}%{_sbindir}
install -m755 src/efibootmgr/efibootmgr %{buildroot}%{_sbindir}

%files
%doc AUTHORS COPYING README
%doc doc/ChangeLog doc/TODO
%{_sbindir}/efibootmgr

