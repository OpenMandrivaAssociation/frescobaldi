Summary:	A LilyPond sheet music editor for KDE4
Name:		frescobaldi
Version: 	2.0.1
Release: 	2
Source0: 	http://lilykde.googlecode.com/files/%name-%version.tar.gz
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		http://www.frescobaldi.org/
BuildArch:	noarch
BuildRequires:	kde4-macros
BuildRequires:	imagemagick
BuildRequires:	qt4-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	python-kde4 >= 1:4.2.0
BuildRequires:	lilypond
BuildRequires:	python-dbus >= 0.82.4
Requires:	lilypond
Requires:	python-kde4
Requires:	python-dbus >= 0.82.4

%description 
Frescobaldi is a LilyPond sheet music editor for KDE4. It aims to be
powerful, yet lightweight and easy to use.

%files
%_kde_bindir/*
%_kde_datadir/applications/*.desktop
%{_prefix}/lib/python2.7/site-packages/*
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

#--------------------------------------------------------------------

%prep
%setup -q


%build
python setup.py build

%install
python setup.py install --prefix=%{buildroot}%{_prefix}
