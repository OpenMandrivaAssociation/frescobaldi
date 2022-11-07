# keep our find_lang
%define _unpackaged_files_terminate_build 0

Summary:	A LilyPond sheet music editor
Name:		frescobaldi
Version:	3.2
Release:	2
Source0:	https://github.com/wbsoft/frescobaldi/releases/download/v%{version}/%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.frescobaldi.org/
BuildArch:	noarch
BuildRequires:	desktop-file-utils
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	gettext

Requires:   python-qt5-core
Requires:   python-qt5-gui
Requires:   python-qt5-network
Requires:   python-qt5-printsupport
Requires:   python-qt5-svg
Requires:   python-qt5-webkit
Requires:   python-qt5-webkitwidgets
Requires:   python-qt5-widgets
Requires:   python-qt5-xml

Requires:   python3dist(python-ly)
Requires:	python-qt5
Requires:	python-poppler-qt5
Requires:	lilypond
Suggests:	portmidi

%description 
Frescobaldi is a LilyPond sheet music editor. It aims to be powerful, yet
lightweight and easy to use.

%files
%doc ChangeLog COPYING README* THANKS TODO
%{_bindir}/%{name}
%{py_puresitedir}/%{name}_app
%{py_puresitedir}/%{name}-%{version}-py*.egg-info
%{_datadir}/applications/org.%{name}.Frescobaldi.desktop
%{_iconsdir}/hicolor/scalable/apps/org.%{name}.Frescobaldi.svg
%{_mandir}/man1/frescobaldi.1.*

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

