import java.io.*;
class Main
{
public static void main(String args[])throws IOException
{
BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
while(true)
{
String str=input.readLine();
String str_ary[]=str.split(" ");
if(str_ary[0].equals("0") && str_ary[1].equals("0") && str_ary[2].equals("0") && str_ary[3].equals("0") &&str_ary[4].equals("0")&& str_ary[5].equals("0"))break;
int x[]=new int[6];
for(int i=0;i<6;i++)
{
x[i]=Integer.parseInt(str_ary[i]);
}
int score=15*(x[0]+x[1])+15*(x[0]*5+x[1]*3)+7*x[2]+2*x[3]+100-3*(x[5]-x[4]-(x[0]*5+x[1]*3))-2*(x[0]*5+x[1]*3);
System.out.println(score);
}
}
}