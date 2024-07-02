package com.example.demo.controller;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.dto.MemberDTO;
import com.example.demo.service.MemberService;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;

@Controller
//@RestController
public class MemberController {
	@Autowired
	private MemberService service;
	
	@GetMapping("/loginForm")
	public String loginForm() {
		return "loginForm";
	}
	
	@PostMapping("/login")
	public String login(Model model, HttpServletRequest request, HttpSession session) {
		String id = request.getParameter("id");
		String pwd = request.getParameter("pwd");
		
		boolean result = service.checkMember(id, pwd);
		
		if(result) {
			session.setAttribute("id", id);
			model.addAttribute("message", "Model set Test.....");
			
			return "redirect:/main";
			
		} else {
			return "error";
		}
	}
	
	@PostMapping("/loginTwo")
	public String loginTwo(ModelMap model,
			@RequestParam("id") String userId, 
			@RequestParam String pwd) {
		
		model.addAttribute("message", "ModelMap Test.....");
		System.out.println(userId + " : " + pwd);
		
		return "main";
	}
	
	@PostMapping("/loginThree")
	public ModelAndView loginThree(MemberDTO member) {
		
		System.out.println(member.getId() + " : " + member.getPwd());
		
		ModelAndView model = new ModelAndView();
		model.addObject("message", "ModelAndView Test......");
		model.setViewName("main");
		
		return model;
	}
	
	@PostMapping("/loginFour")
	public String loginFour(@RequestParam Map<String, String> member) {
		
		System.out.println(member.get("id"));
		System.out.println(member.get("pwd"));
		
		return "redirect:/main";
	}
	
	@PostMapping("/loginFive")
	public String loginFive(
			@ModelAttribute("id") String id,
			@ModelAttribute("pwd") String pwd) {

		System.out.println(id);
		System.out.println("----");
		System.out.println(pwd);

		return "redirect:/main";
	}
	
	@GetMapping("/{one}/pathTest/seq/{two}")
	public String pathTest(
			@PathVariable String one, 
			@PathVariable String two) {
		
		System.out.println(one + " ::: " + two);
		
		return "redirect:/main";
	}
	
	@GetMapping("resBody")
	@ResponseBody
	public MemberDTO resBody() {
		MemberDTO mem = new MemberDTO();
		mem.setId("test");
		mem.setPwd("1234");
		
		return mem;
	}
	
}
