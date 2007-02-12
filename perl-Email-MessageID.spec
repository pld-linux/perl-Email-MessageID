#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	MessageID
Summary:	Email::MessageID - generate world unique message-ids
Summary(pl.UTF-8):   Email::MessageID - generowanie unikalnych w skali świata message-id
Name:		perl-Email-MessageID
Version:	1.35
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	220da063bcd47368548e1ab160af6b63
URL:		http://search.cpan.org/dist/Email-MessageID/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Address >= 1.3
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Message-ids are optional, but highly recommended, headers that
identify a message uniquely. This software generates a unique
message-id.

%description -l pl.UTF-8
Message-ID to opcjonalne, ale zdecydowanie zalecane nagłówki unikalnie
identyfikujące wiadomość. Ten moduł generuje unikalne Message-ID.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Email/*.pm
%{_mandir}/man3/*
