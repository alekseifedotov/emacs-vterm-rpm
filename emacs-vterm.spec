%global pkg vterm
%global forgeurl https://github.com/akermu/emacs-libvterm

Version:
%forgemeta
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



