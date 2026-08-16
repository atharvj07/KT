import java.util.*;
public class InvadLove {
public static void main(String [] args){
Scanner in=new Scanner(System.in);
int n=in.nextInt();
int m=in.nextInt();
if(m==0){
System.out.println("1 0");
System.out.println(n+" 0");
System.out.println("0 0");
System.out.println(n-1+" 0");
}
else if(n==0){
System.out.println("0 1");
System.out.println("0 "+m);
System.out.println("0 0");
System.out.println("0 "+ (m-1));
}
else if(m>n){
double a=3*Math.sqrt(n*n+m*m)-2*Math.sqrt(2);
double b=Math.sqrt(n*n +m*m)+2*Math.sqrt((n-1)*(n-1)+m*m);
double d=2*Math.sqrt(n*n +m*m)+m;
if(d>=a && d>=b){
System.out.println("0 0");
System.out.println(n+" "+m);
System.out.println(n+" 0");
System.out.println("0 "+m);
}
else if(a>=b && a>=d){
System.out.println("1 1");
System.out.println(n+" "+m);
System.out.println("0 0");
System.out.println((n-1)+" "+(m-1));
}
else if(b>=a && b>=d){
System.out.println("1 0");
System.out.println(n+" "+m);
System.out.println("0 0");
System.out.println((n-1)+" "+(m));
}
}
else if(m<=n){
double a=3*Math.sqrt(n*n+m*m)-2*Math.sqrt(2);
double b=Math.sqrt(n*n +m*m)+2*Math.sqrt((n)*(n)+(m-1)*(m-1));
double d=2*Math.sqrt(n*n +m*m)+n;
if(d>=a && d>=b ){
System.out.println("0 0");
System.out.println(n+" "+m);
System.out.println("0 " +m);
System.out.println(n+" 0");
}
else if(a>=b && a>=d){
System.out.println("1 1");
System.out.println(n+" "+m);
System.out.println("0 0");
System.out.println((n-1)+" "+(m-1));
}
else if(b>=a && b>=d){
System.out.println("0 1");
System.out.println(n+" "+m);
System.out.println("0 0");
System.out.println(n+" "+(m-1));
}
}
}
}