import java.util.Arrays;
import java.util.Scanner;

public class  Main
{
	public static void main(String arg[])
	{
		Scanner sc = new Scanner(System.in);

		while(sc.hasNext())
		{
			int n = sc.nextInt();
			int ans =0;
			boolean a[] = new boolean [n+1];
			Arrays.fill(a, true);
			a[0]=a[1]=false;

			for (int p=2; p*p<=n; p++) 
			{
				if (!a[p]) 
					continue;
				for (int j = p+p; j<= n; j += p)   //合成数jを消す
				{ 
					a[j] = false;
				}
			}
			for(int i =0; i<=n; i++)
			{
				if(a[i])
					ans++;
			}
			System.out.println(ans);
		}
	}

}