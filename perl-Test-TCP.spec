#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-TCP
Version  : 2.19
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Test-TCP-2.19.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Test-TCP-2.19.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtest-tcp-perl/libtest-tcp-perl_2.19-1.debian.tar.xz
Summary  : 'testing TCP program'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-TCP-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::SharedFork)

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

%description dev
dev components for the perl-Test-TCP package.


%package license
Summary: license components for the perl-Test-TCP package.
Group: Default

%description license
license components for the perl-Test-TCP package.


%prep
%setup -q -n Test-TCP-2.19
cd ..
%setup -q -T -D -n Test-TCP-2.19 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Test-TCP-2.19/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-TCP
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-TCP/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Test-TCP/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/Net/EmptyPort.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/TCP.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/TCP/CheckPort.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::EmptyPort.3
/usr/share/man/man3/Test::TCP.3
/usr/share/man/man3/Test::TCP::CheckPort.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-TCP/LICENSE
/usr/share/package-licenses/perl-Test-TCP/deblicense_copyright
