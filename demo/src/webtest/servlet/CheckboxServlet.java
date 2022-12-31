package webtest.servlet;

import webdesign.WriteSql;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Date;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;


public class CheckboxServlet extends HttpServlet{

    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // TODO Auto-generated method stub
        doPost(req, resp);
    }
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        request.setCharacterEncoding("UTF-8");//编码部分
        response.setCharacterEncoding("UTF-8");
        response.setHeader("content-type", "text/html;charset=UTF-8");//解码部分
        WriteSql hobbycount =new WriteSql();
        PrintWriter hh=response.getWriter();

        HttpSession session = request.getSession();
        //将数据存储到session中
        String id= (String) session.getAttribute("id");
        //获取session的Id
        System.out.println(id+"正在勾选hobby");
        String hobby1=request.getParameter("hobby1");
        if(hobby1!=null)        {hobbycount.writehobby("财经",id);}
        String hobby2=request.getParameter("hobby2");
        if(hobby2!=null)        {hobbycount.writehobby("彩票",id);}
        String hobby3=request.getParameter("hobby3");
        if(hobby3!=null)        {hobbycount.writehobby("房产",id);}
        String hobby4=request.getParameter("hobby4");
        if(hobby4!=null)        {hobbycount.writehobby("股票",id);}
        String hobby5=request.getParameter("hobby5");
        if(hobby5!=null)        {hobbycount.writehobby("家居",id);}
        String hobby6=request.getParameter("hobby6");
        if(hobby6!=null)        {hobbycount.writehobby("教育",id);}
        String hobby7=request.getParameter("hobby7");
        if(hobby7!=null)        {hobbycount.writehobby("科技",id);}
        String hobby8=request.getParameter("hobby8");
        if(hobby8!=null)        {hobbycount.writehobby("社会",id);}
        String hobby9=request.getParameter("hobby9");
        if(hobby9!=null)        {hobbycount.writehobby("时尚",id);}
        String hobby10=request.getParameter("hobby10");
        if(hobby10!=null)        {hobbycount.writehobby("时政",id);}
        String hobby11=request.getParameter("hobby11");
        if(hobby11!=null)        {hobbycount.writehobby("体育",id);}
        String hobby12=request.getParameter("hobby12");
        if(hobby12!=null)        {hobbycount.writehobby("星座",id);}
        String hobby13=request.getParameter("hobby13");
        if(hobby13!=null)        {hobbycount.writehobby("游戏",id);}
        String hobby14=request.getParameter("hobby14");
        if(hobby14!=null)        {hobbycount.writehobby("娱乐",id);}

        request.getRequestDispatcher("info").forward(request,response);


    }
}
