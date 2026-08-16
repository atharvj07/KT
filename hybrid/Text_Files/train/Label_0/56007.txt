import java.util.Scanner;
public class Main
{
  public static void main(String[]args)
  {
    Scanner rbt=new Scanner(System.in);
    String x=rbt.next();
    int o=0, z=0, f=0;
    for(int i=0; i<x.length(); i++)
    {
      if(x.charAt(i)=='0')
      {
        z++;
        o=0;
      }
      else if(x.charAt(i)=='1')
      {
        o++;
        z=0;
      }
      if(o>=7 || z>=7)
      {
        f++;
        break;
      }
    }
    System.out.println((f>0)? "YES":"NO");
  }
}