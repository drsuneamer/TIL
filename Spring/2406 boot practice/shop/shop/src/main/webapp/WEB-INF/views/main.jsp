<%@ page language="java" contentType="text/html; charset=UTF-8" 
	pageEncoding="UTF-8" %>

<!DOCTYPE html>
<html>
<body>
<h1>Main</h1>
<hr/>

<%
	String id = (String)session.getAttribute("id");
	String msg = (String)request.getAttribute("message");
%>

	Welcome... <%= id %>
	<hr/>
	<%= msg %>

</body>
</html>