Summary:	A LilyPond sheet music editor
Name:		frescobaldi
Version: 	2.0.2
Release: 	1
Source0: 	http://lilykde.googlecode.com/files/%{name}-%{version}.tar.gz
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		http://www.frescobaldi.org/
BuildArch:	noarch
Requires:	lilypond
Requires:	python-poppler-qt4
Requires:	python-qt4

%description 
Frescobaldi is a LilyPond sheet music editor. It aims to be powerful, yet
lightweight and easy to use.

%files
%doc COPYING ChangeLog README THANKS TODO
%{_bindir}/*
%{py_puresitedir}/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

#--------------------------------------------------------------------

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}
