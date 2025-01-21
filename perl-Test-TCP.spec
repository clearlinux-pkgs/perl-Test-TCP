#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Test-TCP
Version  : 2.22
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Test-TCP-2.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Test-TCP-2.22.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtest-tcp-perl/libtest-tcp-perl_2.19-1.debian.tar.xz
Summary  : 'testing TCP program'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-TCP-license = %{version}-%{release}
Requires: perl-Test-TCP-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::SharedFork)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
Test::TCP - testing TCP program
# SYNOPSIS
use Test::TCP;
my $server = Test::TCP->new(
listen => 1,
code => sub {
my $socket = shift;
...
},
);
my $client = MyClient->new(host => '127.0.0.1', port => $server->port);
undef $server; # kill child process on DESTROY

%package dev
Summary: dev components for the perl-Test-TCP package.
Group: Development
Provides: perl-Test-TCP-devel = %{version}-%{release}
Requires: perl-Test-TCP = %{version}-%{release}

%description dev
dev components for the perl-Test-TCP package.


%package license
Summary: license components for the perl-Test-TCP package.
Group: Default

%description license
license components for the perl-Test-TCP package.


%package perl
Summary: perl components for the perl-Test-TCP package.
Group: Default
Requires: perl-Test-TCP = %{version}-%{release}

%description perl
perl components for the perl-Test-TCP package.


%prep
%setup -q -n Test-TCP-2.22
cd %{_builddir}
tar xf %{_sourcedir}/libtest-tcp-perl_2.19-1.debian.tar.xz
cd %{_builddir}/Test-TCP-2.22
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Test-TCP-2.22/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-TCP
cp %{_builddir}/Test-TCP-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-TCP/e32922cc01823ebfc593b2b733ee5cc1a7ae405c || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Test-TCP/b2a6ad1cc91a081c098bc71b38696e2bf4883e42 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::EmptyPort.3
/usr/share/man/man3/Test::TCP.3
/usr/share/man/man3/Test::TCP::CheckPort.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-TCP/b2a6ad1cc91a081c098bc71b38696e2bf4883e42
/usr/share/package-licenses/perl-Test-TCP/e32922cc01823ebfc593b2b733ee5cc1a7ae405c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
