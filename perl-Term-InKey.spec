%define upstream_name    Term-InKey
%define upstream_version 1.04
Name:		perl-%{upstream_name}
Version:	1.04
Release:	1

Summary:	Term::InKey - Perl extension for clearing the screen and receiving a keystroke
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Term-InKey
Source0:	https://cpan.metacpan.org/authors/id/R/RA/RAZINF/Term-InKey-1.04.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements Clear() to clear screen and ReadKey() to
receive a keystroke, on UNIX and Win32 platforms. As opposed to
Term::ReadKey, it does not contain XSUB code and can be easily
installed on Windows boxes.

%prep
%setup -q -n %{upstream_name}-%{version}

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


