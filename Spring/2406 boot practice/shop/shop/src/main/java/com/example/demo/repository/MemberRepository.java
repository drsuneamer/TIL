package com.example.demo.repository;

import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Repository;

@Repository
public class MemberRepository {

	Map<String, String> memberList = new HashMap<String, String>();
	
	public MemberRepository() {
		memberList.put("hong", "1234");
		memberList.put("kim", "abcd");
	}
	
	public boolean checkMember(String id, String pwd) {
		String value = memberList.get(id);
		
		if(value == null || !value.equals(pwd) ) {
			return false;
		
		} else {
			return true;
		}
	}
}
