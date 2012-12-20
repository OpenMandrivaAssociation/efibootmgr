Summary:	Interact with the EFI Boot Manager
Name:		efibootmgr
Version:	0.5.4
Release:	8
License:	GPL
Group:		System/Kernel and hardware
URL:		http://domsch.com/linux/ia64/efibootmgr
Source0:	%{name}-%{version}.tar.bz2
Patch0:		efibootmgr-0.5.4-autoload-module.patch
BuildRequires:	pkgconfig(libpci) pkgconfig(zlib)
ExclusiveArch:	%{ix86} ia64 x86_64

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




%changelog
* Thu Dec 20 2012 Bernhard Rosenkraenzer <bero@lindev.ch> 0.5.4-8
- Add x86_64 support
- Autoload the efivars module

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.4-5mdv2011.0
+ Revision: 664126
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.4-4mdv2011.0
+ Revision: 605098
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.4-3mdv2010.1
+ Revision: 522572
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5.4-2mdv2010.0
+ Revision: 424382
- rebuild

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 0.5.4-1mdv2009.1
+ Revision: 324488
- New upstream release
- New upstream release

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.5.3-4mdv2009.0
+ Revision: 220720
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.5.3-3mdv2008.1
+ Revision: 149690
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Mar 18 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-2mdv2007.1
+ Revision: 145964
- make it build (thanks spturtle)
- Import efibootmgr

* Sun Mar 18 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-2mdv2007.1
- bunzip patches

* Fri Jan 20 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.5.3-1mdk
- 0.5.3 (no change since 0.5.2.2)
- cosmetics (exclusivearch, description)

* Mon Jan 16 2006 Stefan van der Eijk <stefan@eijk.nu> 0.5.2.2-2mdk
- %%mkrel
- BuildRequires

* Fri Oct 21 2005 Bruno Cornec <bcornec@mandriva.org> 0.5.2.2-1mdk
- 0.5.2

