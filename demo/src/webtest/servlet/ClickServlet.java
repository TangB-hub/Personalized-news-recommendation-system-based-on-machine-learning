package webtest.servlet;
import webdesign.WriteSql;

import java.io.IOException;

import java.io.PrintWriter;

import java.util.Date;
import java.text.SimpleDateFormat;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

public class ClickServlet extends HttpServlet{
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // TODO Auto-generated method stub
        doPost(req, resp);
    }
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        request.setCharacterEncoding("UTF-8");//编码部分
        response.setCharacterEncoding("UTF-8");
        response.setHeader("content-type", "text/html;charset=UTF-8");//解码部分
        WriteSql footprintSQL =new WriteSql();
        PrintWriter printWriter=response.getWriter();



        HttpSession session = request.getSession();
        //将数据存储到session中
        String id= (String) session.getAttribute("id");
        //获取session的Id


        String webpos= request.getParameter("webpos");
        System.out.println(webpos);
        if(webpos!=null) {
            Date date = new Date();//获取当前的日期
            SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");//设置日期格式
            String time = df.format(date);//获取String类型的时间
            footprintSQL.SaveFootPrint(id, time, webpos);//将时间
        }


        String PersonalRefresh=request.getParameter("PersonalRefresh");

        if(PersonalRefresh.equals('1')){
            if(!footprintSQL.ifTableNull(id))
            //是否浏览过数据
            {
                printWriter.println("对不起亲，您还没在我这看过啥呢");
            }
            else{
                response.sendRedirect("info");
            }


        }


    }
}
