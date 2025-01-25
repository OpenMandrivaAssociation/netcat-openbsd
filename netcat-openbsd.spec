Name:       netcat-openbsd
Version:    1.229
Release:    1
Summary:    Reads and writes data across network connections using TCP or UDP
Group:      Networking/Other 
License:    BSD
URL:        https://www.openbsd.org/cgi-bin/cvsweb/src/usr.bin/nc/
BuildRequires:	pkgconfig(libbsd)
Obsoletes:      netcat-bsd
Conflicts:      netcat < 1.0
Provides:       netcat = 1.0
Conflicts:      netcat-traditional
Conflicts:      netcat-gnu

%sourcelist
https://raw.githubusercontent.com/openbsd/src/refs/heads/master/usr.bin/nc/Makefile
https://raw.githubusercontent.com/openbsd/src/refs/heads/master/usr.bin/nc/atomicio.c
https://raw.githubusercontent.com/openbsd/src/refs/heads/master/usr.bin/nc/atomicio.h
https://raw.githubusercontent.com/openbsd/src/refs/heads/master/usr.bin/nc/nc.1
https://raw.githubusercontent.com/openbsd/src/refs/heads/master/usr.bin/nc/netcat.c
https://raw.githubusercontent.com/openbsd/src/refs/heads/master/usr.bin/nc/socks.c

%patchlist
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/port-to-linux-with-libbsd.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/build-without-TLS-support.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/connect-timeout.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/get-sev-by-name.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/send-crlf.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/quit-timer.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/udp-scan-timeout.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/dccp-support.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/broadcast-support.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/serialized-handling-multiple-clients.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/set-TCP-MD5SIG-correctly-for-client-connections.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/destination-port-list.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/make-getnameinfo-errors-nonfatal-in-report_sock.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/abstract-unix-domain-socket.patch
https://sources.debian.org/data/main/n/netcat-openbsd/1.228-1/debian/patches/misc-failures-and-features.patch

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
%setup -q -T -c
cp -f %{S:0} %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} .

%autopatch -p1

%build
%make_build CFLAGS="%{build_cflags}"

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
