package com.sample.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class OtherController {

	@GetMapping("/test")
	public String test() {
		return "test";
	}
}
