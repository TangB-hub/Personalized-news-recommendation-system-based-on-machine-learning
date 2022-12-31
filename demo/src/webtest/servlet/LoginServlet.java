package webtest.servlet;


import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.http.HttpSession;
import webdesign.WriteSql;
import javax.servlet.http.Cookie;


public class LoginServlet extends HttpServlet{
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // TODO Auto-generated method stub
        doPost(req, resp);
    }
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        request.setCharacterEncoding("UTF-8");//编码部分
        response.setCharacterEncoding("UTF-8");
        response.setContentType("text/html;charset=UTF-8");
        //response.setHeader("content-type", "text/html;charset=UTF-8");//解码部分

        PrintWriter printwriter=response.getWriter();//浏览器界面显示
        WriteSql verify = new WriteSql();


        //登录界面
        String id=request.getParameter("id");
        String password=request.getParameter("password");


        HttpSession session = request.getSession();
        //将数据存储到session中
        session.setAttribute("id", id);
        //获取session的Id
//        String sessionId = session.getId();
        //判断session是不是新创建的
//        if (session.isNew()) {
//            //response.getWriter().print("session创建成功，session的id是："+sessionId);
////
////            Cookie idcookie = new Cookie("id",id);//将登录信息加入cookie中
////
////            idcookie.setMaxAge(60*60*24*3); //设置cookie最大失效时间<br>　　　　　　　　　　　　　　cookie1.setMaxAge(60*60*24*3);
////
////            response.addCookie(idcookie);//将cookie返回加入
//
//
//
//        }else {
//            response.getWriter().print("id为 "+sessionId+" 已登录");
//            System.out.println("id为 "+sessionId+" 已登录");
//        }


        System.out.println(id);
        if(verify.seekid_psd(id,password)) {
            if(verify.ifTableNull(id)){
                response.sendRedirect("checkbox.html");
            }
            else{
                response.sendRedirect("info");
            }

        }
        else {
            printwriter.write("用户名或密码错误");//注册失败
            System.out.println("密码错误");
        }


    }

}
