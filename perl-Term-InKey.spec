%define upstream_name    Term-InKey
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Term::InKey - Perl extension for clearing the screen and receiving a keystroke
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements Clear() to clear screen and ReadKey() to
receive a keystroke, on UNIX and Win32 platforms. As opposed to
Term::ReadKey, it does not contain XSUB code and can be easily
installed on Windows boxes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

# cleanup
rm -f %{buildroot}%{perl_vendorlib}/Term/demo.pl

%files
%doc Changes README
%{perl_vendorlib}/Term/InKey.pm
%{_mandir}/*/*


%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 1.40.0-2mdv2011.0
+ Revision: 664914
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 405539
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.04-6mdv2009.0
+ Revision: 241960
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.04-4mdv2008.0
+ Revision: 25456
- rebuild

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 1.04-3mdv2008.0
+ Revision: 23832
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.04-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.04-1mdk
- initial Mandriva package

