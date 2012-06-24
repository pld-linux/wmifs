Summary:	wmifs is a complete network monitoring dock.app
Summary(pl):	wmifs jest dokowalnym apletem monitoruj�cym sie�
Summary(pt_BR):	Uma aplica��o dock para a monitora��o de rede
Summary(es):	Aplicaci�n para el dock del WindowMaker para monitorar la red
Name:		wmifs
Version:	1.3b1
Release:	6
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source0:	ftp://ftp.mezaway.org/pub/DockApps/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://windowmaker.mezaway.org/dockapps/wmifs.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

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

%description -l pl
WMiFS jest programem monitoruj�cym sie�, przeznaczonym g��wnie dla
Doku WindowMakera. Zawiera m.in. mo�liwo�� automatycznego wykrywania i
monitorowania wszystkich aktywnych interfejs�w sieciowych, statystyki
transfer�w, mo�liwo�� przekazywania opcji do programu z linii polece�,
mo�liwo�� przypisania w�asnych polece� odpowiednim klawiszom myszy
oraz wiele innych funkcji, kt�re mo�na modyfikowa� przy pomocy pliku
~/.wminetrc.

%description -l pt_BR
O wmifs � um aplicativo dock para monitorar v�rios tipos de interfaces
de rede.

%description -l es
Aplicaci�n para el dock del WindowMaker para monitorar las interfaces
de red

%prep
%setup -q -n %{name}.app
%patch -p0

%build
%{__make} -C %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_applnkdir}/DockApplets} 

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/sample.wmifsrc $RPM_BUILD_ROOT%{_datadir}/wmifsrc
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf BUGS CHANGES HINTS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config %{_datadir}/wmifsrc
%attr(755,root,root) %{_bindir}/%{name}

#%{_applnkdir}/DockApplets/wmifs.desktop
