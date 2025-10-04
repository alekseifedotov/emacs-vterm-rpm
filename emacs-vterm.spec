%global pkg vterm
%global commit adf8d10212d15f9bd5ca62b96c7b423be02ce3c4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapdate 20250929

Name:           emacs-%{pkg}
Version:        0
Release:        1.%{snapdate}git%{shortcommit}%{?dist}
Summary:        Fully-fledged terminal emulator for GNU Emacs

License:        GPL-3.0-or-later
URL:            https://github.com/akermu/emacs-libvterm
Source0:        %{url}/archive/%{commit}/emacs-libvterm-%{commit}.tar.gz

BuildRequires:  cmake >= 3.11
BuildRequires:  gcc
BuildRequires:  libvterm-devel
BuildRequires:  emacs-nw >= 25.1

# Runtime requirements
# NOTE: This package contains a native dynamic module (.so file)
# and therefore is architecture-specific (NOT noarch).
# Dynamic modules require Emacs >= 25.1 with module support.
Requires:       emacs(bin) >= 25.1
# NOTE: libvterm.so dependency should be automatically detected by RPM

%description
Emacs-libvterm (vterm) is a fully-fledged terminal emulator inside GNU
Emacs based on libvterm, a C library. It is significantly faster and more
capable than the built-in term.el, and provides excellent compatibility
with command-line tools including ncurses, htop, vim, and others.

%prep
%autosetup -n emacs-libvterm-%{commit}

%build
%cmake -DUSE_SYSTEM_LIBVTERM=yes
%cmake_build

%install
# CMakeLists.txt doesn't define install rules, so we install manually

# Create package directory in Emacs site-lisp
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{pkg}

# Install the native dynamic module (.so file)
# NOTE: Must be executable (755) for Emacs to load it
install -pm 755 vterm-module.so %{buildroot}%{_emacs_sitelispdir}/%{pkg}/

# Install Elisp source files
install -pm 644 *.el %{buildroot}%{_emacs_sitelispdir}/%{pkg}/

# Byte-compile all Elisp files
# Must use absolute paths and handle errors
for el in %{buildroot}%{_emacs_sitelispdir}/%{pkg}/*.el; do
    %{_emacs_bytecompile} "$el" || {
        echo "ERROR: Failed to byte-compile $el"
        exit 1
    }
done

#-- FILES ---------------------------------------------------------------------#
%files
%license LICENSE
%doc README.md
%{_emacs_sitelispdir}/%{pkg}/

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Sat Oct 04 2025 Aleksei Fedotov <aleksei@fedotov.email> 1.0.0-1
- new package built with tito

* Fri Sep 12 2025 Aleksei Fedotov <aleksei@fedotov.email> 0-0.1
- Initial package built with tito



