Summary:	WAV file manipulation tools
Summary(pl):	Narz�dzia do manipulacji plikami WAV
Name:		audiocut
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Source0:	http://www.slon.net/~gody/audiocut/%{name}-%{version}.tgz
Patch0:		%{name}-make.patch
URL:		http://www.slon.net/~gody/audiocut/
BuildRequires:	libsndfile-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audiocut is package of some small programs to manipulate wav files based
on excelent libsndfile library.

%description -l pl
Audiocut to zbi�r ma�ych programik�w do manipulowania plikami wav, oparty
na znakomitej bibliotece libsndfile.

%prep
%setup -q 
%patch0 -p1

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
