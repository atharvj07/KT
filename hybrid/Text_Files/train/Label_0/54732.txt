import java.util.*;

public class Main{

public static void main(String[] args){
Scanner obj=new Scanner(System.in);
int n=obj.nextInt();
String g=obj.next();
if(n%2!=0){
System.out.println("No");
}else{
int p=n/2;
int q=p;
int h=0;
boolean flag=true;

for(;h<p;h++,q++){

if(g.charAt(h)!=g.charAt(q)){
flag=false;
}

}

if(flag){

System.out.println("Yes");
}else{
System.out.println("No");
}
}

}

}