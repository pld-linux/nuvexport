%include	/usr/lib/rpm/macros.perl
Summary:	MythTV nuv video file conversion script
Summary(pl):	Skrypt do konwersji plików video nuv z MythTV
Name:		nuvexport
Version:	0.2
%define	_snap 20050922
%define	_rel 1
Release:	0.%{_snap}.%{_rel}
License:	GPL
Group:		Applications/Multimedia
Source0:	http://forevermore.net/files/nuvexport/%{name}-%{version}-0.%{_snap}.svn.tar.bz2
# Source0-md5:	67f55c4d8163132fda598828dd351b28
Patch0:		%{name}-DESTDIR.patch
URL:		http://forevermore.net/nuvexport/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	divx4linux
Requires:	ffmpeg >= 0.4.9
Requires:	mjpegtools >= 1.6.2
Requires:	mplayer
#Requires:	perl-base >= 1:5.6
#Requires:	perl-DateManip
#Requires:	perl-DBD-MySQL
#Requires:	perl-DBI
#Requires:	perl-Time-HiRes
Requires:	transcode >= 0.6.12
# mpeg2cut needs some others:
Requires:	avidemux2 >= 2
Requires:	lve
# Actually requires the id3tag program, but it lives in this library
Requires:	id3lib
# Provides some of its own perl modules -- rpm complains if this isn't included
#Provides:	perl(nuvexport::shared_utils)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nuvexport is a Perl script wrapper to several encoders, which is
capable of letting users choose shows from their MythTV database and
convert them to one of several different formats, including SVCD/DVD
MPEG and XviD AVI.

%description -l pl
nuvexport to skrypt Perla bêd±cy wrapperem do kilku koderów,
umo¿liwiaj±cy u¿ytkownikom wy¶wietlanie bazy danych MythTV i
konwertowanie jej do jednego z kilku ró¿nych formatów, w tym SVCD/DVD
MPEG oraz XviD AVI.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=%{_prefix} \
	bindir=%{_bindir} \
	datadir=%{_datadir} \
	mandir=%{_mandir} \
	sysconfdir=%{_sysconfdir} \
	OWNER="" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%config %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/nuvexport
%{_mandir}/man1/*
