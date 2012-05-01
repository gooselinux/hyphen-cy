Name: hyphen-cy
Summary: Welsh hyphenation rules
%define upstreamid 20080619
Version: 0.%{upstreamid}
Release: 2.1%{?dist}
Source: http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/hyph-cy.tex
Group: Applications/Text
URL: http://tug.org/tex-hyphen
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LPPL
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Patch0: hyphen-cy-cleantex.patch

%description
Welsh hyphenation rules.

%prep
%setup -T -q -c -n hyphen-cy
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl hyph-cy.tex hyph_cy_GB.dic ISO8859-1
echo "Created with substring.pl by substrings.pl hyph-cy.tex hyph_cy_GB.dic ISO8859-1" > README
echo "---" >> README
head -n 62 hyph-cy.tex >> README

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_cy_GB.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20080619-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080619-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 13 2009 Caolan McNamara <caolanm@redhat.com> - 0.20080619-1
- initial version
