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
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import javax.servlet.http.Cookie;


public class RefreshServlet extends HttpServlet{
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        request.setCharacterEncoding("UTF-8");//编码部分
        response.setCharacterEncoding("UTF-8");
        response.setContentType("text/html;charset=UTF-8");
        //response.setHeader("content-type", "text/html;charset=UTF-8");//解码部分

        PrintWriter out = response.getWriter();
        HttpSession session = request.getSession();
        String id= (String) session.getAttribute("id");
        WriteSql WithIdTable = new WriteSql();

        Process proc;
        try {
            out.println("<!DOCTYPE html>\n" +
                    "<html lang=\"en\">\n" +
                    "\n" +
                    "<head>\n" +
                    "  <meta charset=\"UTF-8\">\n" +
                    "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n" +
                    "  <title>Document</title>\n" +
                    "\n" +
                    "</head>\n" +
                    "\n"
            );
            //判别以id明明的表存不存在


            System.out.println("在refresh");
            proc= Runtime.getRuntime().exec("python E:\\FishBall\\demo\\simi_achieve.py "+ id );// 执行py文件


            //用输入输出流来截取结果
            BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
            String line = null;
            boolean i=true;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
                if(i){
                    out.println("<a href="+line);
                    i=false;
                }
                else {
                    out.println(" onclick=\"clickfunction(href)\">"+line+"</a><br/>");
                    i=true;
                }
            }


            in.close();//关闭输入流
            proc.waitFor();

            out.println("<script>\n" +
                    "  function clickfunction(webpos){\n" +
                    "    window.location=\"ClickServlet?webpos=\"+webpos;\n" +
                    "  }\n" +
                    "</script>\n" +
                    "\n" +
                    "<input  id=\"refresh\" type=\"button\" value=\"个性化推荐\" onclick=\"buttonClick();\">\n" +
                    "\n" +
                    "<script>\n" +
                    "  function buttonClick(){\n" +
                    "    alert(\"你已开启个性化推荐\");\n" +
                    "    window.location=\"refresh\";\n" +
                    "  }\n" +
                    "</script>\n" +
                    "</body>\n" +
                    "</html>");

        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }


    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        this.doGet(req, resp);
    }
}


// CREATE TABLE `test`.`id` ( `time` INT NOT NULL, `footprint` VARCHAR(45) NULL, PRIMARY KEY (`time`));