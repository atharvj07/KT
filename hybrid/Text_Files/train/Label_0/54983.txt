import java.io.*;
import static java.lang.Integer.parseInt;
import java.util.*;
import javax.swing.*;

public class Start 
{
  public static void main(String arge[]) throws IOException
  {
    BufferedReader in =new BufferedReader(new InputStreamReader(System.in));
    StringBuilder out =new StringBuilder();
    StringTokenizer tk;
    
    int tc=parseInt(in.readLine());
    
    while(tc-- >0)
    {
      tk=new StringTokenizer(in.readLine());
      int a=parseInt(tk.nextToken()),b=parseInt(tk.nextToken()),n=parseInt(tk.nextToken());
      int ans=get(a,b,n%3);
      out.append(ans).append("\n");
    
    }
      System.out.print(out);
           
          
     
     
   
  }
  public static int get(int a,int b,int n)
  {
    if (n==0)
        return a;
    if (n==1)
        return b;
     
     
    return a^b;
  
  }

}
