Summary:	A LilyPond sheet music editor
Name:		frescobaldi
Version:	2.0.8
Release:	1
Source0:	https://github.com/downloads/wbsoft/frescobaldi/%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.frescobaldi.org/
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


%changelog
* Thu Sep 20 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.0.8-1
+ Revision: 817182
- update to 2.0.8
- update to 2.0.6

* Fri Apr 27 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.0.5-1
+ Revision: 793862
- update to 2.0.5

* Mon Feb 13 2012 Andrey Bondrov <abondrov@mandriva.org> 2.0.2-1
+ Revision: 773835
- New version 2.0.2, major spec rework, drop all KDE4 stuff as it's not needed since 1.9.0

* Tue Jan 17 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.0.1-3
+ Revision: 761985
- Requires:python-poppler-qt4

* Fri Jan 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.0.1-2
+ Revision: 760605
- okular not needed

* Thu Jan 12 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.0.1-1
+ Revision: 760562
- version update 2.0.1
- version update 2.0.1

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 1.2.0-2
+ Revision: 677489
- rebuild for updated mimehandler

* Sun Dec 26 2010 Funda Wang <fwang@mandriva.org> 1.2.0-1mdv2011.0
+ Revision: 625127
- update to new version 1.2.0

* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 1.1.8-1mdv2011.0
+ Revision: 598310
- update to new version 1.1.8

* Mon Oct 04 2010 Funda Wang <fwang@mandriva.org> 1.1.7-2mdv2011.0
+ Revision: 582871
- requires lilypond
- update to new version 1.1.7

* Sat Sep 11 2010 Funda Wang <fwang@mandriva.org> 1.1.6-1mdv2011.0
+ Revision: 577481
- update file list
- new version 1.1.6

* Wed Jul 28 2010 Funda Wang <fwang@mandriva.org> 1.1.4-1mdv2011.0
+ Revision: 562676
- New version 1.1.4
- update to new version 1.1.3

* Thu Feb 18 2010 Funda Wang <fwang@mandriva.org> 1.0.2-1mdv2010.1
+ Revision: 507643
- new version 1.0.2

* Sun Jan 17 2010 Funda Wang <fwang@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 492594
- update to new version 1.0.1

* Sat Dec 26 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 482584
- update to new version 1.0.0

* Sun Nov 29 2009 Funda Wang <fwang@mandriva.org> 0.7.17-1mdv2010.1
+ Revision: 471334
- new version 0.7.17

* Mon Nov 16 2009 Funda Wang <fwang@mandriva.org> 0.7.16-1mdv2010.1
+ Revision: 466404
- new version 0.7.16

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 0.7.15-1mdv2010.1
+ Revision: 463297
- new version 0.7.15

* Sun Sep 13 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.14-1mdv2010.0
+ Revision: 438608
- update to new version 0.7.14

* Mon Aug 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.13-1mdv2010.0
+ Revision: 414368
- update to new version 0.7.13

* Thu Jul 02 2009 Funda Wang <fwang@mandriva.org> 0.7.12-1mdv2010.0
+ Revision: 391823
- New version 0.7.12

* Tue Jun 16 2009 Funda Wang <fwang@mandriva.org> 0.7.11-1mdv2010.0
+ Revision: 386240
- New verison 0.7.11

* Tue Jun 09 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.10-1mdv2010.0
+ Revision: 384465
- Update to new version 0.7.10
--This line, and those below, will be ignored--
  AM   SOURCES/frescobaldi-0.7.10.tar.gz
  D    SOURCES/frescobaldi-0.7.9.tar.gz
  M    SPECS/frescobaldi.spec

* Sun May 24 2009 Funda Wang <fwang@mandriva.org> 0.7.9-1mdv2010.0
+ Revision: 379129
- New version 0.7.9

* Sat Mar 21 2009 Funda Wang <fwang@mandriva.org> 0.7.8-1mdv2009.1
+ Revision: 359926
- with html
- BR kdelibs4
- only for kde 4.2
- New version 0.7.8

* Sat Feb 21 2009 Funda Wang <fwang@mandriva.org> 0.7.6-2mdv2009.1
+ Revision: 343614
- lilypond-kde4 is not needed

* Sat Feb 21 2009 Funda Wang <fwang@mandriva.org> 0.7.6-1mdv2009.1
+ Revision: 343613
- New version 0.7.6

* Thu Feb 12 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.5-1mdv2009.1
+ Revision: 339859
- update to new version 0.7.5

* Sun Feb 01 2009 Funda Wang <fwang@mandriva.org> 0.7.4-1mdv2009.1
+ Revision: 335964
- New verison 0.7.4

* Fri Jan 23 2009 Funda Wang <fwang@mandriva.org> 0.7.3-2mdv2009.1
+ Revision: 332847
- requires okular

* Thu Jan 22 2009 Funda Wang <fwang@mandriva.org> 0.7.3-1mdv2009.1
+ Revision: 332551
- import frescobaldi


