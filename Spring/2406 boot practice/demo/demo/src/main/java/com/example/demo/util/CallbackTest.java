package com.example.demo.util;

import org.springframework.beans.factory.InitializingBean;

import jakarta.annotation.PostConstruct;

public class CallbackTest implements InitializingBean {

	public CallbackTest() {
		System.out.println("CallbackTest 생성자");
	}
	
	@PostConstruct
	public void one() {
		System.out.println("==> @PostContruct call");
	}

	@Override
	public void afterPropertiesSet() throws Exception {
		System.out.println("==> InitializingBean : afterPropertiesSet()");
	}
	
	public void myInit() {
		System.out.println("===> myInit() call");
	}
}
