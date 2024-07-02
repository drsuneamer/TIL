package com.example.demo.service;

import java.util.List;

import com.example.demo.entity.Notice;

public interface NoticeService {
	public List<Notice> list();
	
	public Notice detail(int noticeNum);
	
	public void add(Notice notice);
}
