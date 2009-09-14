Name:       netcat-openbsd
Version:    1.89
Release:    %mkrel 4
Summary:    Reads and writes data across network connections using TCP or UDP
Group:      Networking/Other 
License:    BSD
URL:        http://www.openbsd.org/cgi-bin/cvsweb/src/usr.bin/nc/
# source is CVS checkout
Source0:    netcat-openbsd-%{version}.tar.gz
Patch0:     openbsd-compat.patch
Patch1:     socks-b64-prototype.patch
Patch2:     silence-z.patch
Patch3:     glib-strlcpy.patch
Patch4:     no-strtonum.patch
Patch5:     pollhup.patch
Patch6:     reuseaddr.patch
Patch7:     connect-timeout.patch
Patch8:     udp-scan-timeout.patch
Patch9:     verbose-numeric-port.patch
Patch10:    send-crlf.patch
Patch11:    help-version-exit.patch
Patch12:    quit-timer.patch
Patch13:    getservbyname.patch
Patch14:    gcc-warnings.patch
Patch20:    netcat-openbsd-1.89-makefile.patch
Patch21:    netcat-openbsd-1.89-openbsd-compat.patch
Requires:       glib2
BuildRequires:  glib2-devel
Obsoletes:      netcat-bsd
Conflicts:      netcat < 1.0
Provides:       netcat = 1.0
Conflicts:      netcat-traditional
Conflicts:      netcat-gnu
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
The nc package contains Netcat (the program is actually nc), a simple
utility for reading and writing data across network connections, using
the TCP or UDP protocols. Netcat is intended to be a reliable back-end
tool which can be used directly or easily driven by other programs and
scripts.  Netcat is also a feature-rich network debugging and
exploration tool, since it can create many different connections and
has many built-in capabilities.

You may want to install the netcat package if you are administering a
network and you'd like to use its debugging and network exploration
capabilities.

%prep
%setup -q -n netcat-openbsd-%{version}.orig

%patch20 -p1
%patch21 -p1

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

%build
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m 755 nc %{buildroot}%{_bindir}
(cd %{buildroot}%{_bindir} && ln -s nc netcat)
install -d %{buildroot}%{_mandir}/man1
install -m 644 nc.1 %{buildroot}%{_mandir}/man1
(cd %{buildroot}%{_mandir}/man1 && ln -s nc.1 netcat.1)

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/nc
%{_bindir}/netcat
%{_mandir}/man1/nc.1*
%{_mandir}/man1/netcat.1*
