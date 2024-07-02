package com.example.demo.util;

import org.springframework.beans.factory.annotation.Value;

public class Member {

	@Value("${name}")
	private String name;
	
	@Value("${address}")
	private String address;
	
	@Value("${age}")
	private int age;

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}
	
	
}
