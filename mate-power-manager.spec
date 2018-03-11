%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE Power Manager
Name:		mate-power-manager
Version:	1.18.1
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	docbook-utils
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(unique-3.0)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	yelp-tools

Requires:	mate-icon-theme
Requires:	upower

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

The MATE Power Manager is a MATE session daemon that acts as a policy agent on
top of UPower. It listens to system events and responds with user-configurable
actions.

MATE Power Manager comes in three main parts:

  * mate-power-manager:      the manager daemon itself
  * mate-power-preferences:  the control panel program, for configuration
  * mate-power-statistics:   the statistics graphing program

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README 
%{_sysconfdir}/xdg/autostart/mate-power-manager.desktop
%{_bindir}/*
%{_sbindir}/mate-power-backlight-helper
%{_libexecdir}/mate-brightness-applet
%{_libexecdir}/mate-inhibit-applet
%{_datadir}/applications/mate-power-preferences.desktop
%{_datadir}/applications/mate-power-statistics.desktop
%{_datadir}/dbus-1/services/org.mate.panel.applet.BrightnessAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.InhibitAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.PowerManager.service
%{_mandir}/man1/mate-power-backlight-helper.1.xz
%{_mandir}/man1/mate-power-manager.1.xz
%{_mandir}/man1/mate-power-preferences.1.xz
%{_mandir}/man1/mate-power-statistics.1.xz
%{_datadir}/glib-2.0/schemas/org.mate.power-manager.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.BrightnessApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.InhibitApplet.mate-panel-applet
%{_datadir}/mate-power-manager
%{_datadir}/polkit-1/actions/org.mate.power.policy
%{_iconsdir}/hicolor/*/apps/mate-*

#---------------------------------------------------------------------------

%prep
%setup -q

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	--enable-applets \
	%{nil}
%make

%install
export MATEGCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std

#locales
%find_lang %{name} --with-gnome --all-name
 
