%undefine _debugsource_packages

Name:           rakudo
Version:        2024.06
Release:        1

Summary:        A Raku compiler and runtime
License:        Artistic 2.0
Group:          Development/Perl 
URL:            https://www.rakudo.org/
Source0:        https://rakudo.org/dl/rakudo/rakudo-%{version}.tar.gz

BuildRequires:  pkgconfig(moar)
BuildRequires:  pkgconfig(readline)
BuildRequires:	nqp
BuildRequires:	perl
BuildRequires:	perl(ExtUtils::Command)
BuildRequires:	perl(IPC::Cmd)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Digest::SHA)
# For tests
BuildRequires:	perl(Test::Harness)

%description
Rakudo is a Raku compiler for the MoarVM virtual machine.
Rakudo is an implementation of the Raku specification.
More information about Raku is available from:
https://raku.org

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
