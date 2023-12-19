Name:           software-center
Version:        1.0
Release:        10%{?dist}
Summary:        A software center for  Fedora
License:        GPLv3     
URL:            https://github.com/traxtopel/software-center
Source0:        software-center-main.zip 
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  meson
BuildRequires:  glib2-devel
BuildRequires:  gettext
Requires:       python3-gobject
Requires:       gtk4
Requires:       python3-beautifulsoup4
Requires:       flatpak
Requires:       gnome-icon-theme
Requires:       vte291-gtk4 
Requires:       gettext
Requires:       libadwaita
Requires:       mokutil
Requires:       python3-dnf

%description
A software center for  Fedora

A fork of https://github.com/yucefsourani/arfedora-welcome

%prep
%autosetup -n software-center-main

%build
%meson

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/software-center
%{_datadir}/applications/*
%{_datadir}/software-center/plugins/*
%{_datadir}/software-center/images/*
%{_datadir}/software-center/software_center/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/appdata/com.github.softwarecenter.appdata.xml
%{_datadir}/glib-2.0/schemas/com.github.softwarecenter.gschema.xml

%changelog
* Tue Dec 13 2023 traxtopel <traxtopel@gmail.com> 1.0-10
- Initial fork from arfedora-welcome 1.0-10

