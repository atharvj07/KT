import java.util.Scanner;
public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n;
		double[] data1 =new double[1001];
		double[] data2 =new double[1001];
		double[] ans =new double[1001];
		double D=0,D2=0,D3=0,D4=0;

		n = sc.nextInt();
		for(int i=0;i<n;i++)data1[i]=sc.nextDouble();
		for(int i=0;i<n;i++)data2[i]=sc.nextDouble();
		for(int i=0;i<n;i++)ans[i] = data1[i]-data2[i];
		for(int i=0;i<n;i++){
			D +=Math.abs(ans[i]);
			D2 +=Math.pow(Math.abs(ans[i]),2);
			D3 +=Math.pow(Math.abs(ans[i]),3);
			if(Math.abs(ans[i])>D4)D4=Math.abs(ans[i]);
			
		}
		System.out.println(D);
		System.out.println(Math.sqrt(D2));
		System.out.println(Math.cbrt(D3));
		System.out.println(D4);
		
		sc.close();

	}

}

