package com.example.demo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.repository.MemberRepository;

@Service
public class MemberServiceImpl implements MemberService {

	@Autowired
	private MemberRepository dao;
	
	@Override
	public boolean checkMember(String id, String pwd) {
		return dao.checkMember(id, pwd);
	}

}
