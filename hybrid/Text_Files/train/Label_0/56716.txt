import java.util.Scanner;
import java.lang.Math.*;
public class jamesrodriguez
{
 public static void main(String[]args)
 { 
  Scanner sc=new Scanner(System.in);
  int t=sc.nextInt();
  int odd=0;
  int even=0;
  while(t-->0){
   if(sc.nextInt()%2==0){
    even++;
   }
   else{
    odd++;
   }
  }
  System.out.println(Math.min(odd,even));
 }
}
