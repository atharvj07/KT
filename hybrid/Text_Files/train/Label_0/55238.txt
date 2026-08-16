import java.io.*;
import java.util.*;

public class Main
{
	
	public static void main(String[] args)throws IOException
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int ans = 0;
		for(int i = 0; i< n ; i++){
			int now = Integer.parseInt(br.readLine());
			if(now != 1){
				boolean isPrime = true;
				for(int j = 2 ; j*j <= now; j++)
				{
					if(now != j && now % j == 0){
						isPrime = false;
						break;
					}
				}
				if(isPrime) ans++ ;
			}
		}
		System.out.println(ans);
		
	}
}