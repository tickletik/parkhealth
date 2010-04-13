function hwsopen()

{
window.open("http://webapps.urac.org/healthwebsiteaccreditation/default.asp?id=878843645","plain","width=600","height=540");
}

function edopen()

{
window.open("http://www.adam.com/About_ADAM/Editorial/process.html","plain","width=915,height=540, location=yes,menubar=yes,scrollbars=yes,toolbars=yes,resizable=yes");
}

function edpolopen()

{
window.open("http://www.adam.com/EditorialPolicy.html","plain","width=915,height=540, location=yes,menubar=yes,scrollbars=yes,toolbars=yes,resizable=yes");
}

function ppopen()

{
window.open("http://www.adam.com/PrivacyStatement.html","plain","width=915,height=540, location=yes,menubar=yes,scrollbars=yes,toolbars=yes,resizable=yes");
}

txtCred = "<center>"+
"<table width='100%'>"+
"<tr>"+
"<td valign='top' align='left'>"+
"<img src='http://default.adam.com/urac/square-quart.gif'>"+
"</td>"+
"<td align='left'><font face='Arial, Helvetica, sans-serif' size='1'>"+
"A.D.A.M., Inc. is accredited by URAC, also known as the American Accreditation HealthCare Commission (www.urac.org). URAC's <a href='javascript:hwsopen();'>accreditation program</a> is an independent audit to verify that A.D.A.M. follows rigorous standards of quality and accountability. A.D.A.M. is among the first to achieve this important distinction for online health information and services. Learn more about A.D.A.M.'s  <a href='javascript:edpolopen();'>editorial policy</a>, <a href='javascript:edopen();'>editorial process</a> and <a href='javascript:ppopen();'>privacy policy</a>. A.D.A.M. is also a founding member of Hi-Ethics and subscribes to the principles of the Health on the Net Foundation (www.hon.ch).</font>"+
"</td>"+
"</tr>"+
"</table>"+
"</center>";

txtCredSSL = "<center>"+
"<table width='100%'>"+
"<tr>"+
"<td valign='top' align='left'>"+
"<img src='https://ssl.adam.com/urac/square-quart.gif'>"+
"</td>"+
"<td align='left'><font face='Arial, Helvetica, sans-serif' size='1'>"+
"A.D.A.M., Inc. is accredited by URAC, also known as the American Accreditation HealthCare Commission (www.urac.org). URAC's <a href='javascript:hwsopen();'>accreditation program</a> is an independent audit to verify that A.D.A.M. follows rigorous standards of quality and accountability. A.D.A.M. is among the first to achieve this important distinction for online health information and services. Learn more about A.D.A.M.'s  <a href='javascript:edpolopen();'>editorial policy</a>, <a href='javascript:edopen();'>editorial process</a> and <a href='javascript:ppopen();'>privacy policy</a>. A.D.A.M. is also a founding member of Hi-Ethics and subscribes to the principles of the Health on the Net Foundation (www.hon.ch).</font>"+
"</td>"+
"</tr>"+
"</table>"+
"</center>";

	if (SSL == 'https') {
		//window.alert('SSL exists');	
		document.write(txtCredSSL);
		}
	else {
		//window.alert(SSL + ' only here');
				document.write(txtCred);
	}
//document.write(txtCred); 