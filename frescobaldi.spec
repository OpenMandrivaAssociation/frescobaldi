# Keep our find_lang
#global _unpackaged_files_terminate_build 1

Summary:	A LilyPond sheet music editor
Name:	frescobaldi
Version:	4.0.4
Release:	1
Source0:	https://github.com/wbsoft/frescobaldi/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source100:	frescobaldi.rpmlintrc
License:	GPLv2+
Group:	Graphical desktop/KDE
Url:		https://www.frescobaldi.org/
#BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	python3dist(pyproject-api)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(setuptools_scm)
BuildRequires:	pkgconfig(python)

Requires:	python-qt6-core >= 6.6
Requires:	python-qt6-gui
Requires:	python-qt6-network
Requires:	python-qt6-printsupport
Requires:	python-qt6-svg
Requires:	python-qt6-webchannel
Requires:	python-qt6-webengine
Requires:	python-qt6-widgets
Requires:	python-qt6-xml
Requires:	python-qpageview >= 1.0.1
Requires:	python-ly) >= 0.9.5
# Import not present anywhere in the sources
#Requires:	python-poppler-qt5
Requires:	lilypond
Suggests:	portmidi

BuildArch:	noarch

%description 
Frescobaldi is a LilyPond sheet music editor. It aims to be powerful, yet
lightweight and easy to use.

%files
%license LICENSE
%doc CHANGELOG.md README* THANKS TODO
%{_bindir}/%{name}
%{py_puresitedir}/%{name}
%{py_puresitedir}/%{name}-%{version}.dist-info
%{_datadir}/applications/org.%{name}.Frescobaldi.desktop
%{_iconsdir}/hicolor/scalable/apps/org.%{name}.Frescobaldi.svg
%{_metainfodir}/org.%{name}.Frescobaldi.metainfo.xml
%{_mandir}/man1/%{name}.1.*

#-----------------------------------------------------------------------

%prep
%autosetup -p1


%build
%py_build


%install
%py_install

# Manually install some stuff needed but not installed by %%py_install
mkdir -p %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_metainfodir}/
mkdir -p %{buildroot}%{_iconsdir}/hicolor/scalable/apps/
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/
install -m 0644 linux/org.%{name}.Frescobaldi.metainfo.xml %{buildroot}%{_metainfodir}/
install -m 0755 linux/org.%{name}.Frescobaldi.desktop %{buildroot}%{_datadir}/applications/
install -m 0644 %{name}/icons/org.%{name}.Frescobaldi.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/

# Fix perms and shebangs
chmod +x %{buildroot}%{py_puresitedir}/%{name}/language_names/generate.py
chmod +x %{buildroot}%{py_puresitedir}/%{name}/unicode_blocks.py
sed -i '1s|^#!/usr/bin/env python|#!%{__python}|' %{buildroot}%{py_puresitedir}/%{name}/language_names/generate.py
sed -i '1s|^#!/usr/bin/env python|#!%{__python}|' %{buildroot}%{py_puresitedir}/%{name}/unicode_blocks.py
