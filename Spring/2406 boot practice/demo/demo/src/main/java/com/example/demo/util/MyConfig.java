package com.example.demo.util;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Scope;

@Configuration
public class MyConfig {
	
	@Bean("scopeTest")
	@Scope("prototype")
	public ScopeTest getOne() {
		return new ScopeTest();
	}
	
//	@Bean("callbackTest")
	@Bean(name = "callbackTest", initMethod = "myInit")
	public CallbackTest getTwo() {
		return new CallbackTest();
	}
	
//	@Bean
//	public Member getThree() {
//		return new Member();
//	}
}
