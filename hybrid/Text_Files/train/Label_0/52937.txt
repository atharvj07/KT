import java.io.*;
import java.util.*;
public class q1
{
  public static void main(String args[])throws IOException
  {
    Scanner in=new Scanner(System.in);
    PrintWriter pw=new PrintWriter(System.out, true);
    int a=in.nextInt();
    int b=in.nextInt();
    int dis=Math.abs(a-b);
    int ma=dis/2;
    int mb=dis/2;
    if(dis%2!=0)
    mb+=1;
    int tot=ma*(ma+1)/2;
    tot+=mb*(mb+1)/2;
    pw.println(tot);
  }
}
