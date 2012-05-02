Summary:	A LilyPond sheet music editor
Name:		frescobaldi
Version:	2.0.6
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
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%dir %{py_puresitedir}/frescobaldi_app
%{py_puresitedir}/frescobaldi-*.egg-info
%{py_puresitedir}/frescobaldi_app/*.py*
%{py_puresitedir}/frescobaldi_app/autocomplete
%{py_puresitedir}/frescobaldi_app/charmap
%{py_puresitedir}/frescobaldi_app/css
%{py_puresitedir}/frescobaldi_app/docbrowser
%{py_puresitedir}/frescobaldi_app/doclist
%{py_puresitedir}/frescobaldi_app/engrave
%{py_puresitedir}/frescobaldi_app/help
%{py_puresitedir}/frescobaldi_app/hyphdicts
%{py_puresitedir}/frescobaldi_app/icons
%{py_puresitedir}/frescobaldi_app/language_names
%{py_puresitedir}/frescobaldi_app/lilydoc
%{py_puresitedir}/frescobaldi_app/logtool
%{py_puresitedir}/frescobaldi_app/ly
%{py_puresitedir}/frescobaldi_app/midifile
%{py_puresitedir}/frescobaldi_app/miditool
%{py_puresitedir}/frescobaldi_app/musicview
%{py_puresitedir}/frescobaldi_app/pitch
%dir %{py_puresitedir}/frescobaldi_app/po
%{py_puresitedir}/frescobaldi_app/po/*.py*
%{py_puresitedir}/frescobaldi_app/portmidi
%{py_puresitedir}/frescobaldi_app/preferences
%{py_puresitedir}/frescobaldi_app/qmidi
%{py_puresitedir}/frescobaldi_app/qpopplerview
%{py_puresitedir}/frescobaldi_app/quickinsert
%{py_puresitedir}/frescobaldi_app/remote
%{py_puresitedir}/frescobaldi_app/rhythm
%{py_puresitedir}/frescobaldi_app/scorewiz
%{py_puresitedir}/frescobaldi_app/sessions
%{py_puresitedir}/frescobaldi_app/sidebar
%{py_puresitedir}/frescobaldi_app/snippet
%{py_puresitedir}/frescobaldi_app/splashscreen
%{py_puresitedir}/frescobaldi_app/symbols
%{py_puresitedir}/frescobaldi_app/vimode
%{py_puresitedir}/frescobaldi_app/widgets
%lang(cs) %{py_puresitedir}/frescobaldi_app/po/cs.mo
%lang(de) %{py_puresitedir}/frescobaldi_app/po/de.mo
%lang(es) %{py_puresitedir}/frescobaldi_app/po/es.mo
%lang(fr) %{py_puresitedir}/frescobaldi_app/po/fr.mo
%lang(gl) %{py_puresitedir}/frescobaldi_app/po/gl.mo
%lang(it) %{py_puresitedir}/frescobaldi_app/po/it.mo
%lang(nl) %{py_puresitedir}/frescobaldi_app/po/nl.mo
%lang(pl) %{py_puresitedir}/frescobaldi_app/po/pl.mo
%lang(pt_BR) %{py_puresitedir}/frescobaldi_app/po/pt_BR.mo
%lang(ru) %{py_puresitedir}/frescobaldi_app/po/ru.mo
%lang(tr) %{py_puresitedir}/frescobaldi_app/po/tr.mo
%lang(uk) %{py_puresitedir}/frescobaldi_app/po/uk.mo

#--------------------------------------------------------------------

%prep
%setup -q

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}
%__mkdir_p %{buildroot}%{_docdir}/%{name}
