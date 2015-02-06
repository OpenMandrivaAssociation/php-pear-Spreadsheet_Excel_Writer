%define		_class		Spreadsheet
%define		_subclass	Excel
%define		upstream_name	%{_class}_%{_subclass}_Writer

Name:		php-pear-%{upstream_name}
Version:	0.9.3
Release:	2
Summary:	Package for generating Excel spreadsheets
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Spreadsheet_Excel_Writer/
Source0:	http://download.pear.php.net/package/Spreadsheet_Excel_Writer-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Spreadsheet_Excel_Writer was born as a porting of the
Spreadsheet::WriteExcel Perl module to PHP. It allows writing of Excel
spreadsheets without the need for COM objects. It supports formulas,
images (BMP) and all kinds of formatting for text and cells. It
currently supports the BIFF5 format (Excel 5.0), so functionality
appeared in the latest Excel versions is not yet available.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-2mdv2012.0
+ Revision: 742277
- fix major breakage by careless packager

* Wed Dec 14 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-1
+ Revision: 741270
- 0.9.2

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-8
+ Revision: 679581
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-7mdv2011.0
+ Revision: 613774
- the mass rebuild of 2010.1 packages

* Tue Nov 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.1-6mdv2010.1
+ Revision: 467085
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Oct 06 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-5mdv2010.0
+ Revision: 454611
- fix bad xml the hard way, fixes install

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.9.1-4mdv2010.0
+ Revision: 441570
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-3mdv2009.1
+ Revision: 322662
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-2mdv2009.0
+ Revision: 237067
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-1mdv2008.0
+ Revision: 15751
- 0.9.1


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8-8mdv2007.0
+ Revision: 82664
- Import php-pear-Spreadsheet_Excel_Writer

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8-8mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8-5mdk
- fix deps

* Fri Jul 22 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8-4mdk
- fix the package.xml file so it will register

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8-1mdk
- initial Mandriva package (PLD import)


