%global pkg vterm
%global forgeurl https://github.com/akermu/emacs-libvterm

Version: 056ad74653704bc353d8ec8ab52ac75267b7d373
%forgemeta
Name: emacs-vterm
Release: 1%{?dist}
Summary: emacs vterm
URL:	 %{forgeurl}
Source0:  https://github.com/akermu/emacs-libvterm/archive/%{version}.zip
License: GPLv3

BuildArch: x86_64

BuildRequires: cmake
BuildRequires: libvterm-devel
BuildRequires: emacs-nw
Requires:      emacs(bin)

%description
Emacs %{pkg} integration

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%forgesetup
%cmake

%cmake_build
%cmake_install

#-- FILES ---------------------------------------------------------------------#
%files

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Fri Sep 12 2025 Aleksei Fedotov <aleksei.fedotov@toolsforhumanity.com> 0.0.1-1
- new package built with tito



