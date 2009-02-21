Summary:	A LilyPond sheet music editor for KDE4
Name:		frescobaldi
Version: 	0.7.6
Release: 	%mkrel 2
Source0: 	http://lilykde.googlecode.com/files/%name-%version.tar.gz
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		http://www.frescobaldi.org/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	kde4-macros
BuildRequires:	imagemagick
BuildRequires:	python-kde4
BuildRequires:	lilypond
BuildRequires:	python-dbus >= 0.82.4
Requires:	python-kde4
Requires:	python-dbus >= 0.82.4
Requires:	okular

%description 
Frescobaldi is a LilyPond sheet music editor for KDE4. It aims to be
powerful, yet lightweight and easy to use.

%if %mdkversion < 200900
%post
%update_menus

%postun
%update_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/%name
%_kde_iconsdir/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang %name

%clean
rm -rf %{buildroot}
