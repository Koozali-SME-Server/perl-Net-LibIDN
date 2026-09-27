%define name perl-Net-LibIDN
%define version 1.0
%define release 0
Summary: This is what perl-Net-LibIDN does.
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
#you might need to replace %{name} with a name without perl- eg Mojolicious in place of perl-Mojolicious
Source: %{name}-%{version}.tar.gz
License: GNU GPL version 2
Group: SMEserver/addon
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildArchitectures: noarch
BuildRequires: smeserver-devtools
BuildRequires: perl(ExtUtils::Manifest)
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: smeserver-release >= 11.0
AutoReqProv: no

%description
Provides perl bindings for GNU Libidn, a C library for handling Internationalized Domain Names according to IDNA (RFC 3490), in a way very much inspired by Turbo Fredriksson's PHP-IDN.

%changelog

%prep

#you might need to replace %{name} with a name without perl- eg Mojolicious in place of perl-Mojolicious
%setup -q -n %{name}-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make_build

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
| sed -e 's/3pm"$/3pm.gz"/' \
> %{name}-%{version}-filelist

%check
make test

%clean
cd ..
rm -rf %{name}-%{version}

%pre

%preun

%post

%postun
#uninstall
%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
