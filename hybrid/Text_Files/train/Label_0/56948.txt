import java.util.*;
public class prac {
    static Scanner sc=new Scanner(System.in);
    public static void main(String args[]) {
       StringBuffer s=new StringBuffer(sc.nextLine());
       int j=s.length()-1;
       int len=s.length();
       while(j>=1 && s.charAt(0)!=s.charAt(len-1))
       {
         if(s.charAt(j)==s.charAt(j-1))
         {
           StringBuffer str= new StringBuffer(s.substring(0, j));
           StringBuffer str1= new StringBuffer(s.substring(j));
           s=new StringBuffer(str.reverse().toString()+str1.reverse().toString());
         }
         j--;
       }
      //  System.out.print(s);
      int count=1;
      int ans=0;
      for(int i=1;i<s.length();i++)
      {
       if(s.charAt(i)!=s.charAt(i-1))
       count++;
       else{
         ans=Math.max(ans, count);
         count=1;
       }
      }
      ans=Math.max(ans,count);
      System.out.println(ans);
     }
    
    }
  