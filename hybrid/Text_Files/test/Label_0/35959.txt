import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner stdIn=new Scanner(System.in);
		int n=stdIn.nextInt(),k=stdIn.nextInt(),x=stdIn.nextInt(),y=stdIn.nextInt(),s=0,i;
		for(i=0;i<n&&i<k;i++) s+=x;
		for(i=k;i<n;i++) s+=y;
		System.out.print(s);
	}
}