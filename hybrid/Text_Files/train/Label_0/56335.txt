import java.util.Scanner;
class Main
{
    public static void main(String args[])
    {
	Scanner scan=new Scanner(System.in);
	while(scan.hasNext())
	    {
		int a,b;
		a=scan.nextInt();
		b=scan.nextInt();
		System.out.println(a+b);
	    }
    }
}