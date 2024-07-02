package com.example.demo.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.example.demo.entity.Notice;
import com.example.demo.service.NoticeService;

@Controller
public class NoticeController {

	@Autowired
	private NoticeService service;
	
	@GetMapping("/notice/list")
	public String list(Model model) {
		List<Notice> noticeList = service.list();
		
		model.addAttribute("noticeList", noticeList);
		
		return "list";
	}
	
	@GetMapping("/notice/detail")
	public String detail(@RequestParam int noticeNum, Model model) {
		Notice notice = service.detail(noticeNum);
		
		model.addAttribute("notice", notice);
		
		return "detail";
	}
	
	@GetMapping("/notice/addForm")
	public String addForm() {
		return "addForm";
	}
	
	@PostMapping("/notice/add")
	public String add(Notice notice) {
		service.add(notice);
		
		return "redirect:/notice/list";
	}
	
}
