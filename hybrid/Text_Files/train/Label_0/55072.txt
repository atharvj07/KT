import java.util.Scanner;
class Main {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       String a=sc.next();
       String b=sc.next();
       String c=sc.next();
       String ans="";
       ans+=a.charAt(0);
       ans+=b.charAt(0);
       ans+=c.charAt(0);
       System.out.println(ans.toUpperCase());
       
 }
 }          