package com.example.demo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class ShopController {

	@GetMapping("/main")
	public String main() {
		System.out.println("---> main");
		
//		Object obj = session.getAttribute("id");
//		
//		if(obj == null) {
//			return "redirect:/loginForm";
//		}		
		return "main";
	}
}
