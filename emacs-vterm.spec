%global srcname copr-tito-quickdoc

Name: emacs-vterm
Version: 0.0.1
Release: 1%{?dist}
License: GPLv3
Summary: A trivial python 3 program for demonstrating RPM packaging
Url: https://github.com/akermu/emacs-libvterm
Source0: https://github.com/akermu/emacs-libvterm/archive/refs/heads/master.zip

BuildArch: x86_64

BuildRequires: cmake
BuildRequires: libvterm-devel

%description
Emacs libvterm integration

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep

%cmake
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



