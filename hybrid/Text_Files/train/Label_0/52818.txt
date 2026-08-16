import java.util.*;
import java.io.*;

public class Main{
  public static void main(String[] args){
     Scanner scanner = new Scanner(System.in);
     String str = scanner.nextLine();
     int q = scanner.nextInt();
     for(int i=0;i<q;i++){
       String ope = scanner.next();
       if(ope.equals("print")){
         int a = scanner.nextInt();
         int b = scanner.nextInt();
         System.out.println(str.substring(a,b+1));
       }
       if(ope.equals("reverse")){
         int a = scanner.nextInt();
         int b = scanner.nextInt();
         StringBuffer rstr = new StringBuffer(str);
         StringBuffer sb = new StringBuffer(str.substring(a,b+1));
         String revstr = sb.reverse().toString();
         str = rstr.replace(a,b+1,revstr).toString();
       }
       if(ope.equals("replace")){
         int a = scanner.nextInt();
         int b = scanner.nextInt();
         String pstr = scanner.next();
         StringBuffer rstr = new StringBuffer(str);
         str = rstr.replace(a,b+1,pstr).toString();
       }
     }
  }
}

