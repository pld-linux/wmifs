Summary:	wmifs is a complete network monitoring dock.app
Summary(pl):	wmifs jest dokowalnym apletem monitoruj�cym sie�
Name:		wmifs
Version: 	1.3b1
Release: 	4
Copyright: 	GPL
Group:          X11/Window Managers/Tools
Group(pl):      X11/Zarz�dcy Okien/Narz�dzia
URL:		http://windowmaker.mezaway.org/dockapps/%{name}.html
Source:		ftp://ftp.mezaway.org/pub/DockApps/%{name}-%{version}.tar.gz
BuildRoot:      /tmp/%{name}-%{version}-root

%description
WMiFS is a complete network monitoring dock.app, it's mainly
designed for usage in WindowMaker's dock and gives you some
nice & nifty features like:

        * Autosensing of *ALL* active network interfaces;
        * Integrated autoscaling (per interface) transfer
          statistics, tested upto 100Mbit; 
        * Displays a 'normal' xload style graph or our new
          'waveform' like load graph;
        * Realtime cycling through active interfaces by simply
          clicking on the eth0/ppp0 (interface) gadget;
        * Integrated RX/TX interface activity LEDs;
        * Integrated interface status LED;
        * Commandline options to force monitoring a particular
          interface, even 'lo' is supported (-h for help);
        * User-definable scripts for left/middle/right mouse
          buttons which are read from ~/.wmifsrc (optional);
        * Fixed rc file option, usefull for sites where users
          are not allowed to mess with pppd

%description -l pl
WMiFS jest programem monitoruj�cym sie�, przeznaczonym g��wnie 
dla Doku WindowMakera. Zawiera m.in. mo�liwo�� automatycznego
wykrywania i monitorowania wszystkich aktywnych interfejs�w 
sieciowych, statystyki transfer�w, mo�liwo�� przekazywania opcji
do programu z linii polece�, mo�liwo�� przypisania w�asnych polece�
odpowiednim klawiszom myszy oraz wiele innych funkcji, kt�re mo�na
modyfikowa� przy pomocy pliku ~/.wminetrc.

%prep
%setup -q -n %{name}.app

%build
make -C wmifs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,share}
install -s wmifs/wmifs $RPM_BUILD_ROOT/usr/X11R6/bin
install wmifs/sample.wmifsrc $RPM_BUILD_ROOT/usr/X11R6/share/wmifsrc

gzip -9nf BUGS CHANGES HINTS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,HINTS,README,TODO}.gz
%config /usr/X11R6/share/wmifsrc
%attr(755,root,root) /usr/X11R6/bin/wmifs

%changelog
* Sun May 16 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [1.3b1-4]
- cleaned up a bit spec file for PLD use,
- package is FHS 2.0 compliant.

* Tue Feb 9 1998 Ian Macdonald <ianmacd@xs4all.nl>
- first RPM release.
