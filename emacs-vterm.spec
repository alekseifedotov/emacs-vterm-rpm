%global srcname copr-tito-quickdoc

Name: emacs-vterm
Version: 0.0.0
Release: 0%{?dist}
License: GPLv3
Summary: A trivial python 3 program for demonstrating RPM packaging
Url: https://pagure.io/%{srcname}
Source0: https://github.com/akermu/emacs-libvterm.git

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


