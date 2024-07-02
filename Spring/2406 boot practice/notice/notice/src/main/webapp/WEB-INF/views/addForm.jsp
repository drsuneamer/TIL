<%@ page language="java" contentType="text/html; charset=UTF-8" 
	pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<body>

<form action="/notice/add" method="post">
<table border="1">
	<tr>
		<th>Title</th>
		<td><input type="text" name="title" /></td>
	</tr>
	<tr>
		<th>Content</th>
		<td><textarea name="content"></textarea></td>
	</tr>
	<tr>
		<th colspan="2">
			<input type="submit" value="add" />
		</th>
	</tr>
</table>
</form>

</body>
</html>