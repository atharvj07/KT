import java.util.Scanner;
public class Main
{
  public static void main(String[]args)
  {
    Scanner input=new Scanner(System.in);
    int h=0,j=0;
    while(true)
    {int a=input.nextInt();
    int b=input.nextInt();
    if(a==0 && b==0)
      break;
   for(int p=1;p<=a;p++)
     {
       for(int i=1;i<=b;i++)
       {if( p>=2 && i>=2 && p<=a-1 && i<=b-1)
         System.out.print(".");
       else
         System.out.print("#");
       }
      System.out.println();}
       System.out.println();
     }
    }
     }
