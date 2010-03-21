%global year 2010
%global month 03
%global parrot_version 2.2.0

%define parrot_dynext  %{_libdir}/parrot/%{parrot_version}/dynext
%define par_lang_perl6 %{_libdir}/parrot/%{parrot_version}/languages/perl6

Name:           rakudo
Version:        %{year}.%{month}
Release:        %mkrel 1

Summary:        A Perl compiler on Parrot
License:        Artistic 2.0
Group:          Development/Perl 
URL:            http://www.rakudo.org/
Source0:        http://cloud.github.com/downloads/rakudo/rakudo/rakudo-%{year}.%{month}.tar.gz

BuildRequires:  gdbm-devel
BuildRequires:  gmp-devel
BuildRequires:  libicu-devel
BuildRequires:  ncurses-devel
BuildRequires:  parrot       >= %{parrot_version}
BuildRequires:  parrot-devel >= %{parrot_version}
BuildRequires:  parrot-src   >= %{parrot_version}
BuildRequires:  readline-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Rakudo Perl 6, or just Rakudo, is a Perl 6 compiler for the Parrot virtual
machine. Rakudo is an implementation of the Perl 6 specification that runs
on the Parrot VM. More information about Perl 6 is available from:
http://perl6-projects.org

%prep
%setup -q -n %{name}-%{year}.%{month}

%build
%{__perl} Configure.pl
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CREDITS LICENSE README
%{_bindir}/perl6
%{parrot_dynext}
%{par_lang_perl6}
