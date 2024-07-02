package com.example.demo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import com.example.demo.service.WelcomeService;

@Controller
public class WelcomeController {

	@Autowired
	private WelcomeService service;
	
	@GetMapping("/index")
	public String index() {
		service.print();
		return "index";
	}
}
