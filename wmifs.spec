Summary: wmifs is a complete network monitoring dock.app
%define version 1.3b1
Name: wmifs
Version: %{version}
Release: 3
Copyright: GPL
Group: X Windows/Window Managers
URL: http://windowmaker.mezaway.org/dockapps/%{name}.html
Source: ftp://ftp.mezaway.org/pub/DockApps/%{name}-%{version}.tar.gz
Packager: Ian Macdonald <ianmacd@xs4all.nl>
BuildRoot: /var/tmp/%{name}-root

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

%prep
%setup -n %{name}.app

%build
make -C %{name}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{etc,usr/X11R6/bin}
install -s -m 755 %{name}/%{name} $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 644 %{name}/sample.%{name}rc $RPM_BUILD_ROOT/etc/%{name}rc

%files
%defattr(-,root,root)
%config /etc/%{name}rc
/usr/X11R6/bin/%{name}
%doc BUGS CHANGES COPYING HINTS INSTALL README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Feb 9 1998 Ian Macdonald <ianmacd@xs4all.nl>

- first RPM release
