<%@ page language="java" contentType="text/html; charset=UTF-8" 
	pageEncoding="UTF-8" %>

<!DOCTYPE html>
<html>
<body>

<h1>Login</h1>
<hr/>

<!--<form action="/loginFive" method="post">-->

<form action="/login" method="post">
<table border="1">
	<tr>
		<th>ID</th>
		<td><input type="text" name="id" /></td>
	</tr>
	<tr>
		<th>PWD</th>
		<td><input type="password" name="pwd" /></td>
	</tr>
	<tr>
		<th colspan="2">
			<input type="submit" value="login" />
		</th>
	</tr>
</table>
</form>

</body>
</html>