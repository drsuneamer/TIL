<%@ page language="java" contentType="text/html; charset=UTF-8" 
	pageEncoding="UTF-8" %>
<%@ page import="java.util.*" %>
<%@ page import="com.example.demo.entity.*" %>
<!DOCTYPE html>
<html>
<body>

<%
	List<Notice> noticeList = 
			(List<Notice>)request.getAttribute("noticeList");
%>

<table border="1">
	<tr>
		<th>num</th>
		<th>title</th>
		<th>hit</th>
	</tr>
<%
	if(noticeList != null) {
		for(int i = 0; i < noticeList.size(); i++) {
			Notice notice = noticeList.get(i);
%>
	<tr>
		<td><%= notice.getNoticeNum() %></td>
		<td><a href="/notice/detail?noticeNum=<%= notice.getNoticeNum() %>"><%= notice.getTitle() %></a></td>
		<td><%= notice.getHit() %></td>
	</tr>
<%
		}
	}
%>
</table>
<p/>

<a href="/notice/addForm">add</a>

</body>
</html>