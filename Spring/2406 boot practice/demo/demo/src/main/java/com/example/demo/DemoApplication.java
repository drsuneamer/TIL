package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.config.StandardConfigDataLocationResolver;
import org.springframework.boot.web.servlet.context.AnnotationConfigServletWebServerApplicationContext;

import com.example.demo.util.Member;
import com.example.demo.util.ScopeTest;

//@SpringBootApplication

@SpringBootApplication(scanBasePackages = "com.*")
public class DemoApplication {
	
	static {
//		System.setProperty("spring.config.additional-location", "classpath:/imsi/");
	}

	public static void main(String[] args) {
//		ConfigurableApplicationContext cct =
		AnnotationConfigServletWebServerApplicationContext cct = 
				(AnnotationConfigServletWebServerApplicationContext)SpringApplication.run(DemoApplication.class, args);
		
		ScopeTest sOne = cct.getBean("scopeTest", ScopeTest.class);
		ScopeTest sTwo = cct.getBean("scopeTest", ScopeTest.class);
		
		System.out.println(sOne);
		System.out.println(sTwo);
		
//		Member member = cct.getBean(Member.class);
//		System.out.println( member.getName() );
//		System.out.println( member.getAddress() );
//		System.out.println( member.getAge() );
		
//		StandardConfigDataLocationResolver ss = null;
	}

}
