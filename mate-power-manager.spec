%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE Power Manager
Name:		mate-power-manager
Version:	1.8.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(upower-glib)
Requires:	gnome-mime-data
Requires:	mate-icon-theme
Requires:	upower

%description
MATE Power Manager uses the information and facilities provided by Upower
displaying icons and handling user callbacks in an interactive MATE session. 
MATE Power Preferences allows authorised users to set policy and 
change preferences.

%prep
%setup -q
NOCONFIGURE=yes ./autogen.sh

%build
%configure \
	--enable-applets

%make

%install
export MATEGCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std

# remove unneeded converter
rm -fr %{buildroot}%{_datadir}/MateConf

%find_lang %{name} --with-gnome --all-name
 
%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README 
%{_sysconfdir}/xdg/autostart/mate-power-manager.desktop
%{_bindir}/*
%{_sbindir}/mate-power-backlight-helper
%{_libexecdir}/mate-brightness-applet
%{_libexecdir}/mate-inhibit-applet
%{_datadir}/applications/mate-power-preferences.desktop
%{_datadir}/applications/mate-power-statistics.desktop
%{_datadir}/dbus-1/services/mate-power-manager.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.BrightnessAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.InhibitAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.power-manager.gschema.xml
%{_datadir}/mate-2.0/ui/brightness-applet-menu.xml
%{_datadir}/mate-2.0/ui/inhibit-applet-menu.xml
%{_datadir}/mate-panel/applets/org.mate.BrightnessApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.InhibitApplet.mate-panel-applet
%{_datadir}/mate-power-manager
%{_datadir}/polkit-1/actions/org.mate.power.policy
%{_iconsdir}/hicolor/*/apps/mate-*

