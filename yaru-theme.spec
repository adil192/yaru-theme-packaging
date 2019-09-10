%global _license COPYING COPYING.LGPL-2.1 COPYING.LGPL-3.0 LICENSE_CCBYSA

Name:           yaru-theme
Version:        19.10.1
Release:        1%{?dist}
Summary:        Ubuntu community theme "yaru"

License:        GPLv3+ and CC-BY-SA
URL:            https://community.ubuntu.com/c/desktop/theme-refresh
Source0:        https://github.com/ubuntu/yaru/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  meson >= 0.45
BuildRequires:  sassc
BuildRequires:  pkgconfig(appstream-glib)
Requires:       gnome-shell-theme-yaru
Requires:       yaru-gtk2-theme
Requires:       yaru-gtk3-theme
Requires:       yaru-icon-theme
Requires:       yaru-sound-theme

%global _description \
Yaru theme is the default theme for Ubuntu, entirely backed by the community.\
This is the theme that is shaped by the community on the Ubuntu hub, turned into\
the default theme starting from Ubuntu 18.10 Cosmic Cuttlefish.

%description %{_description}


%package     -n gnome-shell-theme-yaru
Summary:        Yaru GNOME Shell Theme
Recommends:     yaru-gtk3-theme
Recommends:     yaru-icon-theme
Suggests:       yaru-sound-theme
Suggests:       yaru-theme

%description -n gnome-shell-theme-yaru %{_description}

This package contains GNOME Shell Theme.


%package     -n yaru-gtk2-theme
Summary:        GTK+ 2 support for the Yaru GTK Theme
Requires:       adwaita-gtk2-theme
Requires:       gtk-murrine-engine
Recommends:     yaru-gtk3-theme

%description -n yaru-gtk2-theme %{_description}

This package contains GTK+ 2 theme.


%package     -n yaru-gtk3-theme
Summary:        GTK+ 3 support for the Yaru GTK Theme
Requires:       gtk3
Recommends:     yaru-gtk2-theme

%description -n yaru-gtk3-theme %{_description}

This package contains GTK+ 3 theme.


%package     -n yaru-icon-theme
Summary:        Yaru icon theme
License:        CC-BY-SA
Requires:       hicolor-icon-theme
Requires:       humanity-icon-theme
Suggests:       gnome-shell-theme-yaru
Suggests:       yaru-gtk3-theme
Suggests:       yaru-sound-theme

%description -n yaru-icon-theme %{_description}

This package contains the icon theme.


%package     -n yaru-sound-theme
Summary:        Yaru sound theme
License:        CC-BY-SA

%description -n yaru-sound-theme %{_description}

This package contains the sound theme following the XDG theming specification.


%prep
%autosetup -n yaru-%{version}

%build
%meson
%meson_build

%install
%meson_install

rm  %{buildroot}%{_datadir}/glib-2.0/schemas/99_Yaru.gschema.override \
    %{buildroot}%{_datadir}/xsessions/Yaru.desktop \
    %{buildroot}%{_datadir}/wayland-sessions/Yaru-wayland.desktop \
    %{buildroot}%{_datadir}/gnome-shell/extensions/ubuntu-dock@ubuntu.com/yaru.css

%fdupes -s %{buildroot}%{_datadir}/icons/Yaru/
%fdupes -s %{buildroot}%{_datadir}/themes/Yaru/

touch %{buildroot}%{_datadir}/icons/Yaru/icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/Yaru
gtk-update-icon-cache --force %{_datadir}/icons/Yaru &>/dev/null || :

%files
%license %{_license}
%doc AUTHORS CONTRIBUTING.md README.md
%{_datadir}/themes/Yaru-dark/index.theme
%{_datadir}/themes/Yaru/index.theme

%files -n gnome-shell-theme-yaru
%license %{_license}
%{_datadir}/gnome-shell/modes/yaru.json
%{_datadir}/gnome-shell/theme/Yaru

%files -n yaru-gtk2-theme
%license %{_license}
%{_datadir}/themes/Yaru-dark/gtk-2.0
%{_datadir}/themes/Yaru/gtk-2.0

%files -n yaru-gtk3-theme
%license %{_license}
%{_datadir}/themes/Yaru-dark/gtk-3.0
%{_datadir}/themes/Yaru-dark/gtk-3.20
%{_datadir}/themes/Yaru/gtk-3.0
%{_datadir}/themes/Yaru/gtk-3.20

%files -n yaru-icon-theme
%license %{_license}
%{_datadir}/icons/Yaru
%ghost %{_datadir}/icons/Yaru/icon-theme.cache

%files -n yaru-sound-theme
%license %{_license}
%{_datadir}/sounds/Yaru

%changelog
* Tue Sep 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.10.1-2
- Update to 19.10.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.1-3.20190425git0ddb244
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.04.1-2.20190425git0ddb244
- Adapt for Fedora

* Fri Jan 18 10:30:30 UTC 2019 - dead_mozay@opensuse.org
- Update to version 19.04+20190117.f36189f4

* Wed Jan 02 11:51:35 UTC 2019 - dead_mozay@opensuse.org
- Update to version 18.10.7+20190101.1db0abb5
