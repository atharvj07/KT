import java.util.*;
public class T{
public static void main(String [] arg){
Scanner in =new Scanner(System.in);
String f=in.next();
int ca=0,cl=0;
for(int i=0;i<f.length();i++){
if(f.charAt(i)=='a')
ca++;
else
cl++;
}
if(ca>cl)
System. out.print(f.length());
else{
int g=0;
while(ca<=cl){
g++;
cl--;
}
System.out.print(f.length()-g);
 }
}}