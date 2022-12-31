package webtest.servlet;


import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Date;

import webdesign.WriteSql;


public class RegisterServlet extends HttpServlet{
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

        WriteSql reging = new WriteSql();



        //注册界面
        String regid=request.getParameter("regid");
        String regpassword1=request.getParameter("regpassword1");
        String regpassword2=request.getParameter("regpassword2");


        if(regid==""||regpassword1==""||regpassword2=="") {
            printwriter.write("注册失败，用户名或密为空");//注册失败，用户名或密码不能为空
        }
        else {
            if (regpassword1.equals(regpassword2)) {

                if (reging.seekuser(regid)) {
                    printwriter.write("注册失败，该用户已存在");//该用户已存在，注册失败
                }
                else {
                    reging.register(regid, regpassword1);//使用上面的第二步，写入数据库
                    reging.CreateIdTable(regid);
                    response.sendRedirect("login.html");
                }
            } else {
                printwriter.write("注册失败，两次密码不一致");//两次密码不一致，注册失败
                response.sendRedirect("index.html");
            }
        }



    }

}
