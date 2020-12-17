%define minor %(echo %{version} |cut -d. -f2)

%global optflags %{optflags} -Oz -Wno-pointer-sign

Summary:	Interact with the EFI Boot Manager
Name:		efibootmgr
Version:	0.17
Release:	4
License:	GPLv2
Group:		System/Kernel and hardware
Url:		https://github.com/rhboot/efibootmgr
Source0:	https://github.com/rhboot/efibootmgr/releases/download/%{name}-%{minor}/%{name}-%{minor}.tar.gz
# (tpg) patches from upstream git
Patch0:		0000-remove-extra-decl.patch
Patch1:		0001-Make-sure-PKGS-is-propogated-into-the-submake-for-ma.patch
Patch2:		0000-Get-rid-of-a-memory-leak-of-deleted-boot-entries.patch
# (tpg) patch from Fedora
Patch100:	efibootmgr-16-efidp_format_device_path-argfix.patch

BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(efivar) >= 37
BuildRequires:	pkgconfig(efiboot)
BuildRequires:	pkgconfig(popt)
BuildRequires:	efi-srpm-macros
BuildRequires:	efi-filesystem
Requires:	efivar >= 37
Requires:	efi-filesystem

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
%autosetup -n %{name}-%{minor} -p1

%build
# (tpg) define grub loaders name per archs
%ifarch %{x86_64} riscv64
%define efiloader grub64
%else
%define efiloader grub
%endif

%set_build_flags
CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" CC=%{__cc} CXX=%{__cxx} %make_build EFIDIR=%{efi_vendor} EFI_LOADER=%{efiloader}.efi

%install
install -m755 src/efibootmgr -D %{buildroot}%{_sbindir}/efibootmgr
install -m755 src/efibootmgr -D %{buildroot}%{_sbindir}/efibootdump
install -m644 src/efibootmgr.8 -D %{buildroot}%{_mandir}/man8/efibootmgr.8
install -m644 src/efibootdump.8 -D %{buildroot}%{_mandir}/man8/efibootdump.8

%files
%doc AUTHORS COPYING README
%{_sbindir}/efibootmgr
%{_sbindir}/efibootdump
%{_mandir}/*/*.?.*
