<%@ page language="java" contentType="text/html; charset=UTF-8" 
	pageEncoding="UTF-8" %>
<%@ page import="com.example.demo.entity.*" %>
<!DOCTYPE html>
<html>
<body>

<%
	Notice notice = (Notice)request.getAttribute("notice");
%>

<table border="1">
	<tr>
		<th>Num</th>
		<td><%= notice.getNoticeNum() %></td>
	</tr>
	<tr>
		<th>Title</th>
		<td><%= notice.getTitle() %></td>
	</tr>
	<tr>
		<th>Content</th>
		<td><%= notice.getContent() %></td>
	</tr>
	<tr>
		<th>Hit</th>
		<td><%= notice.getHit() %></td>
	</tr>
</table>

</body>
</html>