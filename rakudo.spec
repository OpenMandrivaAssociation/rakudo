%undefine _debugsource_packages

Name:           rakudo
Version:        2024.06
Release:        1

Summary:        A Perl compiler on Parrot
License:        Artistic 2.0
Group:          Development/Perl 
URL:            http://www.rakudo.org/
Source0:        https://rakudo.org/dl/rakudo/rakudo-%{version}.tar.gz

BuildRequires:  gdbm-devel
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(moar)
BuildRequires:  pkgconfig(readline)
BuildRequires:	nqp
BuildRequires:	perl
BuildRequires:	perl(ExtUtils::Command)
BuildRequires:	perl(IPC::Cmd)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Digest::SHA)

%description
Rakudo Perl 6, or just Rakudo, is a Perl 6 compiler for the Moar virtual
machine. Rakudo is an implementation of the Perl 6 specification that runs
on the Moar VM. More information about Perl 6 is available from:
http://perl6-projects.org

%prep
%autosetup -p1

%conf
perl Configure.pl --prefix=%{_prefix} --backends=moar

%build
%make_build

%if ! %{cross_compiling}
%check
%make test
%endif

%install
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/perl6
%{_bindir}/perl6-*
%{_bindir}/raku
%{_bindir}/raku-*
%{_bindir}/rakudo
%{_bindir}/rakudo-*
%{_datadir}/perl6
