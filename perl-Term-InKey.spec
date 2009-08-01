%define upstream_name    Term-InKey
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Term::InKey - Perl extension for clearing the screen and receiving a keystroke
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements Clear() to clear screen and ReadKey() to
receive a keystroke, on UNIX and Win32 platforms. As opposed to
Term::ReadKey, it does not contain XSUB code and can be easily
installed on Windows boxes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

# cleanup
rm -f %{buildroot}%{perl_vendorlib}/Term/demo.pl

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Term/InKey.pm
%{_mandir}/*/*
