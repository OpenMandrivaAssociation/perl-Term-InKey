%define module Term-InKey

Summary:	Term::InKey - Perl extension for clearing the screen and receiving a keystroke
Name:		perl-%{module}
Version:	1.04
Release: %mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module implements Clear() to clear screen and ReadKey() to
receive a keystroke, on UNIX and Win32 platforms. As opposed to
Term::ReadKey, it does not contain XSUB code and can be easily
installed on Windows boxes.

%prep
%setup -q -n %{module}-%{version} 

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

