Summary:	MATE Power Manager
Name:		mate-power-manager
Version:	1.4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{lua: print (string.match(rpm.expand("%{version}"),"%d+.%d+"))}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	rarian
BuildRequires:	xmlto
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libmatenotify)
BuildRequires:	pkgconfig(libmatepanelapplet-2.0)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(mate-keyring-1)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(upower-glib)

Requires:	mate-mime-data
Requires:	mate-icon-theme
Requires(preun):	mate-conf
Requires:	upower

%description
MATE Power Manager uses the information and facilities provided by Upower
displaying icons and handling user callbacks in an interactive MATE session. 
MATE Power Preferences allows authorised users to set policy and 
change preferences.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--disable-scrollkeeper \
	--enable-applets

%make

%install
export MATEGCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std
%find_lang %{name} --with-gnome --all-name
 
%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README 
%{_sysconfdir}/mateconf/schemas/mate-power-manager.schemas
%{_sysconfdir}/xdg/autostart/mate-power-manager.desktop
%{_bindir}/*
%{_sbindir}/mate-power-backlight-helper
%{_libexecdir}/mate-brightness-applet
%{_libexecdir}/mate-inhibit-applet
%{_libexecdir}/matecomponent/servers/MATE_BrightnessApplet.server
%{_libexecdir}/matecomponent/servers/MATE_InhibitApplet.server
%{_datadir}/applications/mate-power-preferences.desktop
%{_datadir}/applications/mate-power-statistics.desktop
%{_datadir}/dbus-1/services/mate-power-manager.service
%{_datadir}/mate-2.0/ui/MATE_BrightnessApplet.xml
%{_datadir}/mate-2.0/ui/MATE_InhibitApplet.xml
%{_datadir}/polkit-1/actions/org.mate.power.policy
%{_datadir}/mate-power-manager
%{_iconsdir}/hicolor/*/apps/mate-*




%changelog
* Mon Jun 04 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.1-1
+ Revision: 802453
- imported package mate-power-manager

