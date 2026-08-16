import java.util.*;
import java.io.*;

public class Main{
  public static void main(String[] args) throws Exception{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String s = br.readLine();
    
    if(s.equals("A")) System.out.println("T");
    else if(s.equals("T")) System.out.println("A");
    else if(s.equals("G")) System.out.println("C");
    else System.out.println("G");
  }
}