import java.sql.*; 

class JdbcTest1 { 

  public static void main (String[] args) { 
    try
    {
      // Step 1: "Load" the JDBC driver
      Class.forName("oracle.jdbc.driver.OracleDriver"); 

      // Step 2: Establish the connection to the database 
      String url = "jdbc:oracle:thin//10.132.55.239:1523/LATKRC"; 
      Connection conn = DriverManager.getConnection(url,"LAT_NETWORK_REPOSITORY","insight");  
    }
    catch (Exception e)
    {
      System.err.println("D'oh! Got an exception!"); 
      System.err.println(e.getMessage()); 
      System.err.println(e.printStacktrace());
    } 
  } 
} 