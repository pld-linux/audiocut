Summary:	WAV file manipulation tools
Summary(pl):	Narzêdzia do manipulacji plikami WAV
Name:		audiocut
Version:	0.6
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://www.slon.net/~gody/audiocut/%{name}-%{version}.tgz
Patch0:		%{name}-make.patch
Patch1:		%{name}-misc.patch
URL:		http://www.slon.net/~gody/audiocut/
BuildRequires:	libsndfile-devel >= 1.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audiocut is package of some small programs to manipulate wav files
based on excelent libsndfile library.

%description -l pl
Audiocut to zbiór ma³ych programików do manipulowania plikami wav,
oparty na znakomitej bibliotece libsndfile.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	cc=%{__cc} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install wavtrim wavprint wavcat wavtime wavsplit $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
