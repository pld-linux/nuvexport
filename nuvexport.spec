# TODO
# - remove all encoder deps and show in post banner what could be installed?
%include	/usr/lib/rpm/macros.perl
Summary:	MythTV nuv video file conversion script
Summary(pl):	Skrypt do konwersji plik�w video nuv z MythTV
Name:		nuvexport
Version:	0.2
%define	_snap 20051118
%define	_rel 1
Release:	0.%{_snap}.%{_rel}
License:	GPL
Group:		Applications/Multimedia
Source0:	http://forevermore.net/files/nuvexport/%{name}-%{version}-0.%{_snap}.svn.tar.bz2
# Source0-md5:	63a26f762dae4e486010040df16f9f84
Patch0:		%{name}-DESTDIR.patch
URL:		https://svn.forevermore.net/nuvexport/
BuildRequires:	rpm-perlprov >= 4.1-13
# for mpeg2cut
Requires:	avidemux >= 2
%ifarch %{ix86}
Requires:	divx4linux
%endif
Requires:	ffmpeg >= 0.4.9
Requires:	id3lib-utils
#Requires:	lve # not finished spec
Requires:	mencoder
Requires:	mjpegtools >= 1.6.2
Requires:	perl-DBD-mysql
Requires:	transcode >= 0.6.12
# Provides some of its own perl modules -- rpm complains if this isn't included
Provides:	perl(nuvexport::shared_utils)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nuvexport is a Perl script wrapper to several encoders, which is
capable of letting users choose shows from their MythTV database and
convert them to one of several different formats, including SVCD/DVD
MPEG and XviD AVI.

%description -l pl
nuvexport to skrypt Perla b�d�cy wrapperem do kilku koder�w,
umo�liwiaj�cy u�ytkownikom wy�wietlanie bazy danych MythTV i
konwertowanie jej do jednego z kilku r�nych format�w, w tym SVCD/DVD
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
