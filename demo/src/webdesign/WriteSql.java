package webdesign;

import java.sql.*;
public class WriteSql {
        static Connection con;
        static Statement sql;
        static ResultSet res;
        public Connection Connection(){
                // TODO Auto-generated method stub
                String Driver="com.mysql.cj.jdbc.Driver";
                String url="jdbc:mysql://localhost:3306/test?useSSL=false&serverTimezone=UTC";
                String name="root";
                String code="toor";

                try {
                        Class.forName(Driver);
                }
                catch(ClassNotFoundException e) {
                        e.printStackTrace();
                }
                try {
                        con=DriverManager.getConnection(url, name, code);
                        return con;
                }
                catch(SQLException e) {
                        e.printStackTrace();
                }
                return con;
        }
        public boolean ifTableNull(String id)  {
                WriteSql c=new WriteSql();
                con=c.Connection();
                String if_check = "0";
                try {
                        sql=con.createStatement();
                        res=sql.executeQuery("select * from new");
                        while(res.next()) {
                                if(id.equals(res.getString("id"))){
                                        if(
                                        if_check.equals(res.getString("财经")) &&
                                        if_check.equals(res.getString("彩票")) &&
                                        if_check.equals(res.getString("房产")) &&
                                        if_check.equals(res.getString("股票")) &&
                                        if_check.equals(res.getString("家居")) &&
                                        if_check.equals(res.getString("教育")) &&
                                        if_check.equals(res.getString("科技")) &&
                                        if_check.equals(res.getString("社会")) &&
                                        if_check.equals(res.getString("时尚")) &&
                                        if_check.equals(res.getString("时政")) &&
                                        if_check.equals(res.getString("体育")) &&
                                        if_check.equals(res.getString("星座")) &&
                                        if_check.equals(res.getString("游戏")) &&
                                        if_check.equals(res.getString("娱乐"))


                                ) {
                                        System.out.println("欢迎新人");
                                        return true;
                                } else {
                                        System.out.println("你好，老朋友");
                                        return false;
                                }
                                }//先判别id
                        }//while

                }
                catch(SQLException e) {
                        e.printStackTrace();
                }

                return true;
        }

        public void register(String id,String password) {
                WriteSql c=new WriteSql();
                con=c.Connection();
                try {
                        sql=con.createStatement();
                        String  code= "insert into new (id,password, `财经`, `彩票`, `房产`, `股票`, `家居`, `教育`, `科技`, `社会`, `时尚`, `时政`, `体育`, `星座`, `游戏`, `娱乐`) VALUES (?, ?, '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0');";
                        PreparedStatement pst=con.prepareStatement(code);
                        pst.setString(1, id);
                        pst.setString(2, password);
                        pst.executeUpdate();
                }
                catch (SQLException e){
                        e.printStackTrace();
                }

        }

        public void SaveFootPrint(String id,String time,String footprint) {
                WriteSql c=new WriteSql();
                con=c.Connection();
                try {
                        sql=con.createStatement();
                        String  code= "insert into "+id+" (time,footprint) values(?,?)";
                        PreparedStatement pst=con.prepareStatement(code);
                        pst.setString(1, time);
                        pst.setString(2, footprint);
                        pst.executeUpdate();
                }
                catch (SQLException e){
                        e.printStackTrace();
                }

        }

        public void writehobby(String hobbyterm,String id) {
                WriteSql c=new WriteSql();
                con=c.Connection();

                String  code="UPDATE new SET "+hobbyterm+" = 1 WHERE ( id = ?);";
                System.out.println(code);
                try {
                        sql=con.createStatement();
                        PreparedStatement x = con.prepareStatement(code);
                        x.setString(1,id);
                        x.executeUpdate();
                } catch (SQLException throwables) {
                        throwables.printStackTrace();
                }


        }

        public boolean seekid_psd (String id,String password) {
                WriteSql c=new WriteSql();
                con=c.Connection();
                try {
                        sql=con.createStatement();
                        res=sql.executeQuery("select * from new");
                        while(res.next()) {
                                if(id.equals(res.getString("id"))) {
                                        if(password.equals(res.getString("password"))) {
                                                System.out.println("登录成功");
                                                return true;
                                        }

                                        else {
                                                System.out.println("密码错误！");
                                                return false;
                                        }

                                }
                        }
                        System.out.println("无此用户！");
                        return false;
                }
                catch(SQLException e) {
                        e.printStackTrace();
                        return false;
                }
        }

        public boolean seek (String id,String password) {
                WriteSql c=new WriteSql();
                con=c.Connection();
                try {
                        sql=con.createStatement();
                        res=sql.executeQuery("select time from new");
                        while(res.next()) {
                                if(id.equals(res.getString("id"))) {
                                        if(password.equals(res.getString("password"))) {
                                                System.out.println("登录成功");
                                                return true;
                                        }

                                        else {
                                                System.out.println("密码错误！");
                                                return false;
                                        }

                                }
                        }
                        System.out.println("无此用户！");
                        return false;
                }
                catch(SQLException e) {
                        e.printStackTrace();
                        return false;
                }
        }

        public boolean seekuser (String id) {
                WriteSql c=new WriteSql();
                con=c.Connection();
                try {
                        sql=con.createStatement();
                        res=sql.executeQuery("select * from new");
                        while(res.next()) {
                                if(id.equals(res.getString("id"))) {
                                        return true;
                                }
                        }
                        System.out.println("恭喜！id可用！");
                        return false;
                }
                catch(SQLException e) {
                        e.printStackTrace();
                        return false;
                }
        }

        public boolean CreateIdTable (String id) {
                WriteSql c=new WriteSql();
                con=c.Connection();
                try {
                        sql=con.createStatement();
                        String code="create table if not exists "+id+" ( `time` VARCHAR(50) NOT NULL,`footprint` VARCHAR(10000) NULL, PRIMARY KEY (`time`)); ";
                        PreparedStatement pst=con.prepareStatement(code);
                        pst.executeUpdate();
                        return false;
                }
                catch(SQLException e) {
                        e.printStackTrace();
                        return false;
                }
        }



        public static void main(String[] args)  {
                WriteSql c=new WriteSql();
                //c.read("ggj");
                c.register("ggj","123");
        }

}