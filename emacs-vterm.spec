%global pkg vterm

Name: emacs-%{pkg}
Version: 0.0.1
Release: %autorelease
License: GPLv3
Summary: A trivial python 3 program for demonstrating RPM packaging
Url: https://github.com/akermu/emacs-libvterm
Source0: https://github.com/akermu/emacs-libvterm/archive/refs/heads/master.zip

BuildArch: x86_64

BuildRequires: cmake
BuildRequires: libvterm-devel
BuildRequires: emacs-nw
Requires:      emacs(bin)

%description
Emacs %{pkg} integration

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
exit 98
%autosetup -n %{pkg}-%{version}

%build

%install

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
%{_bindir}/hellocopr
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Fri Sep 12 2025 Aleksei Fedotov <aleksei.fedotov@toolsforhumanity.com> 0.0.1-1
- new package built with tito



