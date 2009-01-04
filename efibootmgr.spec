Summary:	Interact with the EFI Boot Manager
Name:		efibootmgr
Version:	0.5.4
Release:	%mkrel 1
License:	GPL
Group:		System/Kernel and hardware
URL:		http://domsch.com/linux/ia64/efibootmgr
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	pciutils-devel zlib-devel
ExclusiveArch:	%{ix86} ia64
BuildRoot:	%{_tmppath}/%{name}-buildroot

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

%build
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sbindir}
install -m755 src/efibootmgr/efibootmgr %{buildroot}%{_sbindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%doc doc/ChangeLog doc/TODO
%{_sbindir}/efibootmgr


