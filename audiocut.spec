Summary:	WAV file manipulation tools
Summary(pl):	Narzêdzia do manipulacji plikami WAV
Name:		audiocut
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://www.slon.net/~gody/audiocut/%{name}-%{version}.tgz
Patch0:		%{name}-make.patch
URL:		http://www.slon.net/~gody/audiocut/
BuildRequires:	libsndfile-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audiocut is package of some small programs to manipulate wav files based
on excelent libsndfile library.

%description -l pl
Audiocut to zbiór ma³ych programików do manipulowania plikami wav, oparty
na znakomitej bibliotece libsndfile.

%prep
%setup -q 
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

gcc  cut_zero_end.o -o wavtrim -lsndfile -lm
gcc  printwav.o -o wavprint -lsndfile
gcc  cat_wav.o -o wavcat -lsndfile
gcc  time_wav.o -o wavtime -lsndfile
gcc  split_wav.o -o wavsplit -lsndfile

install wavtrim $RPM_BUILD_ROOT%{_bindir}
install wavprint $RPM_BUILD_ROOT%{_bindir}
install wavcat $RPM_BUILD_ROOT%{_bindir}
install wavtime $RPM_BUILD_ROOT%{_bindir}
install wavsplit $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
