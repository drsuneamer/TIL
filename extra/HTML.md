# HTML

## Form

>https://www.youtube.com/watch?v=sFtZdlmgCVY

- 입력한 정보를 서비스를 제공하는 서버에 전송할 때 사용 (입력, 선택 등)

- 사용자로부터 정보를 입력받을 때 - `input` tag

  ```html
  <form action="http://localhost/login.php">
      <p><input type="text" name="id"></p> 	<!-- 사용자로부터 문자를 입력 받음 -->
  	<p><input type="password" name="pw"></p>
      <p>주소: <input type="text" name="address"</p>
  	<input type="submit">	<!-- 정보 제출 (어디로? -> form!) -->
  </form>
  ```

  