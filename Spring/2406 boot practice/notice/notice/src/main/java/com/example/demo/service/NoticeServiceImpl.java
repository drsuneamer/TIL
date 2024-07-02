package com.example.demo.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.entity.Notice;
import com.example.demo.repository.NoticeDAO;

@Service
public class NoticeServiceImpl implements NoticeService {

	@Autowired
	private NoticeDAO dao;
	
	@Override
	public List<Notice> list() {
		return dao.findAll();
	}

	@Override
	public Notice detail(int noticeNum) {
		return dao.findById(noticeNum).get();
	}

	@Override
	public void add(Notice notice) {
		dao.save(notice);
	}
	
}
