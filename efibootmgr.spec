Summary:	Interact with the EFI Boot Manager
Name:		efibootmgr
Version:	0.6.0
Release:	7
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://domsch.com/linux/ia64/efibootmgr
Source0:	http://linux.dell.com/efibootmgr/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:		efibootmgr-0.5.4-autoload-module.patch
ExclusiveArch:	%{ix86} ia64 x86_64
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(zlib)

%description
This is efibootmgr, a Linux user-space application to modify the Intel
Extensible Firmware Interface (EFI) Boot Manager. This application can
create and destroy boot entries, change the boot order, change the
next running boot option, and more.

Details on the EFI Boot Manager are available from the EFI
Specification, v1.02 or above, available from <http://developer.intel.com>.

Note: efibootmgr requires that the kernel module efivars be loaded
prior to use.  `modprobe efivars` should do the trick.

%prep
%setup -q
%apply_patches

%build
%make

%install
mkdir -p %{buildroot}%{_sbindir}
install -m755 src/efibootmgr/efibootmgr %{buildroot}%{_sbindir}

%files
%doc AUTHORS COPYING README
%doc doc/ChangeLog doc/TODO
%{_sbindir}/efibootmgr

