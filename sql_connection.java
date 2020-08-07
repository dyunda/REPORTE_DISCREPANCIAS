import java.sql.*; 

class JdbcTest1 { 

  public static void main (String[] args) { 
    try
    {
      // Step 1: "Load" the JDBC driver
      Class.forName("oracle.jdbc.dr"); 

      // Step 2: Establish the connection to the database 
      String url = "jdbc:msql://:1114/contact_mgr"; 
      Connection conn = DriverManager.getConnection(url,"user1","password");  
    }
    catch (Exception e)
    {
      System.err.println("D'oh! Got an exception!"); 
      System.err.println(e.getMessage()); 
    } 
  } 
} 