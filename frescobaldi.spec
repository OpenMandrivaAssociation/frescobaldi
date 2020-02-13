# keep our find_lang
%define _unpackaged_files_terminate_build 0

Summary:	A LilyPond sheet music editor
Name:		frescobaldi
Version:	3.1.1
Release:	1
Source0:	https://github.com/wbsoft/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.frescobaldi.org/
BuildArch:	noarch
BuildRequires:	desktop-file-utils
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	gettext
Requires:	python-qt5
Requires:	python-poppler-qt5
Requires:	lilypond
Suggests:	portmidi

%description 
Frescobaldi is a LilyPond sheet music editor. It aims to be powerful, yet
lightweight and easy to use.

%prep
%setup -q
find -name "*.py"  -exec sed -i -e 's|#! python||' {} \;

%build
python setup.py build
#cd %{name}_app/po
#make

%install
python ./setup.py install --skip-build --root=%{buildroot}

# menu entry
desktop-file-install                                         \
   --dir=%{buildroot}%{_datadir}/applications                \
   --remove-category=Application                             \
   --add-category=AudioVideo                                 \
   --add-category=X-Notation                                 \
   --delete-original                                         \
   %{name}.desktop
   
# create lang files
for file in %{buildroot}%{python_sitelib}/%{name}_app/po/*.mo; do
    bn=$(basename $file)
    language=$(basename $file|cut -f 2 -d _|sed 's|\..*||')
    echo %%lang\($language\) %{py_puresitedir}/%{name}_app/po/$bn >> frescobaldi.lang
    done


# fix shebangs
sed -i -e 's|#!/usr/bin/python||' \
    %{buildroot}%{py_puresitedir}/%{name}_app/language_names/generate.py

    
# fix permissions
find %{buildroot}%{py_puresitedir}/%{name}_app/ -name "*.py*" -exec chmod 644 {} \;

%files
%doc ChangeLog COPYING README* THANKS TODO
%{_bindir}/%{name}
%{py_puresitedir}/%{name}_app
%{py_puresitedir}/%{name}-%{version}-py*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/frescobaldi.1.*
