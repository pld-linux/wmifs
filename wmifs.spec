Summary:	wmifs is a complete network monitoring dock.app
Summary(es.UTF-8):	Aplicación para el dock del WindowMaker para monitorar la red
Summary(pl.UTF-8):	wmifs jest dokowalnym apletem monitorującym sieć
Summary(pt_BR.UTF-8):	Uma aplicação dock para a monitoração de rede
Name:		wmifs
Version:	1.3b1
Release:	9
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	ftp://ftp.mezaway.org/pub/DockApps/%{name}-%{version}.tar.gz
# Source0-md5:	4a6ec0141792debac2803e0697fa1dd6
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://windowmaker.mezaway.org/dockapps/wmifs.html
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WMiFS is a complete network monitoring dock.app, it's mainly designed
for usage in WindowMaker's dock and gives you some nice & nifty
features like:
- Autosensing of *ALL* active network interfaces;
- Integrated autoscaling (per interface) transfer statistics, tested
  upto 100Mbit;
- Displays a 'normal' xload style graph or our new 'waveform' like
  load graph;
- Realtime cycling through active interfaces by simply clicking on the
  eth0/ppp0 (interface) gadget;
- Integrated RX/TX interface activity LEDs;
- Integrated interface status LED;
- Commandline options to force monitoring a particular interface, even
  'lo' is supported (-h for help);
- User-definable scripts for left/middle/right mouse buttons which are
  read from ~/.wmifsrc (optional);
- Fixed rc file option, usefull for sites where users are not allowed
  to mess with pppd

%description -l es.UTF-8
Aplicación para el dock del WindowMaker para monitorar las interfaces
de red.

%description -l pl.UTF-8
WMiFS jest programem monitorującym sieć, przeznaczonym głównie dla
Doku WindowMakera. Zawiera m.in. możliwość automatycznego wykrywania i
monitorowania wszystkich aktywnych interfejsów sieciowych, statystyki
transferów, możliwość przekazywania opcji do programu z linii poleceń,
możliwość przypisania własnych poleceń odpowiednim klawiszom myszy
oraz wiele innych funkcji, które można modyfikować przy pomocy pliku
~/.wminetrc.

%description -l pt_BR.UTF-8
O wmifs é um aplicativo dock para monitorar vários tipos de interfaces
de rede.

%prep
%setup -q -n %{name}.app
%patch0 -p0

%build
%{__make} -C %{name} \
	CFLAGS="%{rpmcflags} -Wall" \
	LIBDIR="-L/usr/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}}
install -d $RPM_BUILD_ROOT{%{_desktopdir}/docklets,%{_sysconfdir}}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/sample.wmifsrc $RPM_BUILD_ROOT%{_sysconfdir}/wmifsrc
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES HINTS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/wmifsrc
%{_desktopdir}/docklets/wmifs.desktop
