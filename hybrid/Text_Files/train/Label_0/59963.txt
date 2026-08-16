import java.util.*;
public class JerrysProtest
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();
		
		int[] array = new int[n];
		for(int x = 0; x < n; x++)
		{
			array[x] = in.nextInt();
		}
		
		Arrays.sort(array);
		
		long[] freq = new long[5000];
		for(int y = 0; y < array.length; y++)
		{
			for(int z = y + 1; z < array.length; z++)
			{
				freq[array[z] - array[y]]++;
			}
		}
		
		long[] sum = new long[freq.length + 1];
		for(int a = freq.length - 1; a >= 0; a--)
		{
			sum[a] = sum[a + 1] + freq[a];
		}
		
		long count = 0;
		for(int a = 0; a < freq.length; a++)
		{
			for(int b = 0; b < freq.length; b++)
			{
				if(a + b < 5000)
				{
					count += freq[a] * freq[b] * sum[a + b + 1];
				}
			}
		}
		
		long total = (n * (n - 1)) / 2;
		total = total * total * total;
		
		System.out.println((double)count / total);
	}
}
